from idessem.dessem.pdo_oper_titulacao_contratos import (
    PdoOperTitulacaoContratos,
)
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.pdo_oper_titulacao_contratos import (
    MockPdoOperTitulacaoContratos,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_oper_titulacao_contratos():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoContratos))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoContratos.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_oper_titulacao_contratos():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoContratos))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoContratos.read(ARQ_TESTE)
        assert pdo.versao == "20.0.11"


def test_data_estudo_pdo_oper_titulacao_contratos():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoContratos))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoContratos.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2025, month=1, day=24)


def test_tabela_pdo_oper_titulacao_contratos():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoContratos))
    with patch("builtins.open", m):
        pdo = PdoOperTitulacaoContratos.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "tipo_contrato"] == "CI"
        assert pdo.tabela.at[0, "codigo_contrato"] == 65
        assert pdo.tabela.at[0, "nome_contrato"] == "TKUTA2-I"
        assert pdo.tabela.at[0, "codigo_barra"] is None
        assert pdo.tabela.at[0, "codigo_submercado"] is None
        assert pdo.tabela.at[0, "titulacao_inflexibilidade"] == 146.00
        assert pdo.tabela.at[0, "custo_contrato"] == 0
        assert pdo.tabela.at[0, "geracao"] == 146.00
        assert pdo.tabela.at[0, "cmo"] == 59.93
        assert pdo.tabela.at[0, "cmb"] == 63.42
        assert pdo.tabela.at[0, "ordem_merito_total"] == ""
        assert pdo.tabela.at[0, "titulacao"] == "Inflexibilidade"


def test_eq_pdo_oper_titulacao_contratos():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoContratos))
    with patch("builtins.open", m):
        pdo1 = PdoOperTitulacaoContratos.read(ARQ_TESTE)
        pdo2 = PdoOperTitulacaoContratos.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_oper_titulacao_contratos():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperTitulacaoContratos))
    with patch("builtins.open", m):
        pdo1 = PdoOperTitulacaoContratos.read(ARQ_TESTE)
        pdo2 = PdoOperTitulacaoContratos.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
