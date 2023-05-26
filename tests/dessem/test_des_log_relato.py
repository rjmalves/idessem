from idessem.dessem.des_log_relato import DesLogRelato
from idessem.dessem.modelos.des_log_relato import (
    BlocoTempoProcessamento,
    BlocoVariaveisOtimizacao,
)
from datetime import datetime, timedelta
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.des_log_relato import (
    MockDesLogRelato,
    MockBlocoVariaveisOtimizacao,
    MockBlocoTempoProcessamento,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_des_log_relato():
    m: MagicMock = mock_open(read_data="".join(MockDesLogRelato))
    with patch("builtins.open", m):
        log = DesLogRelato.read(ARQ_TESTE)
        assert log.versao is not None
        assert log.data_estudo is not None
        assert log.tempo_processamento is not None
        assert log.variaveis_otimizacao is not None


def test_atributos_naoencontrados_des_log_relato():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        log = DesLogRelato.read(ARQ_TESTE)
        assert log.versao is None
        assert log.data_estudo is None
        assert log.tempo_processamento is None
        assert log.variaveis_otimizacao is None


def test_versao_des_log_relato():
    m: MagicMock = mock_open(read_data="".join(MockDesLogRelato))
    with patch("builtins.open", m):
        log = DesLogRelato.read(ARQ_TESTE)
        assert log.versao == "19.3"


def test_data_estudo_des_log_relato():
    m: MagicMock = mock_open(read_data="".join(MockDesLogRelato))
    with patch("builtins.open", m):
        log = DesLogRelato.read(ARQ_TESTE)
        assert log.data_estudo == datetime(year=2022, month=8, day=11)


def test_eq_blocovariaveisotimizacao():
    m: MagicMock = mock_open(read_data="".join(MockBlocoVariaveisOtimizacao))
    b1 = BlocoVariaveisOtimizacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoVariaveisOtimizacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocovariaveisotimizacao():
    m: MagicMock = mock_open(read_data="".join(MockBlocoVariaveisOtimizacao))
    b1 = BlocoVariaveisOtimizacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoVariaveisOtimizacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data.iloc[0, 0] = -1
    assert b1 != b2


def test_blocovariaveisotimizacao():
    m: MagicMock = mock_open(read_data="".join(MockBlocoVariaveisOtimizacao))
    bloco = BlocoVariaveisOtimizacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            bloco.read(fp)

        assert bloco.data.at[0, "valor"] == 54689900.00685
        assert bloco.data.at[1, "valor"] == 54689882.95697
        assert bloco.data.at[2, "valor"] == 44045.29595
        assert bloco.data.at[3, "valor"] == 54645837.66101
        assert bloco.data.at[4, "valor"] == 0.00000
        assert bloco.data.at[5, "valor"] == 17.04995
        assert bloco.data.at[6, "valor"] == 0.00000
        assert bloco.data.at[7, "valor"] == 0.5037


def test_eq_blocotempoprocessamento():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTempoProcessamento))
    b1 = BlocoTempoProcessamento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoTempoProcessamento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocotempoprocessamento():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTempoProcessamento))
    b1 = BlocoTempoProcessamento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoTempoProcessamento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1 = timedelta(hours=500000)
    assert b1 != b2


def test_blocotempoprocessamento():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTempoProcessamento))
    bloco = BlocoTempoProcessamento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            bloco.read(fp)
        assert bloco.data == timedelta(hours=0, minutes=20, seconds=18)
