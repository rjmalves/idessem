from unittest.mock import MagicMock, patch

from idessem.dessem.desselet import Desselet
from idessem.dessem.modelos.desselet import (
    BlocoCasosBase,
    BlocoCasosModificacao,
)
from tests.mocks.arquivos.desselet import (
    MockBlocoCasoBase,
    MockBlocoCasosModificacao,
    MockDesselet,
)
from tests.mocks.mock_open import mock_open

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_desselet():
    m: MagicMock = mock_open(read_data="".join(MockDesselet))
    with patch("builtins.open", m):
        ad = Desselet.read(ARQ_TESTE)
        assert ad.dados_casos_base is not None
        assert ad.dados_modificacao is not None


def test_atributos_nao_encontrados_desselet():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        ad = Desselet.read(ARQ_TESTE)
        assert ad.dados_casos_base is None
        assert ad.dados_modificacao is None


def test_bloco_caso_base():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCasoBase))
    b = BlocoCasosBase()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.at[0, "indice_caso_base"] == 1
    assert b.data.at[0, "nome_caso_base"] == "leve"
    assert b.data.at[0, "arquivo"] == "leve        .pwf"


def test_bloco_caso_modificacao():
    m: MagicMock = mock_open(read_data="".join(MockBlocoCasosModificacao))
    b = BlocoCasosModificacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.at[0, "codigo_estagio"] == 1
    assert b.data.at[0, "nome_estagio"] == "Estagio01"
    assert b.data.at[0, "ano"] == 2024
    assert b.data.at[0, "mes"] == 6
    assert b.data.at[0, "dia"] == 27
    assert b.data.at[0, "hora"] == 0
    assert b.data.at[0, "minuto"] == 0
    assert b.data.at[0, "duracao_estagio"] == 0.5
    assert b.data.at[0, "indice_caso_base"] == 1
    assert b.data.at[0, "arquivo"] == "pat01.afp"


def test_blocos():
    m: MagicMock = mock_open(read_data="".join(MockDesselet))
    with patch("builtins.open", m):
        ad = Desselet.read(ARQ_TESTE)

        assert ad.dados_casos_base.at[0, "indice_caso_base"] == 1
        df = ad.dados_casos_base
        df.at[0, "indice_caso_base"] = 0
        ad.dados_casos_base = df
        assert ad.dados_casos_base.at[0, "indice_caso_base"] == 0

        assert ad.dados_modificacao.at[0, "codigo_estagio"] == 1
        df = ad.dados_modificacao
        df.at[0, "codigo_estagio"] = 0
        ad.dados_modificacao = df
        assert ad.dados_modificacao.at[0, "codigo_estagio"] == 0


def test_eq_desselet():
    m: MagicMock = mock_open(read_data="".join(MockDesselet))
    with patch("builtins.open", m):
        cf1 = Desselet.read(ARQ_TESTE)
        cf2 = Desselet.read(ARQ_TESTE)
        assert cf1 == cf2


def test_neq_desselet():
    m: MagicMock = mock_open(read_data="".join(MockDesselet))
    with patch("builtins.open", m):
        cf1 = Desselet.read(ARQ_TESTE)
        cf2 = Desselet.read(ARQ_TESTE)
        cf2.dados_casos_base.iloc[0, 0] = -1
        assert cf1 != cf2


def test_leitura_escrita_desselet():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDesselet))
    with patch("builtins.open", m_leitura):
        cf1 = Desselet.read(ARQ_TESTE)
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
        cf2 = Desselet.read(ARQ_TESTE)
        assert cf1 == cf2
