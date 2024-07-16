from idessem.dessem.pdo_eco_usih_conj import PdoEcoUsihConj
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_eco_usih_conj import (
    MockPdoEcoUsihConj,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_eco_usih_conj():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihConj))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihConj.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_eco_usih_conj():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihConj))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihConj.read(ARQ_TESTE)
        assert pdo.versao == "20.3"


def test_data_estudo_pdo_eco_usih_conj():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihConj))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihConj.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=9, day=3)


def test_tabela_pdo_eco_usih_conj():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihConj))
    with patch("builtins.open", m):
        pdo = PdoEcoUsihConj.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "codigo_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert pdo.tabela.at[0, "codigo_conjunto"] == 1
        assert pdo.tabela.at[0, "numero_unidades"] == 2
        assert pdo.tabela.at[0, "potencia_efetiva"] == 23
        assert pdo.tabela.at[0, "vazao_efetiva"] == 107
        assert pdo.tabela.at[0, "altura_efetiva"] == 24.6


def test_eq_pdo_eco_usih_conj():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihConj))
    with patch("builtins.open", m):
        log1 = PdoEcoUsihConj.read(ARQ_TESTE)
        log2 = PdoEcoUsihConj.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_pdo_eco_usih_conj():
    m: MagicMock = mock_open(read_data="".join(MockPdoEcoUsihConj))
    with patch("builtins.open", m):
        log1 = PdoEcoUsihConj.read(ARQ_TESTE)
        log2 = PdoEcoUsihConj.read(ARQ_TESTE)
        log1.tabela.iloc[0, 0] = -1
        assert log1 != log2
