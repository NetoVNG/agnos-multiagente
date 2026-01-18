# api/main.py
from fastapi import FastAPI, HTTPException, Header, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Any
import os
import json
from pathlib import Path

from api.bootstrap_runtime import load_env, validate_keys, get_cors_origins, get_max_input_chars
from api.schemas import RouteRequest, RouteResponse
from tools.tools_logs_cognitivos import CognitiveLogger

from agents.agente_orquestrador import decidir_agente_llm, executar_agente_query

app = FastAPI(title="Sistema Multiagente (Agno)", version="0.2.0")
logger = CognitiveLogger()

# Configs
MAX_INPUT_CHARS = get_max_input_chars()
CORS_ORIGINS = get_cors_origins()


def require_api_key(x_api_key: Optional[str] = Header(default=None)) -> None:
    """
    Segurança simples:
    - Se API_KEY estiver definida no ambiente, exige header X-API-Key.
    - Se API_KEY não existir (dev), não bloqueia.
    """
    expected = (os.getenv("API_KEY") or "").strip()
    if not expected:
        return  # dev mode: sem chave
    if not x_api_key or x_api_key.strip() != expected:
        raise HTTPException(status_code=401, detail="Unauthorized: missing or invalid API key")


def enforce_input_limits(pergunta: str) -> None:
    if not pergunta or not pergunta.strip():
        raise HTTPException(status_code=422, detail="Campo 'pergunta' não pode ser vazio.")
    if len(pergunta) > MAX_INPUT_CHARS:
        raise HTTPException(
            status_code=413,
            detail=f"Pergunta muito longa. Limite: {MAX_INPUT_CHARS} caracteres.",
        )


@app.on_event("startup")
def startup():
    load_env()
    validate_keys()

    # CORS (se não configurar origins, mantém fechado)
    if CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


@app.get("/health")
def health():
    return {"status": "ok", "max_input_chars": MAX_INPUT_CHARS, "cors_origins": CORS_ORIGINS}


@app.get("/")
def root():
    return {"msg": "API no ar. Vá em /docs"}


@app.post("/route", response_model=RouteResponse, dependencies=[Depends(require_api_key)])
def route(req: RouteRequest, x_session_id: Optional[str] = Header(default=None)):
    session_id = x_session_id or logger.new_session_id()
    enforce_input_limits(req.pergunta)

    try:
        logger.log(
            session_id=session_id,
            event_type="routing_start",
            agent="api",
            action="route",
            input_text=req.pergunta,
            metadata={"endpoint": "/route"},
        )

        agente = decidir_agente_llm(req.pergunta)

        logger.log(
            session_id=session_id,
            event_type="routing_decision",
            agent="router-cognitivo",
            action="route",
            input_text=req.pergunta,
            output_text=agente,
            metadata={"endpoint": "/route"},
        )

        return RouteResponse(agente=agente, meta={"modo": "llm-routing", "session_id": session_id})

    except Exception as e:
        logger.log(session_id=session_id, event_type="error", agent="api", action="route", input_text=req.pergunta, output_text=str(e))
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/run", response_model=RouteResponse, dependencies=[Depends(require_api_key)])
def run(req: RouteRequest, x_session_id: Optional[str] = Header(default=None)):
    session_id = x_session_id or logger.new_session_id()
    enforce_input_limits(req.pergunta)

    try:
        logger.log(session_id=session_id, event_type="request_received", agent="api", action="run", input_text=req.pergunta)

        agente = decidir_agente_llm(req.pergunta)

        logger.log(session_id=session_id, event_type="routing_decision", agent="router-cognitivo", action="route", input_text=req.pergunta, output_text=agente)

        logger.log(session_id=session_id, event_type="agent_start", agent=agente, action="execute", input_text=req.pergunta)
        saida = executar_agente_query(agente, req.pergunta)
        logger.log(session_id=session_id, event_type="agent_end", agent=agente, action="respond", input_text=req.pergunta, output_text=saida)

        return RouteResponse(agente=agente, saida=saida, meta={"execucao": "ok", "session_id": session_id})

    except Exception as e:
        logger.log(session_id=session_id, event_type="error", agent="api", action="run", input_text=req.pergunta, output_text=str(e))
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# Debug endpoints (MVP)
# -----------------------------
def _read_jsonl_lines(path: Path, n: int = 50) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    # lê as últimas n linhas sem carregar o arquivo inteiro (MVP simples)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()[-n:]
    out = []
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        try:
            out.append(json.loads(ln))
        except Exception:
            continue
    return out


@app.get("/logs/last", dependencies=[Depends(require_api_key)])
def logs_last(n: int = Query(default=50, ge=1, le=500)):
    data = _read_jsonl_lines(logger.jsonl_path, n=n)
    return {"count": len(data), "items": data}


@app.get("/sessions/{session_id}", dependencies=[Depends(require_api_key)])
def logs_by_session(session_id: str, n: int = Query(default=200, ge=1, le=1000)):
    items = _read_jsonl_lines(logger.jsonl_path, n=n)
    filtered = [it for it in items if it.get("session_id") == session_id]
    return {"session_id": session_id, "count": len(filtered), "items": filtered}
