from datetime import datetime
from unittest.mock import MagicMock, patch

from idessem.dessem.pdo_cmobar import PdoCmoBar
from tests.mocks.arquivos.pdo_cmobar import MockPdoCmoBar
from tests.mocks.mock_open import mock_open

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_cmobar():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmoBar))
    with patch("builtins.open", m):
        log = PdoCmoBar.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_pdo_cmobar():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmoBar))
    with patch("builtins.open", m):
        log = PdoCmoBar.read(ARQ_TESTE)
        assert log.versao == "20.0.11"


def test_data_estudo_pdo_cmobar():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmoBar))
    with patch("builtins.open", m):
        log = PdoCmoBar.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2025, month=1, day=24)


def test_tabela_pdo_cmobar():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmoBar))
    with patch("builtins.open", m):
        log = PdoCmoBar.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "nome_patamar"] == "MEDIA"
        assert log.tabela.at[0, "codigo_barra"] == 10
        assert log.tabela.at[0, "nome_barra"] == "ANGRA1UNE001"
        assert log.tabela.at[0, "nome_submercado"] == "SE"
        assert log.tabela.at[0, "cmo"] == 62.97


def test_eq_pdo_cmobar():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmoBar))
    with patch("builtins.open", m):
        log1 = PdoCmoBar.read(ARQ_TESTE)
        log2 = PdoCmoBar.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_cmobar():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmoBar))
    with patch("builtins.open", m):
        log1 = PdoCmoBar.read(ARQ_TESTE)
        log2 = PdoCmoBar.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
