# agents/agente_orquestrador.py
import sys
from pathlib import Path

from tools.tools_logs_cognitivos import CognitiveLogger

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

from agents.agente_pesquisador import run_query as pesquisador_run
from agents.agente_educador import run_query as educador_run
from agents.agente_planejador import run_query as planejador_run
from agents.agente_conteudo import run_query as conteudo_run
from agents.agente_diagnostico import run_query as diagnostico_run


AGENTES_VALIDOS = ["pesquisador", "educador", "planejador", "conteudo", "diagnostico"]


def executar_agente_query(nome: str, pergunta: str) -> str:
    """
    Executa o agente escolhido e retorna a resposta em texto.
    """
    if nome == "pesquisador":
        return pesquisador_run(pergunta)
    if nome == "educador":
        return educador_run(pergunta)
    if nome == "planejador":
        return planejador_run(pergunta)
    if nome == "conteudo":
        return conteudo_run(pergunta)
    return diagnostico_run(pergunta)


def decidir_agente_por_resposta(resposta: str) -> str:
    r = (resposta or "").strip().lower()
    return r if r in AGENTES_VALIDOS else "diagnostico"


def decidir_agente_llm(pergunta: str) -> str:
    """
    Usa LLM para decidir qual agente deve atuar.
    Se falhar, cai em heurística simples.
    """
    router = Agent(
        name="Router Cognitivo",
        model=OpenAIChat(id="gpt-4.1-mini"),
        instructions=f"""
Você é um roteador de intenção.
Analise a pergunta do usuário e escolha QUAL agente especializado deve atuar.

Responda APENAS com UMA palavra, exatamente uma destas:
{", ".join(AGENTES_VALIDOS)}

Não explique. Não justifique. Não escreva mais nada.
""",
        debug_mode=False,
    )

    try:
        out = router.run(pergunta)
        resposta = out.content if out and getattr(out, "content", None) else ""
        agente = decidir_agente_por_resposta(resposta)
        if agente != "diagnostico":
            return agente
    except Exception:
        pass

    # fallback heurístico (quando API falha ou resposta estranha)
    p = pergunta.lower()
    if any(k in p for k in ["pesquise", "pesquisar", "tendência", "fontes", "notícia", "artigo"]):
        return "pesquisador"
    if any(k in p for k in ["questão", "questoes", "prova", "simulado", "estudar", "aprender"]):
        return "educador"
    if any(k in p for k in ["planejar", "rotina", "semana", "12 semanas", "objetivo", "prioridade"]):
        return "planejador"
    if any(k in p for k in ["roteiro", "conteúdo", "instagram", "tiktok", "narrativa", "calendário"]):
        return "conteudo"
    return "diagnostico"


def main():
    logger = CognitiveLogger()

    print("\n🤖 ORQUESTRADOR DE AGENTES")
    print("-" * 30)
    print("Digite sua pergunta.")
    print("Para encerrar, digite: finalizar agente\n")

    while True:
        pergunta = input("📝 > ").strip()

        if not pergunta:
            print("⚠️ Pergunta vazia. Tente novamente.\n")
            continue

        low = pergunta.lower()
        if ("final" in low and "agente" in low) or low in ["sair", "exit", "quit"]:
            print("\n👋 Orquestrador finalizado com sucesso.\n")
            break

        agente = decidir_agente_llm(pergunta)
        print(f"\n🎯 Agente selecionado: {agente.upper()}\n")

        # ✅ CHAMADA CORRETA: retorna texto (serve para CLI e API)
        saida = executar_agente_query(agente, pergunta)

        print("📌 Resposta:\n")
        print(saida)

        # ✅ LOG COGNITIVO (ajuste o método conforme sua implementação)
        try:
            logger.log(
                agent=agente,
                input_text=pergunta,
                output_text=saida,
                meta={"modo": "cli"}
            )
        except Exception:
            # não deixa logging derrubar o fluxo
            pass

        print("\n🔁 Pode continuar perguntando ou digitar 'finalizar agente'.\n")


if __name__ == "__main__":
    main()
