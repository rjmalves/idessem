from idessem.dessem.pdo_term import PdoTerm
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_term import MockPdoTerm

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_term():
    m: MagicMock = mock_open(read_data="".join(MockPdoTerm))
    with patch("builtins.open", m):
        pdo = PdoTerm.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_term():
    m: MagicMock = mock_open(read_data="".join(MockPdoTerm))
    with patch("builtins.open", m):
        pdo = PdoTerm.read(ARQ_TESTE)
        assert pdo.versao == "19.3"


def test_data_estudo_pdo_term():
    m: MagicMock = mock_open(read_data="".join(MockPdoTerm))
    with patch("builtins.open", m):
        pdo = PdoTerm.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_pdo_term():
    m: MagicMock = mock_open(read_data="".join(MockPdoTerm))
    with patch("builtins.open", m):
        pdo = PdoTerm.read(ARQ_TESTE)
        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "nome_patamar"] == "LEVE"
        assert pdo.tabela.at[0, "codigo_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "ANGRA 1"
        assert pdo.tabela.at[0, "codigo_unidade"] == 1
        assert pdo.tabela.at[0, "nome_submercado"] == "SE"
        assert pdo.tabela.at[0, "geracao"] == 582.00
        assert pdo.tabela.at[0, "geracao_minima"] == 0.00
        assert pdo.tabela.at[0, "geracao_maxima"] == 640.00
        assert pdo.tabela.at[0, "capacidade"] == 640.00
        assert pdo.tabela.at[0, "status"] == "L"
        assert pdo.tabela.at[0, "custo_linear"] == 31.17


def test_eq_pdo_term():
    m: MagicMock = mock_open(read_data="".join(MockPdoTerm))
    with patch("builtins.open", m):
        pdo1 = PdoTerm.read(ARQ_TESTE)
        pdo2 = PdoTerm.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_term():
    m: MagicMock = mock_open(read_data="".join(MockPdoTerm))
    with patch("builtins.open", m):
        pdo1 = PdoTerm.read(ARQ_TESTE)
        pdo2 = PdoTerm.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
