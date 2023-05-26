from idessem.dessem.pdo_hidr import PdoHidr
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_hidr import MockPdoHidr

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_hidr():
    m: MagicMock = mock_open(read_data="".join(MockPdoHidr))
    with patch("builtins.open", m):
        log = PdoHidr.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_pdo_hidr():
    m: MagicMock = mock_open(read_data="".join(MockPdoHidr))
    with patch("builtins.open", m):
        log = PdoHidr.read(ARQ_TESTE)
        assert log.versao == "19.3"


def test_data_estudo_pdo_hidr():
    m: MagicMock = mock_open(read_data="".join(MockPdoHidr))
    with patch("builtins.open", m):
        log = PdoHidr.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_pdo_hidr():
    m: MagicMock = mock_open(read_data="".join(MockPdoHidr))
    with patch("builtins.open", m):
        log = PdoHidr.read(ARQ_TESTE)
        assert log.tabela.at[2, "estagio"] == 1
        assert log.tabela.at[2, "patamar"] == "LEVE"
        assert log.tabela.at[2, "indice_usina"] == 1
        assert log.tabela.at[2, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[2, "submercado"] == "SE"
        assert log.tabela.at[2, "conjunto"] == 99
        assert log.tabela.at[2, "unidade"] == 99
        assert log.tabela.at[2, "valor_agua"] == 64.44
        assert log.tabela.at[2, "volume_final_hm3"] == 580.53
        assert log.tabela.at[2, "volume_final_percentual"] == 86.39
        assert log.tabela.at[2, "vazao_incremental_m3s"] == 45.00
        assert log.tabela.at[2, "vazao_incremental_hm3"] == 0.08
        assert log.tabela.at[2, "vazao_montante_m3s"] == 0.0
        assert log.tabela.at[2, "vazao_montante_hm3"] == 0.0
        assert log.tabela.at[2, "vazao_montante_tempo_viagem_m3s"] == 0.0
        assert log.tabela.at[2, "vazao_montante_tempo_viagem_hm3"] == 0.0
        assert log.tabela.at[2, "vazao_desviada_m3s"] == 0.0
        assert log.tabela.at[2, "vazao_desviada_hm3"] == 0.0
        assert log.tabela.at[2, "vazao_evaporada_m3s"] == 0.59
        assert log.tabela.at[2, "vazao_evaporada_hm3"] == -0.0
        assert log.tabela.at[2, "vazao_uso_alternativo_m3s"] == 0.40
        assert log.tabela.at[2, "vazao_uso_alternativo_hm3"] == 0.0
        assert log.tabela.at[2, "vazao_turbinada_m3s"] == 160.50
        assert log.tabela.at[2, "vazao_turbinada_hm3"] == 0.29
        assert log.tabela.at[2, "vazao_turbinada_minima_m3s"] == 0.0
        assert log.tabela.at[2, "vazao_turbinada_minima_hm3"] == 0.0
        assert log.tabela.at[2, "vazao_turbinada_maxima_m3s"] == 214.00
        assert log.tabela.at[2, "vazao_turbinada_maxima_hm3"] == 0.39
        assert log.tabela.at[2, "engolimento_maximo_m3s"] == 215.85
        assert log.tabela.at[2, "engolimento_maximo_hm3"] == 0.39
        assert log.tabela.at[2, "vazao_vertida_m3s"] == 0.0
        assert log.tabela.at[2, "vazao_vertida_hm3"] == 0.0
        assert log.tabela.at[2, "geracao"] == 36.14
        assert log.tabela.at[2, "geracao_maxima"] == 46.0
        assert log.tabela.at[2, "capacidade"] == 46.0
        assert log.tabela.at[2, "ld"] == "-"
        assert log.tabela.at[2, "perdas_hidraulicas"] == 0.0
        assert log.tabela.at[2, "altura_queda"] == 25.68


def test_eq_pdo_hidr():
    m: MagicMock = mock_open(read_data="".join(MockPdoHidr))
    with patch("builtins.open", m):
        log1 = PdoHidr.read(ARQ_TESTE)
        log2 = PdoHidr.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_hidr():
    m: MagicMock = mock_open(read_data="".join(MockPdoHidr))
    with patch("builtins.open", m):
        log1 = PdoHidr.read(ARQ_TESTE)
        log2 = PdoHidr.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
