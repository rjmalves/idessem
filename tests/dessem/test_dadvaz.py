from datetime import datetime
from unittest.mock import MagicMock, patch

from idessem.dessem.dadvaz import Dadvaz
from idessem.dessem.modelos.dadvaz import (
    BlocoDadosHorizonte,
    BlocoDataInicioEstudo,
    BlocoVazoes,
)
from tests.mocks.arquivos.dadvaz import (
    MockBlocoDadosHorizonte,
    MockBlocoDataInicioEstudo,
    MockBlocoVazoes,
    MockDadvaz,
)
from tests.mocks.mock_open import mock_open

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_dadvaz():
    m: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m):
        ad = Dadvaz.read(ARQ_TESTE)
        assert ad.vazoes is not None
        assert ad.data_inicio is not None
        assert ad.dia_semana_inicial is not None
        assert ad.semana_acoplamento_fcf is not None
        assert ad.numero_semanas is not None
        assert ad.considera_periodo_simulacao is not None


def test_atributos_nao_encontrados_dadvaz():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        ad = Dadvaz.read(ARQ_TESTE)
        assert ad.vazoes is None
        assert ad.data_inicio is None
        assert ad.dia_semana_inicial is None
        assert ad.semana_acoplamento_fcf is None
        assert ad.numero_semanas is None
        assert ad.considera_periodo_simulacao is None


def test_bloco_data_inicio_estudo():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDataInicioEstudo))
    b = BlocoDataInicioEstudo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data == [datetime(2022, 8, 11, 0)]
    assert b.data_inicio == datetime(2022, 8, 11, 0)
    b.data_inicio = datetime(2022, 8, 12, 0)
    assert b.data_inicio == datetime(2022, 8, 12, 0)


def test_bloco_dados_horizonte():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDadosHorizonte))
    b = BlocoDadosHorizonte()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.semana_acoplamento_fcf == 1
    b.semana_acoplamento_fcf = 0
    assert b.semana_acoplamento_fcf == 0
    assert b.numero_semanas == 1
    b.numero_semanas = 0
    assert b.numero_semanas == 0
    assert b.considera_periodo_simulacao == 0
    b.considera_periodo_simulacao = 0
    assert b.considera_periodo_simulacao == 0
    assert b.dia_semana_inicial == 6
    b.dia_semana_inicial = 0
    assert b.dia_semana_inicial == 0

def test_blocos():
    m: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m):
        ad = Dadvaz.read(ARQ_TESTE)
        assert ad.data_inicio == datetime(2022, 8, 11, 0)
        ad.data_inicio = datetime(2022, 8, 12, 0)
        assert ad.data_inicio == datetime(2022, 8, 12, 0)
        assert ad.semana_acoplamento_fcf == 1
        ad.semana_acoplamento_fcf = 0
        assert ad.semana_acoplamento_fcf == 0
        assert ad.numero_semanas == 1
        ad.numero_semanas = 0
        assert ad.numero_semanas == 0
        assert ad.considera_periodo_simulacao == 0
        ad.considera_periodo_simulacao = 1
        assert ad.considera_periodo_simulacao == 1
        assert ad.dia_semana_inicial == 6
        ad.dia_semana_inicial = 0
        assert ad.dia_semana_inicial == 0
        assert ad.vazoes.at[0,"codigo_usina"] == 1
        df = ad.vazoes 
        df.at[0,"codigo_usina"] = 0
        ad.vazoes = df 
        assert ad.vazoes.at[0,"codigo_usina"] == 0

def test_bloco_vazoes():
    m: MagicMock = mock_open(read_data="".join(MockBlocoVazoes))
    b = BlocoVazoes()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.at[0, "codigo_usina"] == 1
    assert b.data.at[0, "nome_usina"] == "CAMARGOS"
    assert b.data.at[0, "tipo_dado"] == 1
    assert b.data.at[0, "dia_inicial"] == 11
    assert b.data.at[0, "hora_inicial"] is None
    assert b.data.at[0, "meia_hora_inicial"] is None
    assert b.data.at[0, "dia_final"] == "F"
    assert b.data.at[0, "hora_final"] is None
    assert b.data.at[0, "meia_hora_final"] is None
    assert b.data.at[0, "vazao"] == 45


def test_eq_dadvaz():
    m: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m):
        cf1 = Dadvaz.read(ARQ_TESTE)
        cf2 = Dadvaz.read(ARQ_TESTE)
        assert cf1 == cf2


def test_neq_dadvaz():
    m: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m):
        cf1 = Dadvaz.read(ARQ_TESTE)
        cf2 = Dadvaz.read(ARQ_TESTE)
        cf2.vazoes.iloc[0, 0] = -1
        assert cf1 != cf2


def test_leitura_escrita_dadvaz():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m_leitura):
        cf1 = Dadvaz.read(ARQ_TESTE)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        cf1.write(ARQ_TESTE)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [chamadas[i].args[0] for i in range(1, len(chamadas) - 1)]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        cf2 = Dadvaz.read(ARQ_TESTE)
        assert cf1 == cf2
