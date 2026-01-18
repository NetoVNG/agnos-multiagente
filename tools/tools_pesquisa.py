"""
CAMADA 2 — TOOLS DE PESQUISA & INTELIGÊNCIA

Funções para:
- pesquisa estruturada
- comparação de fontes
- mapeamento de tendências
- síntese estratégica

Essas tools produzem INSUMOS para agentes.
"""

from typing import List, Dict, Any


# =========================
# PESQUISA ESTRUTURADA
# =========================

def organizar_pesquisa(
    pergunta: str,
    respostas: List[str],
    fontes: List[str]
) -> Dict[str, Any]:
    """
    Organiza resultados de pesquisa em formato estruturado.
    """
    return {
        "pergunta": pergunta,
        "resumo_executivo": respostas[:3],
        "fontes": fontes,
        "quantidade_fontes": len(fontes)
    }


def resumo_executivo(textos: List[str], limite: int = 3) -> List[str]:
    """
    Extrai os principais pontos de uma lista de textos.
    """
    return [texto[:300] + "..." if len(texto) > 300 else texto for texto in textos[:limite]]


# =========================
# COMPARAÇÃO DE FONTES
# =========================

def comparar_fontes(fontes: Dict[str, str]) -> Dict[str, Any]:
    """
    Compara fontes e identifica convergências e divergências.

    Args:
        fontes: {"fonte_a": texto, "fonte_b": texto}

    Returns:
        Estrutura comparativa
    """
    textos = list(fontes.values())

    convergencias = set(textos[0].split()) & set(textos[1].split())
    divergencias = set(textos[0].split()) ^ set(textos[1].split())

    return {
        "fontes_analisadas": list(fontes.keys()),
        "convergencias_aproximadas": list(convergencias)[:20],
        "divergencias_aproximadas": list(divergencias)[:20]
    }


def avaliar_confiabilidade(
    fonte: str,
    dominio: str,
    citacoes: int = 0
) -> Dict[str, Any]:
    """
    Avaliação heurística simples de confiabilidade de fonte.
    """
    score = 0

    if dominio.endswith(".gov") or dominio.endswith(".edu"):
        score += 2
    if citacoes > 5:
        score += 1
    if citacoes > 20:
        score += 2

    nivel = "baixa"
    if score >= 3:
        nivel = "média"
    if score >= 5:
        nivel = "alta"

    return {
        "fonte": fonte,
        "dominio": dominio,
        "citacoes": citacoes,
        "score": score,
        "confiabilidade": nivel
    }


# =========================
# MAPEAMENTO DE TENDÊNCIAS
# =========================

def mapear_tendencias(
    tema: str,
    sinais: List[str]
) -> Dict[str, Any]:
    """
    Organiza sinais de tendência sobre um tema.
    """
    return {
        "tema": tema,
        "sinais_identificados": sinais,
        "volume_sinais": len(sinais),
        "indicativo": (
            "tendência forte" if len(sinais) >= 5
            else "tendência emergente" if len(sinais) >= 3
            else "sinal fraco"
        )
    }


# =========================
# SÍNTESE ESTRATÉGICA
# =========================

def sintese_estrategica(
    pontos_chave: List[str],
    riscos: List[str],
    oportunidades: List[str]
) -> Dict[str, Any]:
    """
    Gera síntese estratégica estruturada.
    """
    return {
        "pontos_chave": pontos_chave,
        "riscos": riscos,
        "oportunidades": oportunidades,
        "direcao_sugerida": (
            "avançar com cautela" if riscos and oportunidades
            else "explorar agressivamente" if oportunidades
            else "reavaliar estratégia"
        )
    }

# Fim do arquivo tools_pesquisa.py
