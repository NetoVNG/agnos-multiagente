import sys
from pathlib import Path

# ======================================================
# MODO DEV – execução direta
# ======================================================
if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))

    try:
        from dotenv import load_dotenv
        load_dotenv(PROJECT_ROOT / ".env")
    except Exception as e:
        print("⚠️ Não foi possível carregar .env:", e)
# ======================================================

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

from tools.tools_pesquisa import (
    organizar_pesquisa,
    resumo_executivo,
    sintese_estrategica,
)


def build_agent(debug: bool = False) -> Agent:
    return Agent(
        name="Agente Pesquisador",
        model=OpenAIChat(id="gpt-4.1-mini"),
        tools=[
            TavilyTools(),
            organizar_pesquisa,
            resumo_executivo,
            sintese_estrategica,
        ],
        instructions="""
        Você atua como pesquisador estratégico.
        Organize informações, identifique padrões
        e produza sínteses claras e acionáveis.
        """,
        debug_mode=debug,
    )


def run_query(pergunta: str, debug: bool = False) -> str:
    agent = build_agent(debug=debug)
    out = agent.run(pergunta)
    content = getattr(out, "content", None)
    return content.strip() if content else ""


def main():
    pergunta = "Pesquise as principais tendências de IA na educação em 2024."
    print(run_query(pergunta, debug=True))


if __name__ == "__main__":
    main()
