# tools/tools_logs_cognitivos.py
from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def project_root() -> Path:
    # tools/ -> raiz
    return Path(__file__).resolve().parents[1]


def ensure_logs_dir() -> Path:
    logs_dir = project_root() / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    return logs_dir


def safe_truncate(text: str, max_len: int = 500) -> str:
    if text is None:
        return ""
    text = str(text)
    return text if len(text) <= max_len else text[:max_len] + "…"


def mask_secrets(value: str) -> str:
    # máscara simples para não vazar chaves caso alguém logue sem querer
    if not value:
        return value
    if len(value) <= 8:
        return "***"
    return value[:3] + "***" + value[-3:]


@dataclass
class CognitiveEvent:
    event_id: str
    timestamp_utc: str
    session_id: str
    event_type: str  # ex: "user_input", "routing_decision", "agent_start", "agent_end", "error"
    agent: str = ""  # ex: "router-cognitivo", "agente-planejador"
    action: str = ""  # ex: "route", "execute", "respond"
    input: str = ""
    output: str = ""
    metadata: Dict[str, Any] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["metadata"] = d["metadata"] or {}
        return d


class CognitiveLogger:
    """
    Logger persistente (JSONL + Markdown opcional).
    - JSONL: ideal para máquina / auditoria / ingestão futura
    - MD: trilha humana, útil para leitura rápida
    """

    def __init__(
        self,
        jsonl_path: Optional[Path] = None,
        md_path: Optional[Path] = None,
        write_markdown: bool = True,
    ):
        logs_dir = ensure_logs_dir()
        self.jsonl_path = jsonl_path or (logs_dir / "cognitive_log.jsonl")
        self.md_path = md_path or (logs_dir / "cognitive_log.md")
        self.write_markdown = write_markdown

    def new_session_id(self) -> str:
        return str(uuid.uuid4())

    def log(
        self,
        session_id: str,
        event_type: str,
        agent: str = "",
        action: str = "",
        input_text: str = "",
        output_text: str = "",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> str:
        event = CognitiveEvent(
            event_id=str(uuid.uuid4()),
            timestamp_utc=utc_now_iso(),
            session_id=session_id,
            event_type=event_type,
            agent=agent,
            action=action,
            input=safe_truncate(input_text, 2000),
            output=safe_truncate(output_text, 2000),
            metadata=metadata or {},
        )

        # JSONL (append)
        with open(self.jsonl_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")

        # Markdown (append) - opcional
        if self.write_markdown:
            self._append_markdown(event)

        return event.event_id

    def _append_markdown(self, event: CognitiveEvent) -> None:
        # trilha humana: curta, legível, sem poluição
        lines = []
        lines.append(f"\n---\n")
        lines.append(f"## {event.timestamp_utc} — {event.event_type}\n")
        lines.append(f"- **session_id:** `{event.session_id}`\n")
        if event.agent:
            lines.append(f"- **agent:** `{event.agent}`\n")
        if event.action:
            lines.append(f"- **action:** `{event.action}`\n")
        if event.input:
            lines.append(f"\n**input:**\n\n> {safe_truncate(event.input, 800)}\n")
        if event.output:
            lines.append(f"\n**output:**\n\n> {safe_truncate(event.output, 800)}\n")
        if event.metadata:
            # metadados em json compacto
            md_meta = json.dumps(event.metadata, ensure_ascii=False)
            lines.append(f"\n**metadata:** `{safe_truncate(md_meta, 800)}`\n")

        with open(self.md_path, "a", encoding="utf-8") as f:
            f.writelines(lines)
