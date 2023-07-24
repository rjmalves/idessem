from idessem.dessem.avl_estatfpha import AvlEstatFpha
from idessem.dessem.modelos.avl_estatfpha import (
    BlocoDesvios,
)
from datetime import datetime, timedelta
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.avl_estatfpha import (
    MockAvlEstatFpha,
    MockBlocoDesvios,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_avl_estatfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlEstatFpha))
    with patch("builtins.open", m):
        avl = AvlEstatFpha.read(ARQ_TESTE)
        assert avl.versao is not None
        assert avl.data_estudo is not None
        assert avl.estatisticas_desvios is not None


def test_atributos_naoencontrados_avl_estatfpha():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        avl = AvlEstatFpha.read(ARQ_TESTE)
        assert avl.versao is None
        assert avl.data_estudo is None
        assert avl.estatisticas_desvios is None


def test_versao_avl_estatfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlEstatFpha))
    with patch("builtins.open", m):
        avl = AvlEstatFpha.read(ARQ_TESTE)
        assert avl.versao == "19.3"


def test_data_estudo_avl_estatfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlEstatFpha))
    with patch("builtins.open", m):
        avl = AvlEstatFpha.read(ARQ_TESTE)
        assert avl.data_estudo == datetime(year=2022, month=8, day=11)


def test_eq_blocodesvios():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDesvios))
    b1 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocodesvios():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDesvios))
    b1 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data.iloc[0, 0] = -1
    assert b1 != b2


def test_blocodesvios():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDesvios))
    bloco = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            bloco.read(fp)

        assert bloco.data.at[0, "valor"] == 13.60
        assert bloco.data.at[1, "valor"] == 4.08
        assert bloco.data.at[2, "valor"] == 0.02
        assert bloco.data.at[3, "valor"] == 13.58
        assert bloco.data.at[4, "valor"] == 0.01
        assert bloco.data.at[5, "valor"] == 4.08
        assert bloco.data.at[6, "valor"] == 0.0
        assert bloco.data.at[7, "valor"] == 0.0
        assert bloco.data.at[8, "valor"] == 0.0
        assert bloco.data.at[9, "valor"] == 0.0
