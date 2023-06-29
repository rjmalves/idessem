from idessem.dessem.modelos.renovaveis import (
    EOLICA,
    EOLICABARRA,
    EOLICASUBM,
    EOLICAGERACAO,
)
from idessem.dessem.renovaveis import Renovaveis
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.renovaveis import (
    MockEolica,
    MockEolicaBarra,
    MockEolicaGeracao,
    MockEolicaSubmercado,
    MockRenovaveis,
)

ARQ_TESTE = "./tests/__init__.py"


def test_registro_eolica_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockEolica))
    r = EOLICA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        "A3AREA_AREAL_00260_UHE",
        9999,
        1.0,
        0,
    ]

    assert r.codigo_usina == 1
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.nome_usina == "A3AREA_AREAL_00260_UHE"
    r.nome_usina = "TESTE"
    assert r.nome_usina == "TESTE"
    assert r.potencia_maxima == 9999
    r.potencia_maxima = 1
    assert r.potencia_maxima == 1
    assert r.fator_capacidade == 1.0
    r.fator_capacidade = 0.5
    assert r.fator_capacidade == 0.5
    assert r.constrained_off == 0
    r.constrained_off = 1
    assert r.constrained_off == 1


def test_registro_eolicabarra_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockEolicaBarra))
    r = EOLICABARRA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [3, 286]

    assert r.codigo_usina == 3
    r.codigo_usina = 2
    assert r.codigo_usina == 2
    assert r.codigo_barra == 286
    r.codigo_barra = 50
    assert r.codigo_barra == 50


def test_registro_eolicasubmercado_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockEolicaSubmercado))
    r = EOLICASUBM()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, "SE"]

    assert r.codigo_usina == 1
    r.codigo_usina = 2
    assert r.codigo_usina == 2
    assert r.submercado == "SE"
    r.submercado = "S"
    assert r.submercado == "S"


def test_registro_eolicageracao_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockEolicaGeracao))
    r = EOLICAGERACAO()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 12, 0, 0, 12, 13, 0, 2]

    assert r.codigo_usina == 1
    r.codigo_usina = 2
    assert r.codigo_usina == 2
    assert r.dia_inicio == 12
    r.dia_inicio = 1
    assert r.dia_inicio == 1
    assert r.hora_inicio == 0
    r.hora_inicio = 1
    assert r.hora_inicio == 1
    assert r.meia_hora_inicio == 0
    r.meia_hora_inicio = 1
    assert r.meia_hora_inicio == 1
    assert r.dia_fim == 12
    r.dia_fim = 1
    assert r.dia_fim == 1
    assert r.hora_fim == 13
    r.hora_fim = 12
    assert r.hora_fim == 12
    assert r.meia_hora_fim == 0
    r.meia_hora_fim = 1
    assert r.meia_hora_fim == 1
    assert r.geracao == 2
    r.geracao = 1
    assert r.geracao == 1


def test_campos_nao_encontrados_renovaveis():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Renovaveis.read("")
    assert d.eolica() is None
    assert d.eolicabarra() is None
    assert d.eolicasubm() is None
    assert d.eolica_geracao() is None


def test_campos_nao_encontrados_renovaveis():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Renovaveis.read("")
    assert d.eolica() is None
    assert d.eolicabarra() is None
    assert d.eolicasubm() is None
    assert d.eolica_geracao() is None


def test_campos_encontrados_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        d = Renovaveis.read(ARQ_TESTE)
    assert d.eolica() is not None
    assert d.eolicabarra() is not None
    assert d.eolicasubm() is not None
    assert d.eolica_geracao() is not None


def test_eq_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        d1 = Renovaveis.read(ARQ_TESTE)
        d2 = Renovaveis.read(ARQ_TESTE)
        assert d1 == d2


def test_neq_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        d1 = Renovaveis.read(ARQ_TESTE)
        d2 = Renovaveis.read(ARQ_TESTE)
        d2.eolica()[0].codigo_usina = -1
        assert d1 != d2


def test_leitura_escrita_renovaveis():
    m_leitura: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m_leitura):
        d1 = Renovaveis.read(ARQ_TESTE)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write(ARQ_TESTE)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(2, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Renovaveis.read(ARQ_TESTE)
        assert d1 == d2
