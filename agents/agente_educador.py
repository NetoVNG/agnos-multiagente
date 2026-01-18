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

from tools.tools_educacionais import (
    gerar_questao_multipla_escolha,
    corrigir_simulado,
    avaliar_desempenho,
    sugerir_plano_estudo,
)


def build_agent(debug: bool = False) -> Agent:
    return Agent(
        name="Agente Educador",
        model=OpenAIChat(id="gpt-4.1-mini"),
        tools=[
            gerar_questao_multipla_escolha,
            corrigir_simulado,
            avaliar_desempenho,
            sugerir_plano_estudo,
        ],
        instructions="""
        Você atua como educador analítico.
        Crie questões, explique respostas, avalie desempenho
        e sugira planos de estudo com objetividade.
        """,
        debug_mode=debug,
    )


def run_query(pergunta: str, debug: bool = False) -> str:
    agent = build_agent(debug=debug)
    out = agent.run(pergunta)
    content = getattr(out, "content", None)
    return content.strip() if content else ""


def main():
    pergunta = "Crie uma questão sobre estruturas condicionais em Python e explique a resposta."
    print(run_query(pergunta, debug=True))


if __name__ == "__main__":
    main()
