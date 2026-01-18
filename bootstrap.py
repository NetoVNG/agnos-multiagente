# bootstrap.py
import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

print("\n🔹 BOOTSTRAP DO PROJETO INICIADO\n")

# ======================================================
# 1. Garantir raiz do projeto
# ======================================================
PROJECT_ROOT = Path(__file__).resolve().parent
os.chdir(PROJECT_ROOT)

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

print(f"📁 Projeto raiz: {PROJECT_ROOT}")
print(f"🐍 Python ativo: {sys.executable}")

# ======================================================
# 2. Garantir virtualenv
# ======================================================
if "venv" not in sys.executable.lower():
    raise RuntimeError(
        "❌ Python não está rodando dentro do virtualenv (venv)"
    )

print("✅ Virtualenv detectado")

# ======================================================
# 3. Garantir uv instalado
# ======================================================
def ensure_uv():
    try:
        subprocess.run(
            ["uv", "--version"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("✅ uv já instalado")
    except Exception:
        print("📦 uv não encontrado. Instalando...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "uv"],
            check=True,
        )
        print("✅ uv instalado com sucesso")

ensure_uv()

# ======================================================
# 4. Sincronizar dependências (controlado por flag)
# ======================================================
pyproject = PROJECT_ROOT / "pyproject.toml"
uv_lock = PROJECT_ROOT / "uv.lock"

if not pyproject.exists():
    raise RuntimeError("❌ pyproject.toml não encontrado")

if not uv_lock.exists():
    raise RuntimeError("❌ uv.lock não encontrado")

if os.getenv("BOOTSTRAP_SYNC", "0") == "1":
    print("📦 BOOTSTRAP_SYNC=1 → Executando uv sync...")
    subprocess.run(
        ["uv", "sync"],
        check=True,
    )
    print("✅ Dependências sincronizadas")
else:
    print("⏭️ uv sync ignorado (BOOTSTRAP_SYNC=0)")

# ======================================================
# 5. Carregar .env
# ======================================================
env_path = PROJECT_ROOT / ".env"

if not env_path.exists():
    raise RuntimeError("❌ Arquivo .env não encontrado na raiz do projeto")

load_dotenv(env_path)

print("✅ .env carregado")

# ======================================================
# 6. Validar chaves obrigatórias
# ======================================================
REQUIRED_KEYS = [
    "OPENAI_API_KEY",
    "GROQ_API_KEY",
    "TAVILY_API_KEY",
]

print("\n🔐 Verificando variáveis de ambiente:\n")

for key in REQUIRED_KEYS:
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"❌ {key} NÃO está definida")
    print(f"✅ {key} OK")

print("\n🚀 BOOTSTRAP CONCLUÍDO COM SUCESSO")
print("Agora é seguro executar os agents.\n")
print("🔹 BOOTSTRAP DO PROJETO CONCLUÍDO\n")
