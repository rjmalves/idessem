from idessem.dessem.modelos.operuh import REST, ELEM, LIM, VAR
from idessem.dessem.operuh import Operuh
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.operuh import (
    MockREST,
    MockLIM,
    MockELEM,
    MockVAR,
    MockOperuh,
)

ARQ_TESTE = "./tests/__init__.py"


def test_registro_rest_operuh():
    m: MagicMock = mock_open(read_data="".join(MockREST))
    r = REST()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [970, "V", "P", "RHQ", 489]
    assert r.codigo_restricao == 970
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.tipo == "V"
    r.tipo = "X"
    assert r.tipo == "X"
    assert r.intervalo_aplicacao == "P"
    r.intervalo_aplicacao = "X"
    assert r.intervalo_aplicacao == "X"
    assert r.justificativa == "RHQ"
    r.justificativa = "X"
    assert r.justificativa == "X"
    assert r.valor_inicial == 489
    r.valor_inicial = -1
    assert r.valor_inicial == -1


def test_registro_lim_operuh():
    m: MagicMock = mock_open(read_data="".join(MockLIM))
    r = LIM()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [66, ["I", None, None], ["F", None, None], None, 600]
    assert r.codigo_restricao == 66
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == "I"
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.limite_inferior is None
    r.limite_inferior = -1
    assert r.limite_inferior == -1
    assert r.limite_superior == 600
    r.limite_superior = -1
    assert r.limite_superior == -1


def test_registro_var_operuh():
    m: MagicMock = mock_open(read_data="".join(MockVAR))
    r = VAR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        970,
        ["I", None, None],
        ["F", None, None],
        None,
        None,
        None,
        550,
    ]
    assert r.codigo_restricao == 970
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == "I"
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.rampa_maxima_decrescimo_percentual is None
    r.rampa_maxima_decrescimo_percentual = -1
    assert r.rampa_maxima_decrescimo_percentual == -1
    assert r.rampa_maxima_acrescimo_percentual is None
    r.rampa_maxima_acrescimo_percentual = -1
    assert r.rampa_maxima_acrescimo_percentual == -1
    assert r.rampa_maxima_decrescimo_absoluta is None
    r.rampa_maxima_decrescimo_absoluta = -1
    assert r.rampa_maxima_decrescimo_absoluta == -1
    assert r.rampa_maxima_acrescimo_absoluta == 550
    r.rampa_maxima_acrescimo_absoluta = -1
    assert r.rampa_maxima_acrescimo_absoluta == -1


def test_registro_elem_operuh():
    m: MagicMock = mock_open(read_data="".join(MockELEM))
    r = ELEM()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [970, 228, "COLIDER", 3, 1.0]
    assert r.codigo_restricao == 970
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.codigo_usina == 228
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.nome_usina == "COLIDER"
    r.nome_usina = "X"
    assert r.nome_usina == "X"
    assert r.tipo == 3
    r.tipo = -1
    assert r.tipo == -1
    assert r.coeficiente == 1
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_campos_nao_encontrados_operuh():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Operuh.read(".")
    assert d.rest() is None
    assert d.elem() is None
    assert d.lim() is None
    assert d.var() is None


def test_campos_encontrados_operuh():
    m: MagicMock = mock_open(read_data="".join(MockOperuh))
    with patch("builtins.open", m):
        d = Operuh.read("./tests/mocks/arquivos/operuh.py")

    assert d.rest() is not None
    assert d.elem() is not None
    assert d.lim() is not None
    assert d.var() is not None


def test_eq_operuh():
    m: MagicMock = mock_open(read_data="".join(MockOperuh))
    with patch("builtins.open", m):
        d1 = Operuh.read("./tests/mocks/arquivos/operuh.py")
        d2 = Operuh.read("./tests/mocks/arquivos/operuh.py")
        assert d1 == d2


def test_neq_operuh():
    m: MagicMock = mock_open(read_data="".join(MockOperuh))
    with patch("builtins.open", m):
        d1 = Operuh.read("./tests/mocks/arquivos/operuh.py")
        d2 = Operuh.read("./tests/mocks/arquivos/operuh.py")
        d2.rest()[0].codigo_restricao = 6
        assert d1 != d2


def test_leitura_escrita_operuh():
    m_leitura: MagicMock = mock_open(read_data="".join(MockOperuh))
    with patch("builtins.open", m_leitura):
        d1 = Operuh.read("./tests/mocks/arquivos/operuh.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/operuh.py")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Operuh.read("./tests/mocks/arquivos/operuh.py")
        assert d1 == d2
