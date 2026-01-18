# api/schemas.py
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RouteRequest(BaseModel):
    pergunta: str = Field(..., min_length=1)


class RouteResponse(BaseModel):
    agente: str
    saida: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
