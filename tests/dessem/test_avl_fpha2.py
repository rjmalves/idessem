from idessem.dessem.avl_fpha2 import AvlFpha2

from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.avl_fpha2 import MockAvlFpha2

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_avl_fpha2():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha2))
    with patch("builtins.open", m):
        log = AvlFpha2.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_avl_fpha2():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha2))
    with patch("builtins.open", m):
        log = AvlFpha2.read(ARQ_TESTE)
        assert log.versao == "20.2"


def test_data_estudo_avl_fpha2():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha2))
    with patch("builtins.open", m):
        log = AvlFpha2.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_avl_fpha2():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha2))
    with patch("builtins.open", m):
        log = AvlFpha2.read(ARQ_TESTE)
        assert log.tabela.at[0, "codigo_usina"] == 1
        assert log.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[0, "volume_armazenado_percentual"] == 0.0
        assert log.tabela.at[0, "vazao_turbinada_m3s"] == 0.0
        assert log.tabela.at[0, "desvio_percentual"] == 100.0


def test_eq_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha2))
    with patch("builtins.open", m):
        log1 = AvlFpha2.read(ARQ_TESTE)
        log2 = AvlFpha2.read(ARQ_TESTE)
        assert log1 == log2
