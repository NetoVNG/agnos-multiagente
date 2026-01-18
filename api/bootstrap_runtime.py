# api/bootstrap_runtime.py
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_env():
    try:
        from dotenv import load_dotenv
        load_dotenv(PROJECT_ROOT / ".env")
    except Exception:
        pass


def validate_keys():
    missing = []

    if not os.getenv("OPENAI_API_KEY"):
        missing.append("OPENAI_API_KEY")

    enable_pesquisador = os.getenv("ENABLE_PESQUISADOR", "1").strip().lower() in ("1", "true", "yes", "y")
    if enable_pesquisador and not os.getenv("TAVILY_API_KEY"):
        missing.append("TAVILY_API_KEY")

    # API_KEY é recomendado, mas pode ser opcional em dev
    # Se você quiser forçar, descomente:
    # if not os.getenv("API_KEY"):
    #     missing.append("API_KEY")

    if missing:
        raise RuntimeError(
            f"Missing environment variables: {', '.join(missing)}. "
            "Defina no .env ou nas variáveis de ambiente do servidor."
        )


def get_cors_origins() -> list[str]:
    raw = (os.getenv("CORS_ORIGINS") or "").strip()
    if not raw:
        return []
    return [o.strip() for o in raw.split(",") if o.strip()]


def get_max_input_chars() -> int:
    raw = (os.getenv("MAX_INPUT_CHARS") or "3000").strip()
    try:
        n = int(raw)
        return max(200, n)  # mínimo razoável
    except Exception:
        return 3000
