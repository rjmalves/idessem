from idessem.dessem.pdo_oper_usih import PdoOperUsih
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_oper_usih import MockPdoOperUsih

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUsih))
    with patch("builtins.open", m):
        pdo = PdoOperUsih.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUsih))
    with patch("builtins.open", m):
        pdo = PdoOperUsih.read(ARQ_TESTE)
        assert pdo.versao == "21.2.1"


def test_data_estudo_pdo_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUsih))
    with patch("builtins.open", m):
        pdo = PdoOperUsih.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2025, month=11, day=18)


def test_tabela_pdo_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUsih))
    with patch("builtins.open", m):
        pdo = PdoOperUsih.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "patamar"] == 1
        assert pdo.tabela.at[0, "codigo_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert pdo.tabela.at[0, "nome_submercado"] == "SE"
        assert pdo.tabela.at[0, "volume_util_inicial"] == 345.0
        assert pdo.tabela.at[0, "volume_util_inicial_p"] == 51.34
        assert pdo.tabela.at[0, "volume_util_final"] == 345.01
        assert pdo.tabela.at[0, "volume_util_final_p"] == 51.34
        assert pdo.tabela.at[0, "volume_util_maximo"] == 672.0
        assert pdo.tabela.at[0, "vazao_incremental_natural"] == 50.0
        assert pdo.tabela.at[0, "volume_incremental_natural"] == 0.09
        assert pdo.tabela.at[0, "vazao_retirada_para_usos_alternativos"] == 0.2
        assert pdo.tabela.at[0, "volume_retirado_para_usos_alternativos"] == 0.0
        assert pdo.tabela.at[0, "vazao_evaporada"] == 0.08
        assert pdo.tabela.at[0, "volume_evaporado"] == 0.0
        assert pdo.tabela.at[0, "vazao_montante"] == 0.0
        assert pdo.tabela.at[0, "volume_montante"] == 0.0
        assert pdo.tabela.at[0, "vazao_montante_periodos_passados"] == 0.0
        assert pdo.tabela.at[0, "volume_montante_periodos_passados"] == 0.0
        assert pdo.tabela.at[0, "vazao_turbinada"] == 46.64
        assert pdo.tabela.at[0, "vazao_turbinada_maxima"] == 214.0
        assert pdo.tabela.at[0, "engolimento_maximo"] == 209.49
        assert pdo.tabela.at[0, "volume_turbinado"] == 0.08
        assert pdo.tabela.at[0, "vazao_vertida"] == 0.0
        assert pdo.tabela.at[0, "volume_vertido"] == 0.0
        assert pdo.tabela.at[0, "vazao_desviada"] == 0.0
        assert pdo.tabela.at[0, "volume_desviado"] == 0.0
        assert pdo.tabela.at[0, "vazao_bombeada"] == 0.0
        assert pdo.tabela.at[0, "volume_bombeado"] == 0.0
        assert pdo.tabela.at[0, "taxa_enchimento_volume_morto"] == None
        assert pdo.tabela.at[0, "volume_enchimento_volume_morto"] == None
        assert pdo.tabela.at[0, "taxa_descarga_fundo"] == None
        assert pdo.tabela.at[0, "volume_descaga_fundo"] == None
        assert pdo.tabela.at[0, "geracao"] == 9.07
        assert pdo.tabela.at[0, "geracao_maxima"] == 46.0
        assert pdo.tabela.at[0, "geracao_minima"] == 0.0
        assert pdo.tabela.at[0, "potencia_instalada"] == 46.0
        assert pdo.tabela.at[0, "valor_agua"] == 668.85


def test_eq_pdo_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUsih))
    with patch("builtins.open", m):
        pdo1 = PdoOperUsih.read(ARQ_TESTE)
        pdo2 = PdoOperUsih.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUsih))
    with patch("builtins.open", m):
        pdo1 = PdoOperUsih.read(ARQ_TESTE)
        pdo2 = PdoOperUsih.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
