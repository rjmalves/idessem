from idessem.dessem.pdo_inter import PdoInter
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_inter import MockPdoInter

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_inter():
    m: MagicMock = mock_open(read_data="".join(MockPdoInter))
    with patch("builtins.open", m):
        pdo = PdoInter.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_inter():
    m: MagicMock = mock_open(read_data="".join(MockPdoInter))
    with patch("builtins.open", m):
        pdo = PdoInter.read(ARQ_TESTE)
        assert pdo.versao == "19.4.3"


def test_data_estudo_pdo_inter():
    m: MagicMock = mock_open(read_data="".join(MockPdoInter))
    with patch("builtins.open", m):
        pdo = PdoInter.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_pdo_inter():
    m: MagicMock = mock_open(read_data="".join(MockPdoInter))
    with patch("builtins.open", m):
        pdo = PdoInter.read(ARQ_TESTE)
        assert pdo.tabela.at[1, "estagio"] == 1
        assert pdo.tabela.at[1, "patamar"] == "LEVE"
        assert pdo.tabela.at[1, "indice_intercambio"] == 1
        assert pdo.tabela.at[1, "nome_submercado_de"] == "S"
        assert pdo.tabela.at[1, "nome_submercado_para"] == "IV"
        assert pdo.tabela.at[1, "intercambio"] == 3877.24


def test_eq_pdo_inter():
    m: MagicMock = mock_open(read_data="".join(MockPdoInter))
    with patch("builtins.open", m):
        pdo1 = PdoInter.read(ARQ_TESTE)
        pdo2 = PdoInter.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_inter():
    m: MagicMock = mock_open(read_data="".join(MockPdoInter))
    with patch("builtins.open", m):
        pdo1 = PdoInter.read(ARQ_TESTE)
        pdo2 = PdoInter.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
