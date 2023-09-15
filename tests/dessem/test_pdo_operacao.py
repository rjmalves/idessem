from idessem.dessem.pdo_operacao import PdoOperacao
from idessem.dessem.modelos.pdo_operacao import (
    BlocoCustos,
    BlocoCortesAtivos,
    BlocoDiscretizacaoTempo,
)
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.pdo_operacao import (
    MockPdoOperacao,
    MockBlocoCustosOperacao,
    MockBlocoCortesAtivos,
    MockBlocoDiscretizacaoTempo,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_pdo_operacao():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperacao))
    with patch("builtins.open", m):
        pdo = PdoOperacao.read(ARQ_TESTE)
        assert pdo.versao is not None
        assert pdo.data_estudo is not None
        assert pdo.custos_operacao is not None
        assert pdo.cortes_ativos is not None
        assert pdo.discretizacao is not None


def test_atributos_naoencontrados_pdo_operacao():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        pdo = PdoOperacao.read(ARQ_TESTE)
        assert pdo.versao is None
        assert pdo.data_estudo is None
        assert pdo.custos_operacao is None
        assert pdo.cortes_ativos is None
        assert pdo.discretizacao is None


def test_versao_pdo_operacao():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperacao))
    with patch("builtins.open", m):
        pdo = PdoOperacao.read(ARQ_TESTE)
        assert pdo.versao == "19.4.3"


def test_data_estudo_pdo_operacao():
    m: MagicMock = mock_open(read_data="".join(MockPdoOperacao))
    with patch("builtins.open", m):
        pdo = PdoOperacao.read(ARQ_TESTE)
        assert pdo.data_estudo == datetime(year=2022, month=8, day=1)


def test_eq_blocodiscretizacao():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDiscretizacaoTempo))
    b1 = BlocoDiscretizacaoTempo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoDiscretizacaoTempo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocodiscretizacao():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDiscretizacaoTempo))
    b1 = BlocoDiscretizacaoTempo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoDiscretizacaoTempo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data.iloc[0, 0] = -1
    assert b1 != b2


def test_blocodiscretizacao():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDiscretizacaoTempo))
    bloco = BlocoDiscretizacaoTempo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            bloco.read(fp)
        assert bloco.data.at[0, "estagio"] == 1
        assert bloco.data.at[0, "data_inicial"] == datetime(
            year=2022, month=8, day=1, hour=0, minute=0
        )
        assert bloco.data.at[0, "data_final"] == datetime(
            year=2022, month=8, day=1, hour=0, minute=30
        )
        assert bloco.data.at[0, "duracao"] == 0.5


def test_eq_blococustos():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCustosOperacao))
    b1 = BlocoCustos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCustos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blococustos():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCustosOperacao))
    b1 = BlocoCustos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCustos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data.iloc[0, 0] = -1
    assert b1 != b2


def test_blococustos():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCustosOperacao))
    bloco = BlocoCustos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            bloco.read(fp)
        assert bloco.data.at[0, "estagio"] == 1
        assert bloco.data.at[0, "custo_presente"] == 310.3559170
        assert bloco.data.at[0, "custo_futuro"] == 0.0


def test_eq_blococortesativos():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCortesAtivos))
    b1 = BlocoCortesAtivos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCortesAtivos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blococortesativos():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCortesAtivos))
    b1 = BlocoCortesAtivos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCortesAtivos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data.iloc[0, 0] = -1
    assert b1 != b2


def test_blococortesativos():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCortesAtivos))
    bloco = BlocoCortesAtivos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            bloco.read(fp)
        assert bloco.data.at[29, "indice_corte"] == 30
        assert bloco.data.at[29, "multiplicador"] == 0.45692382
