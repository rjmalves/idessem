from idessem.dessem.pdo_aval_qmaxusih import PdoAvalQmaxUsih
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
import numpy as np

from tests.mocks.arquivos.pdo_aval_qmaxusih import (
    MockPdoAvalQmaxUsih2001,
    MockPdoAvalQmaxUsih,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_aval_qmaxusih():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih))
    with patch("builtins.open", m):
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_pdo_aval_qmaxusih():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih))
    with patch("builtins.open", m):
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.versao == "20.4"


def test_data_estudo_pdo_aval_qmaxusih():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih))
    with patch("builtins.open", m):
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_pdo_aval_qmaxusih():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih))
    with patch("builtins.open", m):
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "codigo_usina"] == 1
        assert log.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[0, "volume_medio_percentual"] == 78.87
        assert log.tabela.at[0, "vazao_turbinada_m3s"] == 34.02
        assert log.tabela.at[0, "vazao_vertida_m3s"] == 0
        assert log.tabela.at[0, "altura_montante"] == 911.016
        assert log.tabela.at[0, "vazao_jusante_m3s"] == 34.02
        assert log.tabela.at[0, "altura_jusante"] == 885.689
        assert log.tabela.at[0, "altura_liquida"] == 25.23
        assert log.tabela.at[0, "vazao_turbinada_maxima_m3s"] == 214.00
        assert log.tabela.at[0, "engolimento_maximo_m3s"] == 215.09
        assert log.tabela.at[0, "geracao_maxima"] == 46


def test_eq_pdo_aval_qmaxusih():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih))
    with patch("builtins.open", m):
        log1 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        log2 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_aval_qmaxusih():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih))
    with patch("builtins.open", m):
        log1 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        log2 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2


def test_atributos_encontrados_pdo_aval_qmaxusih_2001():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih2001))
    with patch("builtins.open", m):
        PdoAvalQmaxUsih.set_version("20.1")
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_pdo_aval_qmaxusih_2001():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih2001))
    with patch("builtins.open", m):
        PdoAvalQmaxUsih.set_version("20.1")
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.versao == "20.2"


def test_data_estudo_pdo_aval_qmaxusih_2001():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih2001))
    with patch("builtins.open", m):
        PdoAvalQmaxUsih.set_version("20.1")
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_pdo_aval_qmaxusih_2001():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih2001))
    with patch("builtins.open", m):
        PdoAvalQmaxUsih.set_version("20.1")
        log = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "codigo_usina"] == 1
        assert log.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[0, "volume_medio_percentual"] == 78.87
        assert log.tabela.at[0, "vazao_turbinada_m3s"] == 34.02
        assert log.tabela.at[0, "vazao_vertida_m3s"] == 0
        assert log.tabela.at[0, "vazao_turbinada_maxima_m3s"] == 214.00
        assert log.tabela.at[0, "engolimento_maximo_m3s"] == 215.09
        assert log.tabela.at[0, "geracao_maxima"] == 46


def test_eq_pdo_aval_qmaxusih_2001():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih2001))
    with patch("builtins.open", m):
        PdoAvalQmaxUsih.set_version("20.1")
        log1 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        log2 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_aval_qmaxusih_2001():
    m: MagicMock = mock_open(read_data="".join(MockPdoAvalQmaxUsih2001))
    with patch("builtins.open", m):
        PdoAvalQmaxUsih.set_version("20.1")
        log1 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        log2 = PdoAvalQmaxUsih.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
