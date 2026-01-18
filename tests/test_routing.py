import pytest

from agents.agente_orquestrador import decidir_agente_por_resposta


def test_routing_respostas_validas():
    assert decidir_agente_por_resposta("pesquisador") == "pesquisador"
    assert decidir_agente_por_resposta("educador") == "educador"
    assert decidir_agente_por_resposta("planejador") == "planejador"
    assert decidir_agente_por_resposta("conteudo") == "conteudo"


def test_routing_resposta_invalida():
    assert decidir_agente_por_resposta("qualquer coisa") == "diagnostico"
    assert decidir_agente_por_resposta("") == "diagnostico"
    assert decidir_agente_por_resposta("PESQUISA") == "diagnostico"

import pytest
from agents.agente_orquestrador import decidir_agente_llm


@pytest.mark.integration
def test_routing_com_llm_real():
    agente = decidir_agente_llm("Pesquise tendências de IA na educação")
    assert agente == "pesquisador"
