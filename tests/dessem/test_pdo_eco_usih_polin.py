from idessem.dessem.pdo_eco_usih_polin import PdoEcoUsihPolin
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_eco_usih_polin import MockPdoEcoUsihPolin

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_eco_usih_polin():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihPolin))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihPolin.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_eco_usih_polin():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihPolin))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihPolin.read(ARQ_TESTE)
        assert pdo.versao == "19.4.1"


def test_data_estudo_pdo_eco_usih_polin():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihPolin))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihPolin.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2023, month=6, day=13)


def test_tabela_pdo_eco_usih_polin():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihPolin))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihPolin.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "indice_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert pdo.tabela.at[0, "indice_coeficiente"] == 0
        assert pdo.tabela.at[0, "coeficiente_cota_volume"] == 0.89296997e03
        assert pdo.tabela.at[0, "coeficiente_area_cota"] == 0.13334300e05
        assert pdo.tabela.at[0, "cota_vazao_hjus1"] == 0.88609998e03
        assert pdo.tabela.at[0, "hjus1"] == 0.00
        assert pdo.tabela.at[0, "cota_vazao_hjus2"] == 0.00000000e00
        assert pdo.tabela.at[0, "hjus2"] == 0.00
        assert pdo.tabela.at[0, "cota_vazao_hjus3"] == 0.00000000e00
        assert pdo.tabela.at[0, "hjus3"] == 0.00
        assert pdo.tabela.at[0, "cota_vazao_hjus4"] == 0.00000000e00
        assert pdo.tabela.at[0, "hjus4"] == 0.00
        assert pdo.tabela.at[0, "cota_vazao_hjus5"] == 0.00000000e00
        assert pdo.tabela.at[0, "hjus5"] == 0.00
        assert pdo.tabela.at[0, "cota_vazao_hjus6"] == 0.00000000e00
        assert pdo.tabela.at[0, "hjus6"] == 0.00


def test_eq_pdo_eco_usih_polin():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihPolin))
    with patch("builtins.open", m):
        log1 = PdoEcoUsihPolin.read(ARQ_TESTE)
        log2 = PdoEcoUsihPolin.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_eco_usih_polin():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihPolin))
    with patch("builtins.open", m):
        log1 = PdoEcoUsihPolin.read(ARQ_TESTE)
        log2 = PdoEcoUsihPolin.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
