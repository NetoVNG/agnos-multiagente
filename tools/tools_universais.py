"""
CAMADA UNIVERSAL — TOOLS TRANSVERSAIS

Ferramentas genéricas, amplamente utilizadas em sistemas digitais,
produtos SaaS, automações e agentes inteligentes.

Princípios:
- Independentes de domínio
- Reutilizáveis em qualquer agente
- Sem estado
- Entrada e saída explícitas
- Evolução por adição, não por refatoração
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import re
import math


# ======================================================
# TEMPO & DATAS (USO UNIVERSAL)
# ======================================================

def agora_iso() -> str:
    """
    Retorna o timestamp atual em ISO 8601.
    """
    return datetime.utcnow().isoformat()


def diferenca_dias(data_inicio: str, data_fim: str) -> int:
    """
    Calcula diferença em dias entre duas datas ISO.
    """
    d1 = datetime.fromisoformat(data_inicio)
    d2 = datetime.fromisoformat(data_fim)
    return abs((d2 - d1).days)


def janela_tempo(dias: int) -> Dict[str, str]:
    """
    Retorna janela temporal (hoje - N dias).
    """
    fim = datetime.utcnow()
    inicio = fim - timedelta(days=dias)
    return {
        "inicio": inicio.isoformat(),
        "fim": fim.isoformat()
    }


# ======================================================
# SANITIZAÇÃO & NORMALIZAÇÃO DE ENTRADA
# ======================================================

def limitar_tamanho(texto: str, max_chars: int = 1000) -> str:
    """
    Limita tamanho de texto.
    """
    return texto[:max_chars]


def remover_html(texto: str) -> str:
    """
    Remove tags HTML simples.
    """
    return re.sub(r"<[^>]*>", "", texto)


def normalizar_whitespace(texto: str) -> str:
    """
    Normaliza espaços em branco.
    """
    return re.sub(r"\s+", " ", texto).strip()


def mascarar_email(email: str) -> str:
    """
    Mascara e-mail para exibição segura.
    """
    try:
        usuario, dominio = email.split("@")
        return usuario[0] + "***@" + dominio
    except ValueError:
        return "***"


# ======================================================
# ESTRUTURAÇÃO & SERIALIZAÇÃO LEVE
# ======================================================

def dict_para_markdown(dados: Dict[str, Any]) -> str:
    """
    Converte dict simples para Markdown.
    """
    linhas = []
    for chave, valor in dados.items():
        linhas.append(f"- **{chave}**: {valor}")
    return "\n".join(linhas)


def lista_para_tabela(lista: List[Any]) -> List[Dict[str, Any]]:
    """
    Transforma lista simples em estrutura tabular.
    """
    return [{"index": i + 1, "valor": v} for i, v in enumerate(lista)]


# ======================================================
# SCORING & AVALIAÇÃO GENÉRICA
# ======================================================

def calcular_score(valor: float, maximo: float) -> float:
    """
    Retorna score percentual (0–100).
    """
    if maximo == 0:
        return 0.0
    return round((valor / maximo) * 100, 2)


def classificar_faixa(score: float) -> str:
    """
    Classifica score em faixa qualitativa.
    """
    if score >= 85:
        return "alto"
    if score >= 60:
        return "médio"
    return "baixo"


def rankear_itens(valores: Dict[str, float]) -> List[Dict[str, Any]]:
    """
    Rank simples de itens por valor.
    """
    ordenado = sorted(valores.items(), key=lambda x: x[1], reverse=True)
    return [
        {"posicao": i + 1, "item": k, "valor": v}
        for i, (k, v) in enumerate(ordenado)
    ]


# ======================================================
# DETECÇÃO TEXTUAL LEVE
# ======================================================

def eh_pergunta(texto: str) -> bool:
    """
    Detecta se texto é uma pergunta.
    """
    return texto.strip().endswith("?")


def contar_ocorrencias(texto: str, termo: str) -> int:
    """
    Conta ocorrências de um termo no texto.
    """
    return texto.lower().count(termo.lower())


def detectar_lista(texto: str) -> bool:
    """
    Detecta estrutura de lista simples.
    """
    linhas = texto.splitlines()
    return any(l.strip().startswith(("-", "*", "•")) for l in linhas)


# ======================================================
# EXPORTAÇÃO TEXTUAL BÁSICA
# ======================================================

def gerar_resumo_executivo(
    titulo: str,
    pontos: List[str]
) -> Dict[str, Any]:
    """
    Gera estrutura de resumo executivo.
    """
    return {
        "titulo": titulo,
        "resumo": pontos,
        "gerado_em": agora_iso()
    }


# ======================================================
# LOGGING LÓGICO (HUMANO)
# ======================================================

def registrar_evento(
    acao: str,
    resultado: str,
    observacao: str = ""
) -> Dict[str, Any]:
    """
    Registra evento lógico/humano.
    """
    return {
        "acao": acao,
        "resultado": resultado,
        "observacao": observacao,
        "timestamp": agora_iso()
    }


# Fim do arquivo tools_universais.py
