# Rotinas de testes associadas ao arquivo operut.dat do DESSEM
from idessem.dessem.modelos.operut import (
    BlocoInitUT,
    BlocoOper,
    BlocoUcTerm,
    BlocoUctPar,
    BlocoPint,
    BlocoRegraNPTV,
    BlocoAvlCmo,
    BlocoCplexLog,
    BlocoUctBusLoc,
    BlocoUctHeurFp,
    BlocoConstDados,
    BlocoAjusteFcf,
    BlocoTolerIlh,
    BlocoCrossover,
    BlocoEngolimento,
    BlocoTrataInviabIlha,
)
from idessem.dessem.operut import Operut
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.operut import (
    MockBlocoInit,
    MockBlocoOper,
    MockOperut,
    MockBlocoUcterm,
    MockBlocoUctpar,
    MockBlocoPint,
    MockBlocoRegraNPTV,
    MockBlocoAvlCmo,
    MockBlocoCplexLog,
    MockBlocoUctBusLoc,
    MockBlocoUctHeurFp,
    MockBlocoConstDados,
    MockBlocoAjusteFcf,
    MockBlocoTolerIlh,
    MockBlocoCrossover,
    MockBlocoEngolimento,
    MockBlocoTrataInviabIlha,
)
import pandas as pd

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_operut():
    m: MagicMock = mock_open(read_data="".join(MockOperut))
    with patch("builtins.open", m):
        op = Operut.read(ARQ_TESTE)
        assert op.condicoes_iniciais is not None
        assert op.limites_e_condicoes_operativas is not None
        assert op.uctpar is not None
        assert op.ucterm is not None
        assert op.pint is not None
        assert op.regranptv is not None
        assert op.avlcmo is not None
        assert op.cplexlog is not None
        assert op.uctbusloc is None
        assert op.uctheurfp is None
        assert op.constdados is None
        assert op.ajustefcf is None
        assert op.tolerilh is None
        assert op.crossover is None
        assert op.engolimento is None
        assert op.tratainviabilha is None


def test_atributos_nao_encontrados_operut():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        op = Operut.read(ARQ_TESTE)
        assert op.condicoes_iniciais is None
        assert op.limites_e_condicoes_operativas is None
        assert op.uctpar is None
        assert op.ucterm is None
        assert op.pint is None
        assert op.regranptv is None
        assert op.avlcmo is None
        assert op.cplexlog is None
        assert op.uctbusloc is None
        assert op.uctheurfp is None
        assert op.constdados is None
        assert op.ajustefcf is None
        assert op.tolerilh is None
        assert op.crossover is None
        assert op.engolimento is None
        assert op.tratainviabilha is None


# Bloco INIT
def test_eq_blocoinit():
    m: MagicMock = mock_open(read_data="".join(MockBlocoInit))
    b1 = BlocoInitUT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoInitUT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocoinit():
    m: MagicMock = mock_open(read_data="".join(MockBlocoInit))
    b1 = BlocoInitUT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoInitUT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[1].iloc[0, 0] = -1
    assert b1 != b2


def test_bloco_init():
    m: MagicMock = mock_open(read_data="".join(MockBlocoInit))
    b = BlocoInitUT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[1].at[0, "indice_usina"] == 1
    assert b.data[1].at[0, "nome_usina"] == "ANGRA 1"
    assert b.data[1].at[0, "indice_unidade_geradora"] == 1
    assert b.data[1].at[0, "estado"] == 1
    assert b.data[1].at[0, "geracao_inicial"] == 582.0
    assert b.data[1].at[0, "tempo_permanencia_estado"] == 1584
    assert b.data[1].at[0, "meia_hora"] == 0
    assert b.data[1].at[0, "rampa_acionamento_desligamento"] == 0
    assert b.data[1].at[0, "titulacao_inicial"] == 1
    assert b.data[1].at[0, "inflexibilidade_titulacao"] == 582.0


# Bloco OPER
def test_eq_blocooper():
    m: MagicMock = mock_open(read_data="".join(MockBlocoOper))
    b1 = BlocoOper()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoOper()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocooper():
    m: MagicMock = mock_open(read_data="".join(MockBlocoOper))
    b1 = BlocoOper()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoOper()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[1].iloc[0, 0] = -1
    assert b1 != b2


