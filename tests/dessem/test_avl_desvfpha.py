from idessem.dessem.avl_desvfpha import AvlDesvFpha

from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.avl_desvfpha import (
    MockAvlDesvfpha,
    MockAvlDesvfpha190300,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_avl_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha))
    with patch("builtins.open", m):
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_avl_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha))
    with patch("builtins.open", m):
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.versao == "19.4.2"


def test_data_estudo_avl_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha))
    with patch("builtins.open", m):
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2023, month=6, day=13)


def test_tabela_avl_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha))
    with patch("builtins.open", m):
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "indice_usina"] == 1
        assert log.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[0, "volume_medio_hm3"] == 766.94
        assert log.tabela.at[0, "volume_medio_percentual"] == 96.27
        assert log.tabela.at[0, "vazao_incremental_m3s"] == 88.00
        assert log.tabela.at[0, "vazao_turbinada_m3s"] == 83.46
        assert log.tabela.at[0, "vazao_vertida_m3s"] == 0.0
        assert log.tabela.at[0, "vazao_jusante_m3s"] == 83.46
        assert log.tabela.at[0, "vazao_lateral_usina_m3s"] == 0.0
        assert log.tabela.at[0, "vazao_lateral_posto_m3s"] == 0.0
        assert log.tabela.at[0, "altura_jusante"] == 885.742
        assert log.tabela.at[0, "altura_montante"] == 912.693
        assert log.tabela.at[0, "produtibilidade_especifica"] == 0.008767
        assert log.tabela.at[0, "tipo_perdas"] == "m"
        assert log.tabela.at[0, "perdas_hidraulicas"] == 0.095
        assert log.tabela.at[0, "influencia_vertimento_canal_fuga"] == 1
        assert log.tabela.at[0, "afogamento_canal_fuga"] == 0
        assert log.tabela.at[0, "potencia_instalada"] == 46.00
        assert log.tabela.at[0, "geracao_fph"] == 19.65
        assert log.tabela.at[0, "geracao_pl"] == 19.65
        assert log.tabela.at[0, "geracao_fpha"] == 19.65
        assert log.tabela.at[0, "desvio_absoluto_fph_pl"] == 0.01
        assert log.tabela.at[0, "desvio_percentual_fph_pl"] == 0.03
        assert log.tabela.at[0, "desvio_absoluto_fph_fpha"] == 0.01
        assert log.tabela.at[0, "desvio_percentual_fph_fpha"] == 0.03


def test_eq_avl_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha))
    with patch("builtins.open", m):
        log1 = AvlDesvFpha.read(ARQ_TESTE)
        log2 = AvlDesvFpha.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_avl_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha))
    with patch("builtins.open", m):
        log1 = AvlDesvFpha.read(ARQ_TESTE)
        log2 = AvlDesvFpha.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2


def test_atributos_encontrados_avl_desvfpha_190300():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha190300))
    with patch("builtins.open", m):
        AvlDesvFpha.set_version("19.3")
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tabela is not None


def test_versao_avl_desvfpha_190300():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha190300))
    with patch("builtins.open", m):
        AvlDesvFpha.set_version("19.3")
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.versao == "19.3"


def test_data_estudo_avl_desvfpha_190300():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha190300))
    with patch("builtins.open", m):
        AvlDesvFpha.set_version("19.3")
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_tabela_avl_desvfpha_190300():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha190300))
    with patch("builtins.open", m):
        AvlDesvFpha.set_version("19.3")
        log = AvlDesvFpha.read(ARQ_TESTE)
        assert log.tabela.at[0, "estagio"] == 1
        assert log.tabela.at[0, "indice_usina"] == 1
        assert log.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert log.tabela.at[0, "volume_medio_hm3"] == 700.64
        assert log.tabela.at[0, "volume_medio_percentual"] == 86.40
        assert log.tabela.at[0, "vazao_turbinada_m3s"] == 160.50
        assert log.tabela.at[0, "vazao_vertida_m3s"] == 0.0
        assert log.tabela.at[0, "vazao_jusante_m3s"] == 160.0
        assert log.tabela.at[0, "vazao_lateral_usina_m3s"] == 0.0
        assert log.tabela.at[0, "vazao_lateral_posto_m3s"] == 0.0
        assert log.tabela.at[0, "altura_jusante"] == 886.10
        assert log.tabela.at[0, "altura_montante"] == 911.78
        assert log.tabela.at[0, "produtibilidade_especifica"] == 0.008767
        assert log.tabela.at[0, "perdas_hidraulicas"] == 0.0
        assert log.tabela.at[0, "influencia_vertimento_canal_fuga"] == 0
        assert log.tabela.at[0, "afogamento_canal_fuga"] == 0
        assert log.tabela.at[0, "geracao_fph"] == 36.14
        assert log.tabela.at[0, "geracao_pl"] == 36.14
        assert log.tabela.at[0, "geracao_fpha"] == 36.14
        assert log.tabela.at[0, "desvio_absoluto_fph_pl"] == 0.0
        assert log.tabela.at[0, "desvio_percentual_fph_pl"] == -0.01
        assert log.tabela.at[0, "desvio_absoluto_fph_fpha"] == 0.0
        assert log.tabela.at[0, "desvio_percentual_fph_fpha"] == -0.01


def test_eq_avl_desvfpha_190300():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha190300))
    with patch("builtins.open", m):
        AvlDesvFpha.set_version("19.3")
        log1 = AvlDesvFpha.read(ARQ_TESTE)
        log2 = AvlDesvFpha.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_avl_desvfpha_190300():
    m: MagicMock = mock_open(read_data="".join(MockAvlDesvfpha190300))
    with patch("builtins.open", m):
        AvlDesvFpha.set_version("19.3")
        log1 = AvlDesvFpha.read(ARQ_TESTE)
        log2 = AvlDesvFpha.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
