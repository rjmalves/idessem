from datetime import datetime
from unittest.mock import MagicMock, patch

from idessem.dessem.log_inviab import LogInviab
from tests.mocks.arquivos.log_inviab import MockLogInviab
from tests.mocks.mock_open import mock_open

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_log_inviab():
    m: MagicMock = mock_open(read_data="".join(MockLogInviab))
    with patch("builtins.open", m):
        log = LogInviab.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_log_inviab():
    m: MagicMock = mock_open(read_data="".join(MockLogInviab))
    with patch("builtins.open", m):
        log = LogInviab.read(ARQ_TESTE)
        assert log.versao == "20.0.11"


def test_data_estudo_log_inviab():
    m: MagicMock = mock_open(read_data="".join(MockLogInviab))
    with patch("builtins.open", m):
        log = LogInviab.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2024, month=1, day=26)


def test_tabela_log_inviab():
    m: MagicMock = mock_open(read_data="".join(MockLogInviab))
    with patch("builtins.open", m):
        log = LogInviab.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "restricao"] == "INF_LIM_TERM_383"
        assert log.tabela.at[0, "violacao"] == 327.90545
        assert log.tabela.at[0, "unidade"] == "MW"


def test_eq_log_inviab():
    m: MagicMock = mock_open(read_data="".join(MockLogInviab))
    with patch("builtins.open", m):
        log1 = LogInviab.read(ARQ_TESTE)
        log2 = LogInviab.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_log_inviab():
    m: MagicMock = mock_open(read_data="".join(MockLogInviab))
    with patch("builtins.open", m):
        log1 = LogInviab.read(ARQ_TESTE)
        log2 = LogInviab.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
