from idessem.dessem.avl_fpha3 import AvlFpha3

from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.avl_fpha3 import MockAvlFpha3
import numpy as np

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_avl_fpha3():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha3))
    with patch("builtins.open", m):
        avl = AvlFpha3.read(ARQ_TESTE)
        assert avl.versao is not None
        assert avl.data_estudo is not None
        assert avl.tabela is not None


def test_versao_avl_fpha3():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha3))
    with patch("builtins.open", m):
        avl = AvlFpha3.read(ARQ_TESTE)
        assert avl.versao == "20.2"


def test_data_estudo_avl_fpha3():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha3))
    with patch("builtins.open", m):
        avl = AvlFpha3.read(ARQ_TESTE)
        assert avl.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_avl_fpha3():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha3))
    with patch("builtins.open", m):
        avl = AvlFpha3.read(ARQ_TESTE)
        assert avl.tabela.at[0, "codigo_usina"] == 1
        assert avl.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert avl.tabela.at[0, "volume_armazenado_percentual"] == 0.0
        assert avl.tabela.at[0, "vazao_turbinada_m3s"] == 0.0
        assert avl.tabela.at[0, "vazao_lateral_m3s"] == 0.0
        assert avl.tabela.at[0, "desvio_percentual"] == 100.0
        assert avl.tabela.at[avl.tabela.shape[0] - 1, "codigo_usina"] == 2
        assert (
            avl.tabela.at[avl.tabela.shape[0] - 1, "nome_usina"] == "ITUTINGA"
        )
        assert np.isnan(
            avl.tabela.at[
                avl.tabela.shape[0] - 1, "volume_armazenado_percentual"
            ]
        )
        assert (
            avl.tabela.at[avl.tabela.shape[0] - 1, "vazao_turbinada_m3s"]
            == 241.0
        )
        assert (
            avl.tabela.at[avl.tabela.shape[0] - 1, "vazao_lateral_m3s"]
            == 15552
        )
        assert avl.tabela.at[avl.tabela.shape[0] - 1, "desvio_percentual"] == 0


def test_eq_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha3))
    with patch("builtins.open", m):
        avl1 = AvlFpha3.read(ARQ_TESTE)
        avl2 = AvlFpha3.read(ARQ_TESTE)
        assert avl1 == avl2
