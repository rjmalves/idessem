from idessem.dessem.pdo_oper_uct import PdoOperUct
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.pdo_oper_uct import MockPdoOperUct

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_oper_uct():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUct))
    with patch("builtins.open", m):
        pdo = PdoOperUct.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.tabela is not None


def test_versao_pdo_oper_uct():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUct))
    with patch("builtins.open", m):
        pdo = PdoOperUct.read(ARQ_TESTE)
        assert pdo.versao == "19.0.42"


def test_data_estudo_pdo_oper_uct():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUct))
    with patch("builtins.open", m):
        pdo = PdoOperUct.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=8, day=8)


def test_tabela_pdo_oper_uct():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUct))
    with patch("builtins.open", m):
        pdo = PdoOperUct.read(ARQ_TESTE)

        assert pdo.tabela.at[0, "estagio"] == 1
        assert pdo.tabela.at[0, "indice_usina"] == 1
        assert pdo.tabela.at[0, "unidade"] == 1
        assert pdo.tabela.at[0, "nome_usina"] == "ANGRA 1"
        assert pdo.tabela.at[0, "submercado"] == "SE"
        assert pdo.tabela.at[0, "barra"] == 10
        assert pdo.tabela.at[0, "numero_maximo_oscilacoes"] == 0
        assert pdo.tabela.at[0, "flag_geracao_minima_maxima"] == 0
        assert pdo.tabela.at[0, "geracao_minima"] == 605.00
        assert pdo.tabela.at[0, "geracao_minima_unidade"] == 0
        assert pdo.tabela.at[0, "geracao_maxima"] == 605.00
        assert pdo.tabela.at[0, "geracao_maxima_unidade"] == 640.00
        assert pdo.tabela.at[0, "geracao_minima_acionamento"] == 520.00
        assert pdo.tabela.at[0, "tempo_on"] == 168
        assert pdo.tabela.at[0, "tempo_off"] == 168
        assert pdo.tabela.at[0, "status"] == 1
        assert pdo.tabela.at[0, "geracao"] == 605.00
        assert pdo.tabela.at[0, "tempo"] == 1512.5
        assert pdo.tabela.at[0, "custo_linear"] == 31.17
        assert pdo.tabela.at[0, "custo_partida_unidade"] == 0.00
        assert pdo.tabela.at[0, "cmo"] == 90.02
        assert pdo.tabela.at[0, "cmb"] == 90.03
        assert pdo.tabela.at[0, "variavel_dual"] == 0
        assert pdo.tabela.at[0, "titulacao"] == "Ordem de merito"
        assert pdo.tabela.at[0, "rampa_subida"] == 1000000.00
        assert pdo.tabela.at[0, "rampa_descida"] == 1000000.00
        assert pdo.tabela.at[0, "unidade_equivalente"] == 0
        assert pd.isna(pdo.tabela.at[0, "rampa_transicao"])


def test_eq_pdo_oper_uct():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUct))
    with patch("builtins.open", m):
        pdo1 = PdoOperUct.read(ARQ_TESTE)
        pdo2 = PdoOperUct.read(ARQ_TESTE)
        assert pdo1 == pdo2


def test_neq_pdo_oper_uct():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperUct))
    with patch("builtins.open", m):
        pdo1 = PdoOperUct.read(ARQ_TESTE)
        pdo2 = PdoOperUct.read(ARQ_TESTE)
        pdo1.tabela.iloc[0, 0] = -1
        assert pdo1 != pdo2
