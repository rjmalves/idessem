from idessem.dessem.modelos.respot import (
    RP,
    LM
)
from idessem.dessem.respot import Respot
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.respot import (
    MockRP,
    MockLM,
    MockRespot
)

ARQ_TESTE = "./tests/__init__.py"


def test_registro_rp_respot():
    m: MagicMock = mock_open(read_data="".join(MockRP))
    r = RP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        1,
        [11,
        0,
        0,],
        ["F",
        None,
        None,],
        "5% CARGA DO SIN NO CAG SECO"
    ]

    assert r.codigo_area == 1
    r.codigo_area = -1
    assert r.codigo_area == -1
    assert r.dia_inicial == 11
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial == 0
    r.hora_inicial = 1
    assert r.hora_inicial == 1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = 1
    assert r.meia_hora_inicial == 1
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 0
    assert r.hora_final == 0
    assert r.meia_hora_final is None
    r.meia_hora_final = 0
    assert r.meia_hora_final == 0
    assert r.descricao =="5% CARGA DO SIN NO CAG SECO"
    r.descricao = "X"
    assert r.descricao == "X"
    

def test_registro_lm_respot():
    m: MagicMock = mock_open(read_data="".join(MockLM))
    r = LM()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        1,
        [11,
        0,
        0,],
        ["F",
        None,
        None,],3285
    ]

    assert r.codigo_area == 1
    r.codigo_area = -1
    assert r.codigo_area == -1
    assert r.dia_inicial == 11
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial == 0
    r.hora_inicial = 1
    assert r.hora_inicial == 1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = 1
    assert r.meia_hora_inicial == 1
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 0
    assert r.hora_final == 0
    assert r.meia_hora_final is None
    r.meia_hora_final = 0
    assert r.meia_hora_final == 0
    assert r.limite_inferior ==3285.0
    r.limite_inferior = 0
    assert r.limite_inferior == 0

def test_campos_nao_encontrados_respot():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Respot.read(".")
    assert d.rp(1) is None
    assert d.lm(1) is None
   

def test_campos_encontrados_respot():
    m: MagicMock = mock_open(read_data="".join(MockRespot))
    with patch("builtins.open", m):
        d = Respot.read("./tests/mocks/arquivos/respot.py")

    assert d.rp(1) is not None
    assert d.lm(1) is not None


def test_eq_respot():
    m: MagicMock = mock_open(read_data="".join(MockRespot))
    with patch("builtins.open", m):
        d1 = Respot.read("./tests/mocks/arquivos/respot.py")
        d2 = Respot.read("./tests/mocks/arquivos/respot.py")
        assert d1 == d2


def test_neq_respot():
    m: MagicMock = mock_open(read_data="".join(MockRespot))
    with patch("builtins.open", m):
        d1 = Respot.read("./tests/mocks/arquivos/respot.py")
        d2 = Respot.read("./tests/mocks/arquivos/respot.py")
        d2.rp(1).dia_inicial = 5
        assert d1 != d2


def test_leitura_escrita_respot():
    m_leitura: MagicMock = mock_open(read_data="".join(MockRespot))
    with patch("builtins.open", m_leitura):
        d1 = Respot.read("./tests/mocks/arquivos/respot.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/respot.py")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Respot.read("./tests/mocks/arquivos/respot.py")
        assert d1 == d2
