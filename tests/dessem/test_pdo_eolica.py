from idessem.dessem.pdo_eolica import PdoEolica
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_eolica import MockPdoEolica

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_eolica():
    m: MagicMock = mock_open(read_data="".join(MockPdoEolica))
    with patch("builtins.open", m):
        pdo = PdoEolica.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_eolica():
    m: MagicMock = mock_open(read_data="".join(MockPdoEolica))
    with patch("builtins.open", m):
        pdo = PdoEolica.read(ARQ_TESTE)
        assert pdo.versao == "19.4.3"


def test_data_estudo_pdo_eolica():
    m: MagicMock = mock_open(read_data="".join(MockPdoEolica))
    with patch("builtins.open", m):
        pdo = PdoEolica.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_pdo_eolica():
    m: MagicMock = mock_open(read_data="".join(MockPdoEolica))
    with patch("builtins.open", m):
        pdo = PdoEolica.read(ARQ_TESTE)
        assert pdo.tabela.at[1, "estagio"] == 1
        assert pdo.tabela.at[1, "codigo_usina"] == 2
        assert pdo.tabela.at[1, "nome_usina"] == "A3BRAC_BRACO"
        assert pdo.tabela.at[1, "barra"] == 274
        assert pdo.tabela.at[1, "submercado"] == "SE"
        assert pdo.tabela.at[1, "potencia"] == 9999.00
        assert pdo.tabela.at[1, "fator_de_capacidade"] == 1
        assert pdo.tabela.at[1, "geracao_pre_definida"] == 4
        assert pdo.tabela.at[1, "geracao"] == 4


def test_eq_pdo_eolica():
    m: MagicMock = mock_open(read_data="".join(MockPdoEolica))
    with patch("builtins.open", m):
        pdo1 = PdoEolica.read(ARQ_TESTE)
        pdo2 = PdoEolica.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_eolica():
    m: MagicMock = mock_open(read_data="".join(MockPdoEolica))
    with patch("builtins.open", m):
        pdo1 = PdoEolica.read(ARQ_TESTE)
        pdo2 = PdoEolica.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
