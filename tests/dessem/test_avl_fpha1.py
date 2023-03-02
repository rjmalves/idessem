from idessem.dessem.avl_fpha1 import AvlFpha1

from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.avl_fpha1 import MockAvlFpha1


def test_atributos_encontrados_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha1))
    with patch("builtins.open", m):
        log = AvlFpha1.le_arquivo("")
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha1))
    with patch("builtins.open", m):
        log = AvlFpha1.le_arquivo("")
        assert log.versao == "19.3"


def test_data_estudo_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha1))
    with patch("builtins.open", m):
        log = AvlFpha1.le_arquivo("")
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha1))
    with patch("builtins.open", m):
        log = AvlFpha1.le_arquivo("")
        assert log.tabela.at[0, "indice_usina"] == 1
        assert log.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[0, "segmento_fpha"] == 1
        assert log.tabela.at[0, "fator_correcao"] == 1.0
        assert log.tabela.at[0, "vazao_lateral_media"] == 0
        assert log.tabela.at[0, "rhs"] == -11.8461
        assert log.tabela.at[0, "coeficiente_volume_util"] == 0.020604
        assert log.tabela.at[0, "coeficiente_vazao_turbinada"] == 0.224440
        assert log.tabela.at[0, "coeficiente_vazao_lateral"] == 0.0


def test_eq_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha1))
    with patch("builtins.open", m):
        log1 = AvlFpha1.le_arquivo("")
        log2 = AvlFpha1.le_arquivo("")
        assert log1 == log2


def test_neq_avl_fpha1():
    m: MagicMock = mock_open(read_data="".join(MockAvlFpha1))
    with patch("builtins.open", m):
        log1 = AvlFpha1.le_arquivo("")
        log2 = AvlFpha1.le_arquivo("")
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
