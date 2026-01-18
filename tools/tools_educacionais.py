"""
CAMADA 3 — TOOLS EDUCACIONAIS

Ferramentas para:
- geração de questões
- explicação pedagógica
- simulação de provas
- avaliação de desempenho
- plano de estudo sugerido

Essas tools NÃO ensinam sozinhas.
Elas estruturam o ensino para agentes educadores.
"""

from typing import List, Dict, Any
import random
import time


# =========================
# GERAÇÃO DE QUESTÕES
# =========================

def gerar_questao_multipla_escolha(
    tema: str,
    pergunta: str,
    alternativas: List[str],
    correta: int
) -> Dict[str, Any]:
    """
    Cria uma questão objetiva estruturada.
    """
    return {
        "tema": tema,
        "tipo": "multipla_escolha",
        "pergunta": pergunta,
        "alternativas": alternativas,
        "resposta_correta": correta
    }


def gerar_questao_discursiva(
    tema: str,
    pergunta: str,
    criterios_avaliacao: List[str]
) -> Dict[str, Any]:
    """
    Cria questão discursiva com critérios claros.
    """
    return {
        "tema": tema,
        "tipo": "discursiva",
        "pergunta": pergunta,
        "criterios": criterios_avaliacao
    }


# =========================
# EXPLICAÇÃO DE QUESTÕES
# =========================

def explicar_questao(
    pergunta: str,
    resposta_correta: str,
    erros_comuns: List[str],
    atalho_raciocinio: str
) -> Dict[str, Any]:
    """
    Estrutura explicação pedagógica.
    """
    return {
        "pergunta": pergunta,
        "explicacao_passo_a_passo": resposta_correta,
        "erros_comuns": erros_comuns,
        "atalho_de_raciocinio": atalho_raciocinio
    }


# =========================
# SIMULAÇÃO DE PROVAS
# =========================

def iniciar_simulado(
    questoes: List[Dict[str, Any]],
    tempo_maximo_minutos: int
) -> Dict[str, Any]:
    """
    Inicia simulado com controle de tempo.
    """
    inicio = time.time()
    return {
        "questoes": questoes,
        "tempo_maximo_minutos": tempo_maximo_minutos,
        "inicio_timestamp": inicio
    }


def corrigir_simulado(
    simulado: Dict[str, Any],
    respostas_usuario: List[int]
) -> Dict[str, Any]:
    """
    Corrige simulado objetivo.
    """
    questoes = simulado["questoes"]
    acertos = 0

    for q, r in zip(questoes, respostas_usuario):
        if q.get("resposta_correta") == r:
            acertos += 1

    total = len(questoes)
    percentual = round((acertos / total) * 100, 2)

    return {
        "total_questoes": total,
        "acertos": acertos,
        "erros": total - acertos,
        "percentual": percentual
    }


# =========================
# AVALIAÇÃO DE DESEMPENHO
# =========================

def avaliar_desempenho(
    historico: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Avalia desempenho com base em histórico de simulados.
    """
    medias = [h["percentual"] for h in historico]

    media_geral = round(sum(medias) / len(medias), 2) if medias else 0

    nivel = "iniciante"
    if media_geral >= 70:
        nivel = "intermediário"
    if media_geral >= 85:
        nivel = "avançado"

    return {
        "media_geral": media_geral,
        "nivel": nivel,
        "quantidade_simulados": len(historico)
    }


# =========================
# PLANO DE ESTUDO SUGERIDO
# =========================

def sugerir_plano_estudo(
    pontos_fortes: List[str],
    pontos_fracos: List[str],
    horas_semanais: int
) -> Dict[str, Any]:
    """
    Gera plano de estudo adaptativo simples.
    """
    foco = pontos_fracos if pontos_fracos else pontos_fortes

    horas_por_tema = round(horas_semanais / len(foco), 2) if foco else 0

    return {
        "horas_semanais": horas_semanais,
        "foco_principal": foco,
        "distribuicao_horas": {
            tema: horas_por_tema for tema in foco
        },
        "recomendacao": (
            "priorizar revisão e exercícios"
            if pontos_fracos
            else "manter ritmo e aprofundar"
        )
    }
# Fim do arquivo tools_educacionais.py
