from idessem.dessem.pdo_elev import PdoElev
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_elev import MockPdoElev

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_elev():
    m: MagicMock = mock_open(read_data="".join(MockPdoElev))
    with patch("builtins.open", m):
        pdo = PdoElev.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_elev():
    m: MagicMock = mock_open(read_data="".join(MockPdoElev))
    with patch("builtins.open", m):
        pdo = PdoElev.read(ARQ_TESTE)
        assert pdo.versao == "21.2.1"


def test_data_estudo_pdo_elev():
    m: MagicMock = mock_open(read_data="".join(MockPdoElev))
    with patch("builtins.open", m):
        pdo = PdoElev.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2025, month=11, day=18)


def test_tabela_pdo_elev():
    m: MagicMock = mock_open(read_data="".join(MockPdoElev))
    with patch("builtins.open", m):
        pdo = PdoElev.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "nome_patamar"] == "MEDIA"
        assert pdo.tabela.at[0, "codigo_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "Sta Cecilia"
        assert pdo.tabela.at[0, "nome_submercado"] == "SE"
        assert pdo.tabela.at[0, "bombeamento_minimo"] == 0.0
        assert pdo.tabela.at[0, "bombeamento"] == 118.3
        assert pdo.tabela.at[0, "bombeamento_maximo"] == 160.0
        assert pdo.tabela.at[0, "consumo"] == 23.66


def test_eq_pdo_elev():
    m: MagicMock = mock_open(read_data="".join(MockPdoElev))
    with patch("builtins.open", m):
        pdo1 = PdoElev.read(ARQ_TESTE)
        pdo2 = PdoElev.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_elev():
    m: MagicMock = mock_open(read_data="".join(MockPdoElev))
    with patch("builtins.open", m):
        pdo1 = PdoElev.read(ARQ_TESTE)
        pdo2 = PdoElev.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
