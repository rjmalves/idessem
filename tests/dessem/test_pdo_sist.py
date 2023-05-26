from idessem.dessem.pdo_sist import PdoSist
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_sist import MockPdoSist

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_sist():
    m: MagicMock = mock_open(read_data="".join(MockPdoSist))
    with patch("builtins.open", m):
        log = PdoSist.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_pdo_sist():
    m: MagicMock = mock_open(read_data="".join(MockPdoSist))
    with patch("builtins.open", m):
        log = PdoSist.read(ARQ_TESTE)
        assert log.versao == "19.3"


def test_data_estudo_pdo_sist():
    m: MagicMock = mock_open(read_data="".join(MockPdoSist))
    with patch("builtins.open", m):
        log = PdoSist.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_pdo_sist():
    m: MagicMock = mock_open(read_data="".join(MockPdoSist))
    with patch("builtins.open", m):
        log = PdoSist.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "patamar"] == "LEVE"
        assert log.tabela.at[0, "submercado"] == "SE"
        assert log.tabela.at[0, "cmo"] == 71.48
        assert log.tabela.at[0, "demanda"] == 36935.91
        assert log.tabela.at[0, "perdas"] == "-"
        assert log.tabela.at[0, "geracao_pequenas_usinas"] == 0.0
        assert log.tabela.at[0, "geracao_fixa_barra"] == 0.0
        assert log.tabela.at[0, "geracao_renovavel"] == 5006.00
        assert log.tabela.at[0, "geracao_hidraulica"] == 27152.97
        assert log.tabela.at[0, "geracao_termica"] == 2555.95
        assert log.tabela.at[0, "consumo_elevatorias"] == 108.62
        assert log.tabela.at[0, "importacao"] == 6479.64
        assert log.tabela.at[0, "exportacao"] == 6079.64
        assert log.tabela.at[0, "corte_carga"] == 0.0
        assert log.tabela.at[0, "saldo"] == -3461.61
        assert log.tabela.at[0, "recebimento"] == 3461.61
        assert log.tabela.at[0, "geracao_termica_minima"] == 2555.95
        assert log.tabela.at[0, "geracao_termica_maxima"] == 9489.79
        assert log.tabela.at[0, "energia_armazenada"] == 122020.78


def test_eq_pdo_sist():
    m: MagicMock = mock_open(read_data="".join(MockPdoSist))
    with patch("builtins.open", m):
        log1 = PdoSist.read(ARQ_TESTE)
        log2 = PdoSist.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_sist():
    m: MagicMock = mock_open(read_data="".join(MockPdoSist))
    with patch("builtins.open", m):
        log1 = PdoSist.read(ARQ_TESTE)
        log2 = PdoSist.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
