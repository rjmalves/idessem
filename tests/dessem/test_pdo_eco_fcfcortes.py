from idessem.dessem.pdo_eco_fcfcortes import PdoEcoFcfCortes
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.pdo_eco_fcfcortes import MockPdoEcoFcfCortes

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_eco_fcfcortes():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoFcfCortes))
    with patch("builtins.open", m):
        pdo = PdoEcoFcfCortes.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_eco_fcfcortes():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoFcfCortes))
    with patch("builtins.open", m):
        pdo = PdoEcoFcfCortes.read(ARQ_TESTE)
        assert pdo.versao == "19.4.1"


def test_data_estudo_pdo_eco_fcfcortes():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoFcfCortes))
    with patch("builtins.open", m):
        pdo = PdoEcoFcfCortes.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2023, month=6, day=13)


def test_tabela_pdo_eco_fcfcortes():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoFcfCortes))
    with patch("builtins.open", m):
        pdo = PdoEcoFcfCortes.read(ARQ_TESTE)

        assert pdo.tabela.at[1, "indice_corte"] == 1
        assert pdo.tabela.at[1, "tipo_entidade"] == "USIH"
        assert pdo.tabela.at[1, "indice_entidade"] == 1
        assert pdo.tabela.at[1, "nome_entidade"] == "CAMARGOS"
        assert pdo.tabela.at[1, "tipo_coeficiente"] == "VARM"
        assert pdo.tabela.at[1, "indice_lag"] == 0
        assert pdo.tabela.at[1, "indice_patamar"] == 0
        assert pdo.tabela.at[1, "valor_coeficiente"] == 0.0005367
        assert pdo.tabela.at[1, "unidade"] == "(1000$/hm3)"


def test_eq_pdo_eco_fcfcortes():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoFcfCortes))
    with patch("builtins.open", m):
        log1 = PdoEcoFcfCortes.read(ARQ_TESTE)
        log2 = PdoEcoFcfCortes.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_eco_fcfcortes():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoFcfCortes))
    with patch("builtins.open", m):
        log1 = PdoEcoFcfCortes.read(ARQ_TESTE)
        log2 = PdoEcoFcfCortes.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
