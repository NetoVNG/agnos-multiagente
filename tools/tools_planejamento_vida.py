"""
CAMADA 4 — TOOLS DE PLANEJAMENTO & VIDA

Ferramentas para:
- alinhamento de valores
- definição de objetivos
- planejamento em ciclos
- planejamento semanal
- revisão de rota
- registro de aprendizados

Essas tools ajudam pessoas a se orientarem no tempo.
"""

from typing import List, Dict, Any
from datetime import date, timedelta


# =========================
# ALINHAMENTO DE VALORES
# =========================

def alinhar_valores(
    valores: List[str],
    objetivos: List[str]
) -> Dict[str, Any]:
    """
    Verifica alinhamento entre valores e objetivos.
    """
    alinhados = [obj for obj in objetivos if any(v.lower() in obj.lower() for v in valores)]
    desalinhados = [obj for obj in objetivos if obj not in alinhados]

    return {
        "valores": valores,
        "objetivos": objetivos,
        "objetivos_alinhados": alinhados,
        "objetivos_desalinhados": desalinhados
    }


# =========================
# DEFINIÇÃO DE OBJETIVOS
# =========================

def definir_objetivos(
    curto_prazo: List[str],
    medio_prazo: List[str]
) -> Dict[str, Any]:
    """
    Organiza objetivos por horizonte temporal.
    """
    return {
        "curto_prazo": curto_prazo,
        "medio_prazo": medio_prazo,
        "total_objetivos": len(curto_prazo) + len(medio_prazo)
    }


# =========================
# PLANEJAMENTO EM CICLOS
# =========================

def planejar_ciclo(
    objetivo_central: str,
    duracao_semanas: int = 12
) -> Dict[str, Any]:
    """
    Cria um ciclo de planejamento (ex: 12 semanas).
    """
    hoje = date.today()
    fim = hoje + timedelta(weeks=duracao_semanas)

    return {
        "objetivo_central": objetivo_central,
        "inicio": hoje.isoformat(),
        "fim": fim.isoformat(),
        "duracao_semanas": duracao_semanas
    }


# =========================
# PLANEJAMENTO SEMANAL
# =========================

def planejar_semana(
    foco_principal: str,
    tarefas: List[str]
) -> Dict[str, Any]:
    """
    Organiza foco e tarefas da semana.
    """
    return {
        "foco_principal": foco_principal,
        "tarefas_semana": tarefas,
        "quantidade_tarefas": len(tarefas)
    }


# =========================
# REVISÃO E AJUSTE DE ROTA
# =========================

def revisar_rota(
    objetivos: List[str],
    realizados: List[str],
    aprendizados: List[str]
) -> Dict[str, Any]:
    """
    Avalia progresso e sugere ajustes.
    """
    pendentes = [obj for obj in objetivos if obj not in realizados]

    return {
        "objetivos_planejados": objetivos,
        "objetivos_realizados": realizados,
        "objetivos_pendentes": pendentes,
        "aprendizados": aprendizados,
        "ajuste_sugerido": (
            "reduzir escopo" if len(pendentes) > len(realizados)
            else "manter estratégia"
        )
    }


# =========================
# CHECKLIST DE EXECUÇÃO
# =========================

def checklist_execucao(tarefas: List[str]) -> Dict[str, bool]:
    """
    Gera checklist simples de execução.
    """
    return {tarefa: False for tarefa in tarefas}


# =========================
# REGISTRO DE APRENDIZADOS
# =========================

def registrar_aprendizado(
    contexto: str,
    aprendizado: str,
    proxima_acao: str
) -> Dict[str, Any]:
    """
    Registra aprendizado acionável.
    """
    return {
        "contexto": contexto,
        "aprendizado": aprendizado,
        "proxima_acao": proxima_acao,
        "data": date.today().isoformat()
    }
    
    
# Fim do tools_planejamento_vida.py
