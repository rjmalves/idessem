from idessem.dessem.pdo_oper_titulacao_usinas import PdoOperTitulacaoUsinas
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_oper_titulacao_usinas import (
    MockPdoOperTitulacaoUsinas,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_oper_titulacao_usinas():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoUsinas))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoUsinas.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_oper_titulacao_usinas():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoUsinas))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoUsinas.read(ARQ_TESTE)
        assert pdo.versao == "20.0.11"


def test_data_estudo_pdo_oper_titulacao_usinas():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoUsinas))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoUsinas.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2025, month=1, day=24)


def test_tabela_pdo_oper_titulacao_usinas():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoUsinas))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoUsinas.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "codigo_usina"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "ANGRA 1"
        assert pdo.tabela.at[0, "nome_submercado"] == "SE"
        assert pdo.tabela.at[0, "geracao"] == 0
        assert pdo.tabela.at[0, "titulacao_ordem_merito"] == 0
        assert pdo.tabela.at[0, "titulacao_inflexibilidade"] == 0
        assert pdo.tabela.at[0, "geracao_unit_commitment"] == 0
        assert pdo.tabela.at[0, "geracao_tempo_off"] == 0
        assert pdo.tabela.at[0, "ordem_merito_total"] == ""


def test_eq_pdo_oper_titulacao_usinas():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoUsinas))
    with patch("builtins.open", m):
        pdo1 = PdoOperTitulacaoUsinas.read(ARQ_TESTE)
        pdo2 = PdoOperTitulacaoUsinas.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_oper_titulacao_usinas():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoUsinas))
    with patch("builtins.open", m):
        pdo1 = PdoOperTitulacaoUsinas.read(ARQ_TESTE)
        pdo2 = PdoOperTitulacaoUsinas.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
