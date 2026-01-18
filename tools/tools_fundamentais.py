"""
CAMADA 1 — TOOLS FUNDAMENTAIS
Ferramentas utilitárias reutilizáveis para agentes Agno.

Princípios:
- Função única
- Sem estado
- Entrada e saída claras
- Reutilizável em qualquer agente
"""
"""
Para importação:
from tools.tools_fundamentais import *
E plugar direto:

agent = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[
        TavilyTools(),
        celsius_to_fahrenheit,
        validar_cpf,
        gerar_senha,
        gerar_uuid,
    ],
    debug_mode=True
)


"""
# =========================
# CONVERSORES
# =========================

def celsius_to_fahrenheit(temp_celsius: float) -> float:
    """
    Converte temperatura de Celsius para Fahrenheit.
    """
    return (temp_celsius * 9 / 5) + 32


def fahrenheit_to_celsius(temp_fahrenheit: float) -> float:
    """
    Converte temperatura de Fahrenheit para Celsius.
    """
    return (temp_fahrenheit - 32) * 5 / 9


# =========================
# VALIDADORES
# =========================

def validar_email(email: str) -> bool:
    """
    Valida formato básico de e-mail.
    """
    import re
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))


def validar_cpf(cpf: str) -> bool:
    """
    Valida CPF brasileiro.
    """
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf_parcial, peso):
        soma = sum(int(num) * p for num, p in zip(cpf_parcial, peso))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    d1 = calc_digito(cpf[:9], range(10, 1, -1))
    d2 = calc_digito(cpf[:10], range(11, 1, -1))

    return cpf[-2:] == d1 + d2


def validar_cnpj(cnpj: str) -> bool:
    """
    Valida CNPJ brasileiro.
    """
    cnpj = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj) != 14:
        return False

    def calc_digito(cnpj_parcial, pesos):
        soma = sum(int(a) * b for a, b in zip(cnpj_parcial, pesos))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    pesos2 = [6] + pesos1

    d1 = calc_digito(cnpj[:12], pesos1)
    d2 = calc_digito(cnpj[:13], pesos2)

    return cnpj[-2:] == d1 + d2


# =========================
# NORMALIZADORES DE TEXTO
# =========================

def limpar_texto(texto: str) -> str:
    """
    Remove caracteres especiais desnecessários.
    """
    import re
    texto = texto.strip()
    texto = re.sub(r'\s+', ' ', texto)
    return texto


def texto_para_json(texto: str) -> dict:
    """
    Converte texto simples em estrutura JSON básica.
    """
    linhas = texto.splitlines()
    return {"conteudo": [linha.strip() for linha in linhas if linha.strip()]}


def resumir_texto(texto: str, max_chars: int = 500) -> str:
    """
    Resume texto truncando por tamanho.
    """
    return texto[:max_chars] + "..." if len(texto) > max_chars else texto


# =========================
# GERADORES
# =========================

def gerar_senha(tamanho: int = 12) -> str:
    """
    Gera senha segura com letras, números e símbolos.
    """
    import secrets
    import string

    caracteres = string.ascii_letters + string.digits + "!@#$%&*?"
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))


def gerar_uuid() -> str:
    """
    Gera UUID v4.
    """
    import uuid
    return str(uuid.uuid4())


def gerar_hash(texto: str) -> str:
    """
    Gera hash SHA256 de um texto.
    """
    import hashlib
    return hashlib.sha256(texto.encode()).hexdigest()


def gerar_checklist(itens: list[str]) -> dict:
    """
    Gera checklist estruturado.
    """
    return {item: False for item in itens}


# =========================
# LEITURA E TRANSFORMAÇÃO
# =========================

def csv_para_json(conteudo_csv: str) -> list[dict]:
    """
    Converte CSV (texto) para JSON.
    """
    import csv
    from io import StringIO

    reader = csv.DictReader(StringIO(conteudo_csv))
    return list(reader)


def txt_para_estrutura(texto: str) -> dict:
    """
    Organiza TXT em blocos numerados.
    """
    linhas = [l.strip() for l in texto.splitlines() if l.strip()]
    return {f"item_{i+1}": linha for i, linha in enumerate(linhas)}


# Fim do arquivo tools_fundamentais.py

