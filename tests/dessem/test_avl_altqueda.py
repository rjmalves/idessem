from idessem.dessem.avl_altqueda import AvlAltQueda

from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.avl_altqueda import MockAvlAltqueda


def test_atributos_encontrados_avl_altqueda():
    m: MagicMock = mock_open(read_data="".join(MockAvlAltqueda))
    with patch("builtins.open", m):
        log = AvlAltQueda.le_arquivo("")
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_avl_altqueda():
    m: MagicMock = mock_open(read_data="".join(MockAvlAltqueda))
    with patch("builtins.open", m):
        log = AvlAltQueda.le_arquivo("")
        assert log.versao == "19.3"


def test_data_estudo_avl_altqueda():
    m: MagicMock = mock_open(read_data="".join(MockAvlAltqueda))
    with patch("builtins.open", m):
        log = AvlAltQueda.le_arquivo("")
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_avl_altqueda():
    m: MagicMock = mock_open(read_data="".join(MockAvlAltqueda))
    with patch("builtins.open", m):
        log = AvlAltQueda.le_arquivo("")
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "iteracao"] == 1
        assert log.tabela.at[0, "ides"] == "S"
        assert log.tabela.at[0, "patamar"] == "LEVE"
        assert log.tabela.at[0, "indice_usina"] == 1
        assert log.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[0, "altura_montante"] == 911.78
        assert log.tabela.at[0, "altura_jusante"] == 886.10
        assert log.tabela.at[0, "altura_liquida"] == 25.68
        assert log.tabela.at[0, "vazao_defluente_m3s"] == 160.50
        assert log.tabela.at[0, "problema"] is None


def test_eq_avl_altqueda():
    m: MagicMock = mock_open(read_data="".join(MockAvlAltqueda))
    with patch("builtins.open", m):
        log1 = AvlAltQueda.le_arquivo("")
        log2 = AvlAltQueda.le_arquivo("")
        assert log1 == log2


def test_neq_avl_altqueda():
    m: MagicMock = mock_open(read_data="".join(MockAvlAltqueda))
    with patch("builtins.open", m):
        log1 = AvlAltQueda.le_arquivo("")
        log2 = AvlAltQueda.le_arquivo("")
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
