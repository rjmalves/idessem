from idessem.dessem.pdo_oper_tviag_calha import PdoOperTviagCalha
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_oper_tviag_calha import MockPdoOperTviagCalha

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_oper_tviag_calha():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTviagCalha))
    with patch("builtins.open", m):
        pdo = PdoOperTviagCalha.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_oper_tviag_calha():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTviagCalha))
    with patch("builtins.open", m):
        pdo = PdoOperTviagCalha.read(ARQ_TESTE)
        assert pdo.versao == "20.3"


def test_data_estudo_pdo_oper_tviag_calha():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTviagCalha))
    with patch("builtins.open", m):
        pdo = PdoOperTviagCalha.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_pdo_oper_tviag_calha():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTviagCalha))
    with patch("builtins.open", m):
        pdo = PdoOperTviagCalha.read(ARQ_TESTE)
        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "duracao"] == 0.5
        assert pdo.tabela.at[0, "codigo_usina_montante"] == 66
        assert pdo.tabela.at[0, "nome_usina_montante"] == "ITAIPU"
        assert pdo.tabela.at[0, "tipo_elemento_jusante"] == "SECR"
        assert pdo.tabela.at[0, "codigo_elemento_jusante"] == 1
        assert pdo.tabela.at[0, "nome_elemento_jusante"] == "R11"
        assert pdo.tabela.at[0, "tempo_viagem"] == 24.00
        assert pdo.tabela.at[0, "tipo_tempo_viagem"] == "PROPAG"
        assert pdo.tabela.at[0, "tempo_restante"] == 168.0
        assert pdo.tabela.at[0, "percentual_volume_calha"] == 0.00
        assert pdo.tabela.at[0, "volume_calha_hm3"] == 0.00


def test_eq_pdo_oper_tviag_calha():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTviagCalha))
    with patch("builtins.open", m):
        pdo1 = PdoOperTviagCalha.read(ARQ_TESTE)
        pdo2 = PdoOperTviagCalha.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_oper_tviag_calha():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTviagCalha))
    with patch("builtins.open", m):
        pdo1 = PdoOperTviagCalha.read(ARQ_TESTE)
        pdo2 = PdoOperTviagCalha.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
