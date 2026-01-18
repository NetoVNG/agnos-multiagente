# main.py
from pathlib import Path
import sys
import bootstrap
from tools.tools_logs_cognitivos import CognitiveLogger

# ======================================================
# BOOTSTRAP DO SISTEMA (PRODUÇÃO)
# ======================================================
PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from dotenv import load_dotenv
    load_dotenv(PROJECT_ROOT / ".env")
except Exception as e:
    print("⚠️ Não foi possível carregar .env:", e)
# ======================================================

from agents.agente_orquestrador import main as orquestrador_main

logger = CognitiveLogger(write_markdown=True)
session_id = logger.new_session_id()

logger.log(
    session_id=session_id,
    event_type="session_start",
    agent="agente-orquestrador",
    action="start",
    metadata={"app": "sistema-multiagente"},
)

def main():
    print("\n🚀 SISTEMA MULTIAGENTE")
    print("=" * 40)
    print("1 - Iniciar Orquestrador Cognitivo")
    print("2 - Sair\n")
    

    while True:
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            orquestrador_main()
            break

        elif escolha == "2":
            print("\n👋 Sistema encerrado.\n")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
