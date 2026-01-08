from idessem.dessem.pdo_cmosist import PdoCmosist
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_cmosist import MockPdoCmosist

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_cmosist():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmosist))
    with patch("builtins.open", m):
        pdo = PdoCmosist.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_cmosist():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmosist))
    with patch("builtins.open", m):
        pdo = PdoCmosist.read(ARQ_TESTE)
        assert pdo.versao == "21.2.1"


def test_data_estudo_pdo_cmosist():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmosist))
    with patch("builtins.open", m):
        pdo = PdoCmosist.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2025, month=11, day=18)


def test_tabela_pdo_cmosist():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmosist))
    with patch("builtins.open", m):
        pdo = PdoCmosist.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "nome_patamar"] == "MEDIA"
        assert pdo.tabela.at[0, "nome_submercado"] == "SE"
        assert pdo.tabela.at[0, "cmo"] == 316.70
        assert pdo.tabela.at[0, "pi_demanda"] == 316.70

        assert pdo.tabela.at[11, "estagio"] == 3
        assert pdo.tabela.at[11, "nome_patamar"] == "LEVE"
        assert pdo.tabela.at[11, "nome_submercado"] == "S"
        assert pdo.tabela.at[11, "cmo"] == 302.97
        assert pdo.tabela.at[11, "pi_demanda"] == 302.97


def test_eq_pdo_cmosist():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmosist))
    with patch("builtins.open", m):
        pdo1 = PdoCmosist.read(ARQ_TESTE)
        pdo2 = PdoCmosist.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_cmosist():
    m: MagicMock = mock_open(read_data="".join(MockPdoCmosist))
    with patch("builtins.open", m):
        pdo1 = PdoCmosist.read(ARQ_TESTE)
        pdo2 = PdoCmosist.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
