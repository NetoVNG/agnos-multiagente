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

from tools.tools_pesquisa import sintese_estrategica
from tools.tools_planejamento_vida import registrar_aprendizado


def build_agent(debug: bool = False) -> Agent:
    return Agent(
        name="Agente de Diagnóstico",
        model=OpenAIChat(id="gpt-4.1-mini"),
        tools=[sintese_estrategica, registrar_aprendizado],
        instructions="""
        Você atua como agente de diagnóstico.
        Analise a situação, organize riscos e possibilidades,
        e proponha direções sem impor decisões.
        """,
        debug_mode=debug,
    )


def run_query(pergunta: str, debug: bool = False) -> str:
    agent = build_agent(debug=debug)
    out = agent.run(pergunta)
    content = getattr(out, "content", None)
    return content.strip() if content else ""


def main():
    pergunta = "Estou estudando, trabalhando muito e me sentindo sobrecarregado. Me ajude a analisar."
    print(run_query(pergunta, debug=True))


if __name__ == "__main__":
    main()
