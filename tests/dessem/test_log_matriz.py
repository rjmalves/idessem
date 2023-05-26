from idessem.dessem.log_matriz import LogMatriz

from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.log_matriz import MockLogMatriz

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_log_matriz():
    m: MagicMock = mock_open(read_data="".join(MockLogMatriz))
    with patch("builtins.open", m):
        log = LogMatriz.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_log_matriz():
    m: MagicMock = mock_open(read_data="".join(MockLogMatriz))
    with patch("builtins.open", m):
        log = LogMatriz.read(ARQ_TESTE)
        assert log.versao == "19.3"


def test_data_estudo_log_matriz():
    m: MagicMock = mock_open(read_data="".join(MockLogMatriz))
    with patch("builtins.open", m):
        log = LogMatriz.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_log_matriz():
    m: MagicMock = mock_open(read_data="".join(MockLogMatriz))
    with patch("builtins.open", m):
        log = LogMatriz.read(ARQ_TESTE)
        assert log.tabela.at[0, "iteracao"] == 1
        assert log.tabela.at[0, "tipo"] == "PL"
        assert log.tabela.at[0, "variaveis"] == 489633
        assert log.tabela.at[0, "variaveis_inteiras"] == 0
        assert log.tabela.at[0, "restricoes"] == 114133
        assert log.tabela.at[0, "restricoes_inteiras"] == 0
        assert log.tabela.at[0, "elementos"] == 1486191
        assert log.tabela.at[0, "tempo_min"] == 0.3
        assert log.tabela.at[0, "funcao_objetivo"] == -12925383.197
        assert log.tabela.at[0, "status"] == 1


def test_eq_log_matriz():
    m: MagicMock = mock_open(read_data="".join(MockLogMatriz))
    with patch("builtins.open", m):
        log1 = LogMatriz.read(ARQ_TESTE)
        log2 = LogMatriz.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_log_matriz():
    m: MagicMock = mock_open(read_data="".join(MockLogMatriz))
    with patch("builtins.open", m):
        log1 = LogMatriz.read(ARQ_TESTE)
        log2 = LogMatriz.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
