from idessem.dessem.pdo_oper_lpp import PdoOperLpp
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_oper_lpp import MockPdoOperLpp

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_oper_lpp():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperLpp))
    with patch("builtins.open", m):
        pdo = PdoOperLpp.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_oper_lpp():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperLpp))
    with patch("builtins.open", m):
        pdo = PdoOperLpp.read(ARQ_TESTE)
        assert pdo.versao == "21"


def test_data_estudo_pdo_oper_lpp():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperLpp))
    with patch("builtins.open", m):
        pdo = PdoOperLpp.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2025, month=7, day=14)


def test_tabela_pdo_oper_lpp():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperLpp))
    with patch("builtins.open", m):
        pdo = PdoOperLpp.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "codigo_lpp"] == 101
        assert pdo.tabela.at[0, "codigo_dref"] == 0
        assert pdo.tabela.at[0, "codigo_re"] == 907
        assert pdo.tabela.at[0, "valor"] == 427.80
        assert pdo.tabela.at[0, "limite_superior"] == 4886.50
        assert pdo.tabela.at[0, "indice_corte_ativo"] == 2
        assert pdo.tabela.at[0, "coeficiente_linear"] == 5100.00
        assert pdo.tabela.at[0, "codigo_controladora"] == "942"
        assert pdo.tabela.at[0, "tipo_controladora"] == "RELE"
        assert pdo.tabela.at[0, "valor_parametro"] == 400.00
        assert pdo.tabela.at[0, "coeficiente_angular"] == 0.0000
        assert pdo.tabela.at[0, "multiplicador"] == 0.00000000


def test_eq_pdo_oper_lpp():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperLpp))
    with patch("builtins.open", m):
        pdo1 = PdoOperLpp.read(ARQ_TESTE)
        pdo2 = PdoOperLpp.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_oper_lpp():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperLpp))
    with patch("builtins.open", m):
        pdo1 = PdoOperLpp.read(ARQ_TESTE)
        pdo2 = PdoOperLpp.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
