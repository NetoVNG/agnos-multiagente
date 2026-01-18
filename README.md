# Sistema Multiagente (Agno) — API + Tools + Logs Cognitivos

Projeto em Python para orquestrar **agentes especializados** (pesquisa, educação, planejamento, conteúdo e diagnóstico) usando **Agno** + **OpenAI**, com:

- **Roteamento por LLM** (Router Cognitivo)
- **Execução via FastAPI** (`/route` e `/run`)
- **Tools em camadas** (fundamentais, pesquisa, educacionais, planejamento, criativas, universais)
- **Logs cognitivos** (JSONL + Markdown) para auditoria e evolução do sistema
- **Deploy com Docker** 

---

## 🧠 Visão Geral

O sistema funciona assim:

1. O usuário envia uma pergunta.
2. O **Router Cognitivo** decide qual agente deve atuar.
3. O agente escolhido executa usando suas **tools**.
4. A API retorna:
   - `agente`: agente selecionado
   - `saida`: resposta gerada
   - `meta`: metadados (ex.: `session_id`, modo, etc.)
5. Todo o fluxo é registrado em logs:
   - `logs/cognitive_log.jsonl`
   - `logs/cognitive_log.md`

---

## 📁 Estrutura de Pastas (sugerida)

```text
.
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── bootstrap_runtime.py
├── agents/
│   ├── agente_orquestrador.py
│   ├── agente_pesquisador.py
│   ├── agente_educador.py
│   ├── agente_planejador.py
│   ├── agente_conteudo.py
│   └── agente_diagnostico.py
├── tools/
│   ├── tools_fundamentais.py
│   ├── tools_pesquisa.py
│   ├── tools_educacionais.py
│   ├── tools_planejamento_vida.py
│   ├── tools_criativas_conteudo.py
│   ├── tools_universais.py
│   └── tools_logs_cognitivos.py
├── logs/
│   ├── cognitive_log.jsonl
│   └── cognitive_log.md
├── .env
├── requirements.txt (ou pyproject.toml)
└── Dockerfile
```

> **Observação:** a pasta `logs/` é criada automaticamente se não existir.

---

## 🔐 Variáveis de Ambiente (`.env`)

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=...
TAVILY_API_KEY=...

# Opcional/recomendado
API_KEY=uma-chave-forte
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
MAX_INPUT_CHARS=3000

# Opcional
ENABLE_PESQUISADOR=1
```

### Regras

- `OPENAI_API_KEY` é **obrigatória**.
- `TAVILY_API_KEY` é **obrigatória** se `ENABLE_PESQUISADOR=1` e o pesquisador usa Tavily.
- `API_KEY` é recomendada para proteger a API em produção.

---

## 🚀 Como Rodar Local (sem Docker)

1) Instale dependências:

```bash
pip install -r requirements.txt
```

2) Suba a API:

```bash
uvicorn api.main:app --reload
```

3) Abra no navegador:

- `http://127.0.0.1:8000/docs` (Swagger)
- `http://127.0.0.1:8000/health`

---

## 🧪 Endpoints da API

### `GET /health`

Retorna status básico.

### `POST /route`

Roteia (decide agente), **não executa**.

**Body:**

```json
{ "pergunta": "Crie um roteiro para Instagram" }
```

**Resposta:**

```json
{
  "agente": "conteudo",
  "saida": null,
  "meta": { "modo": "llm-routing", "session_id": "..." }
}
```

### `POST /run`

Roteia e executa o agente, retornando `saida`.

**Body:**

```json
{ "pergunta": "Crie um roteiro para Instagram" }
```

**Resposta:**

```json
{
  "agente": "conteudo",
  "saida": "texto gerado...",
  "meta": { "execucao": "ok", "session_id": "..." }
}
```

---

## 🧾 Logs Cognitivos (Auditoria)

A tool `tools/tools_logs_cognitivos.py` registra:

- **JSONL**: `logs/cognitive_log.jsonl` (ideal para ingestão / análise / dashboards)
- **Markdown**: `logs/cognitive_log.md` (ideal para leitura humana)

Eventos típicos:

- `request_received`
- `routing_start`
- `routing_decision`
- `agent_start`
- `agent_end`
- `error`

---

## 🐳 Deploy com Docker (Opção B)

### 1) Garanta `uvicorn` nas dependências

No `requirements.txt`, inclua **no mínimo**:

```text
fastapi
uvicorn[standard]
python-dotenv
```

> Inclua também `agno`, `tavily` (ou dependências do `TavilyTools`) e quaisquer outras libs usadas no projeto.

### 2) Dockerfile (recomendado)

Use `python -m uvicorn` para evitar problemas de PATH:

```dockerfile
FROM python:3.13-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 3) Build

```bash
docker build -t agno-api .
```

### 4) Run (com `.env`)

```bash
docker run --rm -p 8000:8000 --env-file .env agno-api
```

### 5) Persistir logs (opcional)

No Windows PowerShell:

```bash
docker run --rm -p 8000:8000 --env-file .env -v "%cd%/logs:/app/logs" agno-api
```

---

## ✍️ Assinatura

Sagaz.Lab 864
