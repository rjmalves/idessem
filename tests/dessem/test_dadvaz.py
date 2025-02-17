from idessem.dessem.modelos.dadvaz import (
    BlocoDataInicioEstudo,
    BlocoDadosHorizonte,
    BlocoVazoes
)
from idessem.dessem.dadvaz import Dadvaz
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dadvaz import (
    MockDadvaz
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_confhd():
    m: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m):
        ad = Dadvaz.read(ARQ_TESTE)
        assert ad.vazoes is not None


def test_atributos_nao_encontrados_confhd():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        ad = Dadvaz.read(ARQ_TESTE)
        assert ad.vazoes is None


def test_eq_confhd():
    m: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m):
        cf1 = Dadvaz.read(ARQ_TESTE)
        cf2 = Dadvaz.read(ARQ_TESTE)
        assert cf1 == cf2


def test_neq_confhd():
    m: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m):
        cf1 = Dadvaz.read(ARQ_TESTE)
        cf2 = Dadvaz.read(ARQ_TESTE)
        print("debug\n",cf2.vazoes)
        cf2.vazoes.iloc[0, 0] = -1
        assert cf1 != cf2


def test_leitura_escrita_confhd():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDadvaz))
    with patch("builtins.open", m_leitura):
        cf1 = Dadvaz.read(ARQ_TESTE)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        cf1.write(ARQ_TESTE)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        cf2 = Dadvaz.read(ARQ_TESTE)
        assert cf1 == cf2