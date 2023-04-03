# Rotinas de testes associadas ao arquivo operut.dat do DESSEM
from idessem.dessem.modelos.operut import BlocoInitUT, BlocoOper
from idessem.dessem.operut import Operut
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.operut import (
    MockBlocoInit,
    MockBlocoOper,
    MockOperut,
)
import pandas as pd


def test_atributos_encontrados_operut():
    m: MagicMock = mock_open(read_data="".join(MockOperut))
    with patch("builtins.open", m):
        op = Operut.le_arquivo("")
        assert op.condicoes_iniciais is not None
        assert op.limites_e_condicoes_operativas is not None


def test_atributos_nao_encontrados_operut():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        op = Operut.le_arquivo("")
        assert op.condicoes_iniciais is None
        assert op.limites_e_condicoes_operativas is None


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


def test_leitura_escrita_operut():
    m_leitura: MagicMock = mock_open(read_data="".join(MockOperut))
    with patch("builtins.open", m_leitura):
        op1 = Operut.le_arquivo("")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        op1.escreve_arquivo("", "")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(2, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        op2 = Operut.le_arquivo("")
        assert op1 == op2
