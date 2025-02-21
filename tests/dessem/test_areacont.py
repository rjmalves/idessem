# Rotinas de testes associadas ao arquivo areacont.dat do DESSEM
from unittest.mock import MagicMock, patch

import pandas as pd

from idessem.dessem.areacont import Areacont
from idessem.dessem.modelos.areacont import BlocoArea, BlocoUsina
from tests.mocks.arquivos.areacont import (
    MockAreacont,
    MockBlocoArea,
    MockBlocoUsina,
)
from tests.mocks.mock_open import mock_open

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_areacont():
    m: MagicMock = mock_open(read_data="".join(MockAreacont))
    with patch("builtins.open", m):
        arq = Areacont.read(ARQ_TESTE)
        assert arq.area is not None
        assert arq.usina is not None


def test_atributos_nao_encontrados_areacont():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        arq = Areacont.read(ARQ_TESTE)
        assert arq.area is None
        assert arq.usina is None


# Bloco AREA
def test_eq_blocoarea():
    m: MagicMock = mock_open(read_data="".join(MockBlocoArea))
    b1 = BlocoArea()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoArea()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocoarea():
    m: MagicMock = mock_open(read_data="".join(MockBlocoArea))
    b1 = BlocoArea()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoArea()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[1].iloc[0, 0] = -1
    assert b1 != b2


def test_bloco_area():
    m: MagicMock = mock_open(read_data="".join(MockBlocoArea))
    b = BlocoArea()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[1].at[0, "codigo_area"] == 1
    assert (
        b.data[1].at[0, "nome_area"] == "FOLGA FPM - RESERVA DE POTENCIA DO SIN"
    )


# Bloco USINA
def test_eq_blocousina():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUsina))
    b1 = BlocoUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocousina():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUsina))
    b1 = BlocoUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data[1].iloc[0, 0] = -1
    assert b1 != b2


def test_bloco_usina():
    m: MagicMock = mock_open(read_data="".join(MockBlocoUsina))
    b = BlocoUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[1].at[0, "codigo_area"] == 1
    assert pd.isna(b.data[1].at[0, "codigo_conjunto"])
    assert b.data[1].at[0, "tipo_componente"] == "H"
    assert b.data[1].at[0, "codigo_componente"] == "261"
    assert b.data[1].at[0, "nome_componente"] == "LAJEADO"


def test_blocos():
    m: MagicMock = mock_open(read_data="".join(MockAreacont))
    with patch("builtins.open", m):
        ad = Areacont.read(ARQ_TESTE)

        assert ad.area.at[0, "codigo_area"] == 1
        df = ad.area
        df.at[0, "codigo_area"] = 0
        ad.area = df
        assert ad.area.at[0, "codigo_area"] == 0

        assert ad.usina.at[0, "codigo_area"] == 1
        df = ad.usina
        df.at[0, "codigo_area"] = 0
        ad.usina = df
        assert ad.usina.at[0, "codigo_area"] == 0


def test_leitura_escrita_areacont():
    m_leitura: MagicMock = mock_open(read_data="".join(MockAreacont))
    with patch("builtins.open", m_leitura):
        d1 = Areacont.read(ARQ_TESTE)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write(ARQ_TESTE)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Areacont.read(ARQ_TESTE)
        assert d1 == d2
