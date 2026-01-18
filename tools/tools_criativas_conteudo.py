"""
CAMADA 5 — TOOLS CRIATIVAS & CONTEÚDO (TEXTO)

Ferramentas para:
- criação de roteiros textuais
- narrativas seriadas
- personagens e vozes narrativas
- sequenciamento de ideias
- organização de calendários editoriais

Sem dependência de mídia.
Somente texto, estrutura e intenção.
"""

from typing import List, Dict, Any


# =========================
# ROTEIROS CURTOS (TEXTO)
# =========================

def gerar_roteiro_curto(
    tema: str,
    objetivo: str,
    duracao: str = "15s"
) -> Dict[str, Any]:
    """
    Gera roteiro textual curto.
    """
    return {
        "tema": tema,
        "duracao": duracao,
        "estrutura": [
            "gancho inicial",
            "ideia central",
            "fechamento"
        ],
        "objetivo": objetivo
    }


# =========================
# NARRATIVAS SERIADAS
# =========================

def criar_narrativa_seriada(
    tema: str,
    episodios: int,
    fio_condutor: str
) -> Dict[str, Any]:
    """
    Cria estrutura de narrativa em episódios.
    """
    return {
        "tema": tema,
        "episodios": [
            {
                "episodio": i + 1,
                "foco": f"{fio_condutor} — parte {i + 1}"
            }
            for i in range(episodios)
        ],
        "fio_condutor": fio_condutor
    }


# =========================
# SEQUÊNCIA DE MICROCONTEÚDOS
# =========================

def sequenciar_microconteudos(
    ideia_central: str,
    desdobramentos: List[str]
) -> Dict[str, Any]:
    """
    Quebra uma ideia central em microconteúdos.
    """
    return {
        "ideia_central": ideia_central,
        "microconteudos": [
            {
                "ordem": i + 1,
                "foco": item
            }
            for i, item in enumerate(desdobramentos)
        ]
    }


# =========================
# PERSONAGENS & VOZ NARRATIVA
# =========================

def criar_personagem_narrativo(
    nome: str,
    personalidade: str,
    tom_de_voz: str,
    valores: List[str]
) -> Dict[str, Any]:
    """
    Define personagem narrativo textual.
    """
    return {
        "nome": nome,
        "personalidade": personalidade,
        "tom_de_voz": tom_de_voz,
        "valores": valores,
        "estilo_narrativo": "consistente e reconhecível"
    }


def definir_voz_narrativa(
    tom: str,
    nivel_tecnico: str,
    ritmo: str
) -> Dict[str, str]:
    """
    Define parâmetros da voz narrativa.
    """
    return {
        "tom": tom,
        "nivel_tecnico": nivel_tecnico,
        "ritmo": ritmo
    }


# =========================
# ANÁLISE TEXTUAL DE CONTEÚDO
# =========================

def analisar_retenção_textual(
    texto: str
) -> Dict[str, Any]:
    """
    Avalia potencial de retenção baseado em estrutura textual.
    """
    tamanho = len(texto)

    return {
        "tamanho_caracteres": tamanho,
        "estrutura_detectada": (
            "curta" if tamanho < 300
            else "média" if tamanho < 800
            else "longa"
        ),
        "potencial_retenção": (
            "alto" if tamanho < 500
            else "médio" if tamanho < 1000
            else "baixo"
        )
    }


# =========================
# CALENDÁRIO DE CONTEÚDO
# =========================

def organizar_calendario_conteudo(
    temas: List[str],
    frequencia: str = "semanal"
) -> Dict[str, Any]:
    """
    Organiza calendário editorial textual.
    """
    return {
        "frequencia": frequencia,
        "planejamento": [
            {
                "ordem": i + 1,
                "tema": tema
            }
            for i, tema in enumerate(temas)
        ]
    }
# Fim do arquivo tools/tools_criativas_conteudo.py