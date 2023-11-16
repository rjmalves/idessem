from idessem.dessem.modelos.termdat import CADUSIT, CADUNIDT, CADCONF, CADMIN
from idessem.dessem.termdat import Term
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.termdat import (
    MockCADCONF,
    MockCADMIN,
    MockCADUNIDT,
    MockCADUSIT,
    MockTerm,
)

ARQ_TESTE = "./tests/__init__.py"


def test_registro_cadusit_term():
    m: MagicMock = mock_open(read_data="".join(MockCADUSIT))
    r = CADUSIT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [12, "CUIABA G CC", 1, 1999, 4, 6, 0, 0, 3]
    assert r.codigo_usina == 12
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.nome_usina == "CUIABA G CC"
    r.nome_usina = -1
    assert r.nome_usina == -1
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.ano_operacao == 1999
    r.ano_operacao = 0
    assert r.ano_operacao == 0
    assert r.mes_operacao == 4
    r.mes_operacao = 0
    assert r.mes_operacao == 0
    assert r.dia_operacao == 6
    r.dia_operacao = 0
    assert r.dia_operacao == 0
    assert r.hora_operacao == 0
    r.hora_operacao = -1
    assert r.hora_operacao == -1
    assert r.meia_hora_operacao == 0
    r.meia_hora_operacao = -1
    assert r.meia_hora_operacao == -1
    assert r.numero_unidades == 3
    r.numero_unidades = -1
    assert r.numero_unidades == -1


def test_registro_cadunidt_operuh():
    m: MagicMock = mock_open(read_data="".join(MockCADUNIDT))
    r = CADUNIDT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        35,
        1,
        2022,
        4,
        30,
        0,
        0,
        250.0,
        180.0,
        168,
        0,
        None,
        None,
        70,
        90,
        None,
        None,
        1,
        None,
    ]
    assert r.codigo_usina == 35
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.ano_operacao == 2022
    r.ano_operacao = 0
    assert r.ano_operacao == 0
    assert r.mes_operacao == 4
    r.mes_operacao = 0
    assert r.mes_operacao == 0
    assert r.dia_operacao == 30
    r.dia_operacao = 0
    assert r.dia_operacao == 0
    assert r.hora_operacao == 0
    r.hora_operacao = -1
    assert r.hora_operacao == -1
    assert r.meia_hora_operacao == 0
    r.meia_hora_operacao = -1
    assert r.meia_hora_operacao == -1
    assert r.capacidade_geracao == 250
    r.capacidade_geracao = -1
    assert r.capacidade_geracao == -1
    assert r.geracao_minima == 180
    r.geracao_minima = -1
    assert r.geracao_minima == -1
    assert r.tempo_on == 168
    r.tempo_on = -1
    assert r.tempo_on == -1
    assert r.tempo_off == 0
    r.tempo_off = -1
    assert r.tempo_off == -1
    assert r.custo_acionamento_frio is None
    r.custo_acionamento_frio = -1
    assert r.custo_acionamento_frio == -1
    assert r.custo_acionamento_quente is None
    r.custo_acionamento_quente = -1
    assert r.custo_acionamento_quente == -1
    assert r.rampa_subida == 70
    r.rampa_subida = -1
    assert r.rampa_subida == -1
    assert r.rampa_descida == 90
    r.rampa_descida = -1
    assert r.rampa_descida == -1
    assert r.geracao_maxima_ou_minima is None
    r.geracao_maxima_ou_minima = -1
    assert r.geracao_maxima_ou_minima == -1
    assert r.numero_maximo_oscilacoes is None
    r.numero_maximo_oscilacoes = -1
    assert r.numero_maximo_oscilacoes == -1
    assert r.unidades_equivalentes == 1
    r.unidades_equivalentes = -1
    assert r.unidades_equivalentes == -1
    assert r.rampa_transicao is None
    r.rampa_transicao = -1
    assert r.rampa_transicao == -1


def test_registro_cadconf_term():
    m: MagicMock = mock_open(read_data="".join(MockCADCONF))
    r = CADCONF()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [35, 1, 2]
    assert r.codigo_usina == 35
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.codigo_unidade_equivalente == 1
    r.codigo_unidade_equivalente = -1
    assert r.codigo_unidade_equivalente == -1
    assert r.codigo_unidade == 2
    r.codigo_unidade = -1
    assert r.codigo_unidade == -1


def test_registro_cadmin_term():
    m: MagicMock = mock_open(read_data="".join(MockCADMIN))
    r = CADMIN()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [49, 1, 3]
    assert r.codigo_usina == 49
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.codigo_unidade_equivalente == 1
    r.codigo_unidade_equivalente = -1
    assert r.codigo_unidade_equivalente == -1
    assert r.numero_minimo_unidades == 3
    r.numero_minimo_unidades = -1
    assert r.numero_minimo_unidades == -1


def test_campos_nao_encontrados_term():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Term.read(".")
    assert d.cadusit() is None
    assert d.cadunidt() is None
    assert d.cadconf() is None
    assert d.cadmin() is None


def test_campos_encontrados_term():
    m: MagicMock = mock_open(read_data="".join(MockTerm))
    with patch("builtins.open", m):
        d = Term.read("./tests/mocks/arquivos/termdat.py")

    assert d.cadusit() is not None
    assert d.cadunidt() is not None
    assert d.cadconf() is not None
    assert d.cadmin() is not None


def test_eq_term():
    m: MagicMock = mock_open(read_data="".join(MockTerm))
    with patch("builtins.open", m):
        d1 = Term.read("./tests/mocks/arquivos/termdat.py")
        d2 = Term.read("./tests/mocks/arquivos/termdat.py")
        assert d1 == d2


def test_neq_term():
    m: MagicMock = mock_open(read_data="".join(MockTerm))
    with patch("builtins.open", m):
        d1 = Term.read("./tests/mocks/arquivos/termdat.py")
        d2 = Term.read("./tests/mocks/arquivos/termdat.py")
        d2.cadusit()[0].codigo_usina = 99
        assert d1 != d2


def test_leitura_escrita_term():
    m_leitura: MagicMock = mock_open(read_data="".join(MockTerm))
    with patch("builtins.open", m_leitura):
        d1 = Term.read("./tests/mocks/arquivos/termdat.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/termdat.py")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Term.read("./tests/mocks/arquivos/termdat.py")
        assert d1 == d2