def test_bloco_oper():
    m: MagicMock = mock_open(read_data="".join(MockBlocoOper))
    b = BlocoOper()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[1].at[0, "indice_usina"] == 1
    assert b.data[1].at[0, "nome_usina"] == "ANGRA 1"
    assert b.data[1].at[0, "indice_unidade_geradora"] == 1
    assert b.data[1].at[0, "dia_inicial"] == 6
    assert b.data[1].at[0, "hora_inicial"] == 0
    assert b.data[1].at[0, "meia_hora_inicial"] == 0
    assert pd.isna(b.data[1].at[0, "dia_final"])
    assert pd.isna(b.data[1].at[0, "hora_final"])
    assert pd.isna(b.data[1].at[0, "meia_hora_final"])
    assert pd.isna(b.data[1].at[0, "geracao_minima"])
    assert pd.isna(b.data[1].at[0, "geracao_maxima"])
    assert b.data[1].at[0, "custo"] == 31.17


# Bloco UCTERM
def test_eq_blocoucterm():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUcterm))
    b1 = BlocoUcTerm()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUcTerm()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_bloco_ucterm():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUcterm))
    b = BlocoUcTerm()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data == 2


def test_neq_blocoucterm():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUcterm))
    b1 = BlocoUcTerm()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUcTerm()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    assert b1 != b2


# Bloco UCTPAR
def test_eq_blocouctpar():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctpar))
    b1 = BlocoUctPar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUctPar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_bloco_uctpar():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctpar))
    b = BlocoUctPar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data == 2


def test_neq_blocouctpar():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctpar))
    b1 = BlocoUctPar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUctPar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    assert b1 != b2


# Bloco PINT
def test_eq_blocopint():
    m: MagicMock = mock_open(read_data="".join(MockBlocoPint))
    b1 = BlocoPint()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoPint()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocopint():
    m: MagicMock = mock_open(read_data="".join(MockBlocoPint))
    b1 = BlocoPint()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoPint()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    # Especifidade do bloco PINT: todos são iguais
    assert b1 == b2


def test_bloco_pint():
    m: MagicMock = mock_open(read_data="".join(MockBlocoPint))
    b = BlocoPint()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data == "PINT"


# Bloco REGRANPTV
def test_eq_blocoregranptv():
    m: MagicMock = mock_open(read_data="".join(MockBlocoRegraNPTV))
    b1 = BlocoRegraNPTV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoRegraNPTV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocoregranptv():
    m: MagicMock = mock_open(read_data="".join(MockBlocoRegraNPTV))
    b1 = BlocoRegraNPTV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoRegraNPTV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[0] = -1
    assert b1 != b2


def test_bloco_regranptv():
    m: MagicMock = mock_open(read_data="".join(MockBlocoRegraNPTV))
    b = BlocoRegraNPTV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[0] is None
    assert b.data[1] == 1
    assert b.data[2] is None


# Bloco AVLCMO
def test_eq_blocoavlcmo():
    m: MagicMock = mock_open(read_data="".join(MockBlocoAvlCmo))
    b1 = BlocoAvlCmo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoAvlCmo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocoavlcmo():
    m: MagicMock = mock_open(read_data="".join(MockBlocoAvlCmo))
    b1 = BlocoAvlCmo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoAvlCmo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    assert b1 != b2


def test_bloco_avlcmo():
    m: MagicMock = mock_open(read_data="".join(MockBlocoAvlCmo))
    b = BlocoAvlCmo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data == 1


# Bloco CPLEXLOG
def test_eq_blococplexlog():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCplexLog))
    b1 = BlocoCplexLog()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCplexLog()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blococplexlog():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCplexLog))
    b1 = BlocoCplexLog()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCplexLog()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    # Especifidade do bloco CPLEXLOG: todos são iguais
    assert b1 == b2


def test_bloco_cplexlog():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCplexLog))
    b = BlocoCplexLog()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data == "CPLEXLOG"


# Bloco UCTBUSLOC
def test_eq_blocouctbusloc():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctBusLoc))
    b1 = BlocoUctBusLoc()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUctBusLoc()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocouctbusloc():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctBusLoc))
    b1 = BlocoUctBusLoc()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUctBusLoc()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    # Especifidade do bloco UCTBUSLOC: todos são iguais
    assert b1 == b2


