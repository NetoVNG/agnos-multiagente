# scripts/ler_logs.py
import json
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "logs" / "cognitive_log.jsonl"


def main():
    if not LOG_PATH.exists():
        print("Nenhum log encontrado em:", LOG_PATH)
        return

    total = 0
    por_tipo = {}

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ev = json.loads(line)
            t = ev.get("event_type", "unknown")
            por_tipo[t] = por_tipo.get(t, 0) + 1

    print("\n📊 Resumo de logs cognitivos")
    print("Arquivo:", LOG_PATH)
    print("Total de eventos:", total)
    print("\nPor tipo:")
    for k in sorted(por_tipo.keys()):
        print(f"- {k}: {por_tipo[k]}")


if __name__ == "__main__":
    main()
