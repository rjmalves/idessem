from datetime import datetime
from unittest.mock import MagicMock, patch

import numpy as np

from idessem.dessem.pdo_somflux import PdoSomFlux
from tests.mocks.arquivos.pdo_somflux import MockPdoSomFlux
from tests.mocks.mock_open import mock_open

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_somflux():
    m: MagicMock = mock_open(read_data="".join(MockPdoSomFlux))
    with patch("builtins.open", m):
        log = PdoSomFlux.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_pdo_somflux():
    m: MagicMock = mock_open(read_data="".join(MockPdoSomFlux))
    with patch("builtins.open", m):
        log = PdoSomFlux.read(ARQ_TESTE)
        assert log.versao == "20.0.11"


def test_data_estudo_pdo_somflux():
    m: MagicMock = mock_open(read_data="".join(MockPdoSomFlux))
    with patch("builtins.open", m):
        log = PdoSomFlux.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2025, month=1, day=24)


def test_tabela_pdo_somflux():
    m: MagicMock = mock_open(read_data="".join(MockPdoSomFlux))
    with patch("builtins.open", m):
        log = PdoSomFlux.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "indice_restricao"] == 1
        assert log.tabela.at[0, "nome_patamar"] == "MEDIA"
        assert log.tabela.at[0, "restricao_violada"] == "-"
        assert log.tabela.at[0, "restricao_liberada"] == ""
        assert log.tabela.at[0, "codigo_restricao"] == 1
        assert log.tabela.at[0, "nome_restricao"] == "# Exp_N"
        assert np.isnan(log.tabela.at[0, "codigo_barra_de"])
        assert np.isnan(log.tabela.at[0, "codigo_barra_para"])
        assert np.isnan(log.tabela.at[0, "indice_circuito"])
        assert log.tabela.at[0, "valor"] == 4647.736
        assert log.tabela.at[0, "limite_inferior"] == -99999.000
        assert log.tabela.at[0, "limite_superior"] == 8000.000
        assert log.tabela.at[0, "multiplicador"] == 0.000


def test_eq_pdo_somflux():
    m: MagicMock = mock_open(read_data="".join(MockPdoSomFlux))
    with patch("builtins.open", m):
        log1 = PdoSomFlux.read(ARQ_TESTE)
        log2 = PdoSomFlux.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_somflux():
    m: MagicMock = mock_open(read_data="".join(MockPdoSomFlux))
    with patch("builtins.open", m):
        log1 = PdoSomFlux.read(ARQ_TESTE)
        log2 = PdoSomFlux.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
