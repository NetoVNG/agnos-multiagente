import sys
from pathlib import Path

if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    try:
        from dotenv import load_dotenv
        load_dotenv(PROJECT_ROOT / ".env")
    except Exception as e:
        print("⚠️ Não foi possível carregar .env:", e)

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from tools.tools_criativas_conteudo import (
    gerar_roteiro_curto,
    criar_narrativa_seriada,
    organizar_calendario_conteudo,
)


def build_agent(debug: bool = False) -> Agent:
    return Agent(
        name="Agente de Conteúdo",
        model=OpenAIChat(id="gpt-4.1-mini"),
        tools=[gerar_roteiro_curto, criar_narrativa_seriada, organizar_calendario_conteudo],
        instructions="""
        Você atua como arquiteto de conteúdo textual.
        Transforme ideias em roteiros, séries e calendários coerentes.
        """,
        debug_mode=debug,
    )


def run_query(pergunta: str, debug: bool = False) -> str:
    agent = build_agent(debug=debug)
    out = agent.run(pergunta)
    content = getattr(out, "content", None)
    return content.strip() if content else ""


def main():
    pergunta = "Crie uma ideia de narrativa seriada sobre aprendizado em programação."
    print(run_query(pergunta, debug=True))


if __name__ == "__main__":
    main()
