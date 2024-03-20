from idessem.dessem.pdo_reserva import PdoReserva
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
import numpy as np

from tests.mocks.arquivos.pdo_reserva import MockPdoReserva

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_reserva():
    m: MagicMock = mock_open(read_data="".join(MockPdoReserva))
    with patch("builtins.open", m):
        log = PdoReserva.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_pdo_reserva():
    m: MagicMock = mock_open(read_data="".join(MockPdoReserva))
    with patch("builtins.open", m):
        log = PdoReserva.read(ARQ_TESTE)
        assert log.versao == "19.3"


def test_data_estudo_pdo_reserva():
    m: MagicMock = mock_open(read_data="".join(MockPdoReserva))
    with patch("builtins.open", m):
        log = PdoReserva.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_pdo_reserva():
    m: MagicMock = mock_open(read_data="".join(MockPdoReserva))
    with patch("builtins.open", m):
        log = PdoReserva.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "nome_patamar"] == "LEVE"
        assert log.tabela.at[0, "codigo_entidade"] == 1
        assert log.tabela.at[0, "nome_entidade"] == "CAGSECO - RE"
        assert log.tabela.at[0, "tipo_entidade"] == "A"
        assert log.tabela.at[0, "codigo_area"] == 1
        assert log.tabela.at[0, "codigo_conjunto"] is None
        assert log.tabela.at[0, "reserva"] == 3285.00
        assert log.tabela.at[0, "geracao"] == 5028.54
        assert log.tabela.at[0, "reserva_minima"] == 3285.0
        assert np.isnan(log.tabela.at[1, "reserva_minima"])
        assert log.tabela.at[0, "multiplicador"] == 0
        assert log.tabela.at[0, "geracao_maxima"] == 8313.54


def test_eq_pdo_reserva():
    m: MagicMock = mock_open(read_data="".join(MockPdoReserva))
    with patch("builtins.open", m):
        log1 = PdoReserva.read(ARQ_TESTE)
        log2 = PdoReserva.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_reserva():
    m: MagicMock = mock_open(read_data="".join(MockPdoReserva))
    with patch("builtins.open", m):
        log1 = PdoReserva.read(ARQ_TESTE)
        log2 = PdoReserva.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
