from idessem.dessem.pdo_eco_usih import PdoEcoUsih
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_eco_usih import (
    MockPdoEcoUsih,
    MockPdoEcoUsih190301,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_eco_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih))
    with patch("builtins.open", m):
        pdo = PdoEcoUsih.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_eco_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih))
    with patch("builtins.open", m):
        pdo = PdoEcoUsih.read(ARQ_TESTE)
        assert pdo.versao == "19.4.2"


def test_data_estudo_pdo_eco_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih))
    with patch("builtins.open", m):
        pdo = PdoEcoUsih.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2023, month=6, day=13)


def test_tabela_pdo_eco_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih))
    with patch("builtins.open", m):
        pdo = PdoEcoUsih.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "indice_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert pdo.tabela.at[0, "submercado"] == "SE"
        assert pdo.tabela.at[0, "indice_usina_jusante"] == 2
        assert pd.isna(pdo.tabela.at[0, "indice_usina_desvio"])
        assert pdo.tabela.at[0, "indice_usina_jusante_earm"] == 2
        assert pdo.tabela.at[0, "estagio_inicial"] == 1
        assert pd.isna(pdo.tabela.at[0, "volume_morto_inicial_hm3"])
        assert pd.isna(pdo.tabela.at[0, "volume_morto_inicial_percentual"])
        assert pdo.tabela.at[0, "volume_util_inicial_hm3"] == 646.93
        assert pdo.tabela.at[0, "volume_util_inicial_percentual"] == 96.27
        assert pdo.tabela.at[0, "volume_armazenado_minimo_hm3"] == 120.00
        assert pdo.tabela.at[0, "volume_armazenado_maximo_hm3"] == 792.00
        assert pdo.tabela.at[0, "volume_soleira_vertedouro_hm3"] == 120.00
        assert (
            pdo.tabela.at[0, "volume_soleira_vertedouro_util_percentual"] == 0
        )
        assert pdo.tabela.at[0, "volume_soleira_desvio_hm3"] == 120.00
        assert (
            pdo.tabela.at[0, "volume_soleira_desvio_util_percentual"] == 0.00
        )
        assert pdo.tabela.at[0, "volume_referencia_hm3"] == 792.00
        assert pdo.tabela.at[0, "tipo_reservatorio"] == "RV"
        assert pdo.tabela.at[0, "tipo_regularizacao"] == "M"
        assert pdo.tabela.at[0, "flag_evaporacao"] == 1
        assert pdo.tabela.at[0, "numero_conjuntos"] == 1
        assert pdo.tabela.at[0, "produtibilidade_especifica"] == 0.008767
        assert pdo.tabela.at[0, "tipo_perdas"] == "m"
        assert pdo.tabela.at[0, "perdas_hidraulicas"] == 0.095
        assert pdo.tabela.at[0, "canal_fuga_medio"] == 885.73
        assert pdo.tabela.at[0, "influencia_vertimento_canal_fuga"] == 1


def test_eq_pdo_eco_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih))
    with patch("builtins.open", m):
        log1 = PdoEcoUsih.read(ARQ_TESTE)
        log2 = PdoEcoUsih.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_eco_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih))
    with patch("builtins.open", m):
        log1 = PdoEcoUsih.read(ARQ_TESTE)
        log2 = PdoEcoUsih.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2


def test_atributos_encontrados_pdo_eco_usih_190301():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih190301))
    with patch("builtins.open", m):
        PdoEcoUsih.set_version("19.3.1")
        pdo = PdoEcoUsih.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_eco_usih_190301():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih190301))
    with patch("builtins.open", m):
        PdoEcoUsih.set_version("19.3.1")
        pdo = PdoEcoUsih.read(ARQ_TESTE)
        assert pdo.versao == "19.3.1"


def test_data_estudo_pdo_eco_usih_190301():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih190301))
    with patch("builtins.open", m):
        PdoEcoUsih.set_version("19.3.1")
        pdo = PdoEcoUsih.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_pdo_eco_usih_190301():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih190301))
    with patch("builtins.open", m):
        PdoEcoUsih.set_version("19.3.1")
        pdo = PdoEcoUsih.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "indice_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert pdo.tabela.at[0, "submercado"] == "SE"
        assert pdo.tabela.at[0, "indice_usina_jusante"] == 2
        assert pd.isna(pdo.tabela.at[0, "indice_usina_desvio"])
        assert pdo.tabela.at[0, "indice_usina_jusante_earm"] == 2
        assert pdo.tabela.at[0, "estagio_inicial"] == 1
        assert pd.isna(pdo.tabela.at[0, "volume_morto_inicial_hm3"])
        assert pd.isna(pdo.tabela.at[0, "volume_morto_inicial_percentual"])
        assert pdo.tabela.at[0, "volume_util_inicial_hm3"] == 580.74
        assert pdo.tabela.at[0, "volume_util_inicial_percentual"] == 86.42
        assert pdo.tabela.at[0, "volume_armazenado_minimo_hm3"] == 120.00
        assert pdo.tabela.at[0, "volume_armazenado_maximo_hm3"] == 792.00
        assert pdo.tabela.at[0, "volume_soleira_vertedouro_hm3"] == 120.00
        assert (
            pdo.tabela.at[0, "volume_soleira_vertedouro_util_percentual"] == 0
        )
        assert pdo.tabela.at[0, "volume_soleira_desvio_hm3"] == 120.00
        assert (
            pdo.tabela.at[0, "volume_soleira_desvio_util_percentual"] == 0.00
        )
        assert pdo.tabela.at[0, "volume_referencia_hm3"] == 792.00
        assert pdo.tabela.at[0, "tipo_regularizacao"] == "M"
        assert pdo.tabela.at[0, "flag_evaporacao"] == 1
        assert pdo.tabela.at[0, "numero_conjuntos"] == 1
        assert pdo.tabela.at[0, "produtibilidade_especifica"] == 0.008767
        assert pdo.tabela.at[0, "tipo_perdas"] == "m"
        assert pdo.tabela.at[0, "perdas_hidraulicas"] == 0.09
        assert pdo.tabela.at[0, "canal_fuga_medio"] == 885.73
        assert pdo.tabela.at[0, "influencia_vertimento_canal_fuga"] == 0


def test_eq_pdo_eco_usih_190301():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih190301))
    with patch("builtins.open", m):
        PdoEcoUsih.set_version("19.3.1")
        log1 = PdoEcoUsih.read(ARQ_TESTE)
        log2 = PdoEcoUsih.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_eco_usih_190301():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsih190301))
    with patch("builtins.open", m):
        PdoEcoUsih.set_version("19.3.1")
        log1 = PdoEcoUsih.read(ARQ_TESTE)
        PdoEcoUsih.set_version("19.3.1")
        log2 = PdoEcoUsih.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