def test_bloco_uctbusloc():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctBusLoc))
    b = BlocoUctBusLoc()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data == "UCTBUSLOC"


# Bloco UCTHEURFP
def test_eq_blocouctheurfp():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctHeurFp))
    b1 = BlocoUctHeurFp()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUctHeurFp()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocouctheurfp():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctHeurFp))
    b1 = BlocoUctHeurFp()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUctHeurFp()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[0] = -1
    assert b1 != b2


def test_bloco_uctheurfp():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUctHeurFp))
    b = BlocoUctHeurFp()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[0] == 1
    assert b.data[1] == 100
    assert b.data[2] is None


# Bloco CONSTDADOS
def test_eq_blococonstdados():
    m: MagicMock = mock_open(read_data="".join(MockBlocoConstDados))
    b1 = BlocoConstDados()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoConstDados()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blococonstdados():
    m: MagicMock = mock_open(read_data="".join(MockBlocoConstDados))
    b1 = BlocoConstDados()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoConstDados()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[0] = -1
    assert b1 != b2


def test_bloco_constdados():
    m: MagicMock = mock_open(read_data="".join(MockBlocoConstDados))
    b = BlocoConstDados()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[0] == 0
    assert b.data[1] is None


# Bloco AJUSTEFCF
def test_eq_blocoajustefcf():
    m: MagicMock = mock_open(read_data="".join(MockBlocoAjusteFcf))
    b1 = BlocoAjusteFcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoAjusteFcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocoajustefcf():
    m: MagicMock = mock_open(read_data="".join(MockBlocoAjusteFcf))
    b1 = BlocoAjusteFcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoAjusteFcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[0] = -1
    assert b1 != b2


def test_bloco_ajustefcf():
    m: MagicMock = mock_open(read_data="".join(MockBlocoAjusteFcf))
    b = BlocoAjusteFcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[0] is None
    assert b.data[1] is None
    assert b.data[2] is None


# Bloco TOLERILH
def test_eq_blocotolerilh():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTolerIlh))
    b1 = BlocoTolerIlh()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoTolerIlh()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocotolerilh():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTolerIlh))
    b1 = BlocoTolerIlh()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoTolerIlh()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    assert b1 != b2


def test_bloco_tolerilh():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTolerIlh))
    b = BlocoTolerIlh()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data == 1


# Bloco CROSSOVER
def test_eq_blococrossover():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCrossover))
    b1 = BlocoCrossover()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCrossover()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blococrossover():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCrossover))
    b1 = BlocoCrossover()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoCrossover()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[0] = -1
    assert b1 != b2


def test_bloco_crossover():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCrossover))
    b = BlocoCrossover()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[0] == 0
    assert b.data[1] == 0
    assert b.data[2] == 0
    assert b.data[3] == 0
    assert b.data[4] is None


# Bloco ENGOLIMENTO
def test_eq_blocoengolimento():
    m: MagicMock = mock_open(read_data="".join(MockBlocoEngolimento))
    b1 = BlocoEngolimento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoEngolimento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocoengolimento():
    m: MagicMock = mock_open(read_data="".join(MockBlocoEngolimento))
    b1 = BlocoEngolimento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoEngolimento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    assert b1 != b2


def test_bloco_engolimento():
    m: MagicMock = mock_open(read_data="".join(MockBlocoEngolimento))
    b = BlocoEngolimento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data == 0


# Bloco TRATA_INVIAB_ILHA
def test_eq_blocotratainviabilha():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTrataInviabIlha))
    b1 = BlocoTrataInviabIlha()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoTrataInviabIlha()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocotratainviabilha():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTrataInviabIlha))
    b1 = BlocoTrataInviabIlha()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoTrataInviabIlha()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data = -1
    assert b1 != b2


def test_bloco_tratainviabilha():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTrataInviabIlha))
    b = BlocoTrataInviabIlha()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data == 1


# Leitura e escrita
def test_leitura_escrita_operut():
    m_leitura: MagicMock = mock_open(read_data="".join(MockOperut))
    with patch("builtins.open", m_leitura):
        op1 = Operut.read(ARQ_TESTE)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        op1.write(ARQ_TESTE)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        op2 = Operut.read(ARQ_TESTE)
        assert op1 == op2
