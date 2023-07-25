from idessem.dessem.uch import Uch
from idessem.dessem.modelos.uch import (
    UchOpcaoPadrao,
    UchOpcaoUsina,
    UchOpcaoPadraoData,
    UchTonToffUnidade,
    UchTonToffConjunto,
    UchTonToffUsina,
    UchGminGmaxUnidade,
    UchQturminQturmaxUnidade,
    UchCondicaoInicialUnidade,
)
import pandas as pd  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.uch import (
    MockUch,
    MockUchOpcaoPadrao,
    MockUchOpcaoUsina,
    MockUchOpcaoPadraoData,
    MockUchTonToffUnidade,
    MockUchTonToffConjunto,
    MockUchTonToffUsina,
    MockUchGminGmaxUnidade,
    MockUchQturminQturmaxUnidade,
    MockUchCondicaoInicialUnidade,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_uch():
    m: MagicMock = mock_open(read_data="".join(MockUch))
    with patch("builtins.open", m):
        uch = Uch.read(ARQ_TESTE)
        assert uch.opcao_padrao is not None
        assert uch.opcao_padrao_data is None
        assert uch.opcao_usina() is not None
        assert uch.ton_toff_unidade() is None
        assert uch.ton_toff_conjunto() is None
        assert uch.ton_toff_usina() is not None
        assert uch.gmin_gmax_unidade() is not None
        assert uch.qturmin_qturmax_unidade() is None
        assert uch.condicao_inicial_unidade() is not None


def test_registro_uch_opcao_padrao():
    m: MagicMock = mock_open(read_data="".join(MockUchOpcaoPadrao))
    r = UchOpcaoPadrao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1]
    assert r.considera_uch == 1
    r.considera_uch = 0
    assert r.considera_uch == 0


def test_registro_uch_opcao_usina():
    m: MagicMock = mock_open(read_data="".join(MockUchOpcaoUsina))
    r = UchOpcaoUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [2, 1]
    assert r.codigo_usina == 2
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.considera_uch_usina == 1
    r.considera_uch_usina = 0
    assert r.considera_uch_usina == 0


def test_registro_uch_opcao_padrao_data():
    m: MagicMock = mock_open(read_data="".join(MockUchOpcaoPadraoData))
    r = UchOpcaoPadraoData()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [31, 0, 0, 31, 23, 1]
    assert r.dia_inicial == 31
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial == 0
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == 31
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final == 23
    r.hora_final = 0
    assert r.hora_final == 0
    assert r.meia_hora_final == 1
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1


def test_registro_uch_ton_toff_unidade():
    m: MagicMock = mock_open(read_data="".join(MockUchTonToffUnidade))
    r = UchTonToffUnidade()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 2, 1, 5, 10]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_conjunto == 2
    r.codigo_conjunto = 0
    assert r.codigo_conjunto == 0
    assert r.codigo_unidade == 1
    r.codigo_unidade = 0
    assert r.codigo_unidade == 0
    assert r.tempo_minimo_ligada == 5
    r.tempo_minimo_ligada = 0
    assert r.tempo_minimo_ligada == 0
    assert r.tempo_minimo_desligada == 10
    r.tempo_minimo_desligada = 0
    assert r.tempo_minimo_desligada == 0


def test_registro_uch_ton_toff_conjunto():
    m: MagicMock = mock_open(read_data="".join(MockUchTonToffConjunto))
    r = UchTonToffConjunto()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [2, 1, 5, 10]
    assert r.codigo_usina == 2
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_conjunto == 1
    r.codigo_conjunto = 0
    assert r.codigo_conjunto == 0
    assert r.tempo_minimo_ligada == 5
    r.tempo_minimo_ligada = 0
    assert r.tempo_minimo_ligada == 0
    assert r.tempo_minimo_desligada == 10
    r.tempo_minimo_desligada = 0
    assert r.tempo_minimo_desligada == 0


def test_registro_uch_ton_toff_usina():
    m: MagicMock = mock_open(read_data="".join(MockUchTonToffUsina))
    r = UchTonToffUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 5, 10]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.tempo_minimo_ligada == 5
    r.tempo_minimo_ligada = 0
    assert r.tempo_minimo_ligada == 0
    assert r.tempo_minimo_desligada == 10
    r.tempo_minimo_desligada = 0
    assert r.tempo_minimo_desligada == 0


def test_registro_ghmin_ghmax_unidade():
    m: MagicMock = mock_open(read_data="".join(MockUchGminGmaxUnidade))
    r = UchGminGmaxUnidade()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 1, 3.5, 23]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_conjunto == 1
    r.codigo_conjunto = 0
    assert r.codigo_conjunto == 0
    assert r.codigo_unidade == 1
    r.codigo_unidade = 0
    assert r.codigo_unidade == 0
    assert r.geracao_minima_unidade == 3.5
    r.geracao_minima_unidade = 0
    assert r.geracao_minima_unidade == 0
    assert r.geracao_maxima_unidade == 23
    r.geracao_maxima_unidade = 0
    assert r.geracao_maxima_unidade == 0


def test_registro_qturmin_qturmax_unidade():
    m: MagicMock = mock_open(read_data="".join(MockUchQturminQturmaxUnidade))
    r = UchQturminQturmaxUnidade()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 1, 100, 200]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_conjunto == 1
    r.codigo_conjunto = 0
    assert r.codigo_conjunto == 0
    assert r.codigo_unidade == 1
    r.codigo_unidade = 0
    assert r.codigo_unidade == 0
    assert r.turbinamento_minimo_unidade == 100
    r.turbinamento_minimo_unidade = 0
    assert r.turbinamento_minimo_unidade == 0
    assert r.turbinamento_maximo_unidade == 200
    r.turbinamento_maximo_unidade = 0
    assert r.turbinamento_maximo_unidade == 0


def test_registro_condicao_inicial_unidade():
    m: MagicMock = mock_open(read_data="".join(MockUchCondicaoInicialUnidade))
    r = UchCondicaoInicialUnidade()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [2, 3, 1, 0, 5, 0, 0]
    assert r.codigo_usina == 2
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_conjunto == 3
    r.codigo_conjunto = 0
    assert r.codigo_conjunto == 0
    assert r.codigo_unidade == 1
    r.codigo_unidade = 0
    assert r.codigo_unidade == 0
    assert r.status_inicial == 0
    r.status_inicial = -1
    assert r.status_inicial == 0 - 1
    assert r.geracao_inicial_unidade == 0
    r.geracao_inicial_unidade = -1
    assert r.geracao_inicial_unidade == -1
    assert r.turbinamento_inicial_unidade == 0
    r.turbinamento_inicial_unidade = -1
    assert r.turbinamento_inicial_unidade == -1


def test_df_uch_opcao_usina():
    m: MagicMock = mock_open(read_data="".join(MockUch))
    with patch("builtins.open", m):
        uch = Uch.read(ARQ_TESTE)
        df_uch = uch.opcao_usina(df=True)
        assert df_uch.at[2, "codigo_usina"] == 1
        assert df_uch.at[2, "considera_uch_usina"] == 4


def test_df_uch_ton_toff_usina():
    m: MagicMock = mock_open(read_data="".join(MockUch))
    with patch("builtins.open", m):
        uch = Uch.read(ARQ_TESTE)
        df_uch = uch.ton_toff_usina(df=True)
        assert df_uch.at[2, "codigo_usina"] == 4
        assert df_uch.at[2, "tempo_minimo_ligada"] == 5
        assert df_uch.at[2, "tempo_minimo_desligada"] == 5


def test_df_uch_gmin_gmax_unidade():
    m: MagicMock = mock_open(read_data="".join(MockUch))
    with patch("builtins.open", m):
        uch = Uch.read(ARQ_TESTE)
        df_uch = uch.gmin_gmax_unidade(df=True)
        assert df_uch.at[2, "codigo_usina"] == 2
        assert df_uch.at[2, "codigo_conjunto"] == 1
        assert df_uch.at[2, "codigo_unidade"] == 1
        assert df_uch.at[2, "geracao_minima_unidade"] == 3
        assert df_uch.at[2, "geracao_maxima_unidade"] == 12.5


def test_df_uch_condicao_inicial_unidade():
    m: MagicMock = mock_open(read_data="".join(MockUch))
    with patch("builtins.open", m):
        uch = Uch.read(ARQ_TESTE)
        df_uch = uch.condicao_inicial_unidade(df=True)
        assert df_uch.at[2, "codigo_usina"] == 2
        assert df_uch.at[2, "codigo_conjunto"] == 1
        assert df_uch.at[2, "codigo_unidade"] == 1
        assert df_uch.at[2, "status_inicial"] == 0
        assert df_uch.at[2, "tempo_permanencia_unidade"] == 5
        assert df_uch.at[2, "geracao_inicial_unidade"] == 0
        assert df_uch.at[2, "turbinamento_inicial_unidade"] == 0


# def test_df_polinjus_hidreletrica_curvajusante_polinomio():
#     m: MagicMock = mock_open(read_data="".join(MockPolinjus))
#     with patch("builtins.open", m):
#         polinjus = Polinjus.read(ARQ_TESTE)
#         df_curvajusante_polinomio = (
#             polinjus.hidreletrica_curvajusante_polinomio(df=True)
#         )
#         assert df_curvajusante_polinomio.at[2, "codigo_usina"] == 1
#         assert df_curvajusante_polinomio.at[2, "indice_familia"] == 3
#         assert df_curvajusante_polinomio.at[2, "numero_polinomios"] == 3


# def test_df_polinjus_hidreletrica_curvajusante_polinomio_segmento():
#     m: MagicMock = mock_open(read_data="".join(MockPolinjus))
#     with patch("builtins.open", m):
#         polinjus = Polinjus.read(ARQ_TESTE)
#         df_curvajusante_polinomio_segmento = (
#             polinjus.hidreletrica_curvajusante_polinomio_segmento(df=True)
#         )
#         assert df_curvajusante_polinomio_segmento.at[2, "codigo_usina"] == 1
#         assert df_curvajusante_polinomio_segmento.at[2, "indice_familia"] == 2
#         assert (
#             df_curvajusante_polinomio_segmento.at[2, "indice_polinomio"] == 1
#         )
#         assert (
#             df_curvajusante_polinomio_segmento.at[
#                 2, "limite_inferior_vazao_jusante"
#             ]
#             == 0.0
#         )
#         assert (
#             df_curvajusante_polinomio_segmento.at[
#                 2, "limite_superior_vazao_jusante"
#             ]
#             == 123.055
#         )
#         assert (
#             df_curvajusante_polinomio_segmento.at[2, "coeficiente_a0"] == 885.4
#         )
#         assert (
#             df_curvajusante_polinomio_segmento.at[2, "coeficiente_a1"]
#             == 0.002226482
#         )
#         assert (
#             df_curvajusante_polinomio_segmento.at[2, "coeficiente_a2"]
#             == 7.226778e-06
#         )
#         assert (
#             df_curvajusante_polinomio_segmento.at[2, "coeficiente_a3"]
#             == -4.675277e-07
#         )
#         assert (
#             df_curvajusante_polinomio_segmento.at[2, "coeficiente_a4"]
#             == 2.806664e-09
#         )


# def test_df_polinjus_hidreletrica_curvajusante_afogamentoexplicito_usina():
#     m: MagicMock = mock_open(read_data="".join(MockPolinjus))
#     with patch("builtins.open", m):
#         polinjus = Polinjus.read(ARQ_TESTE)
#         df_curvajusante_afogamentoexplicito_usina = (
#             polinjus.hidreletrica_curvajusante_afogamentoexplicito_usina(
#                 df=True
#             )
#         )
#         assert (
#             df_curvajusante_afogamentoexplicito_usina.at[2, "codigo_usina"]
#             == 54
#         )
#         assert (
#             df_curvajusante_afogamentoexplicito_usina.at[
#                 2, "considera_afogamento"
#             ]
#             == "nao"
#         )


def test_eq_uch():
    m: MagicMock = mock_open(read_data="".join(MockUch))
    with patch("builtins.open", m):
        arq1 = Uch.read(ARQ_TESTE)
        arq2 = Uch.read(ARQ_TESTE)
        assert arq1 == arq2


def test_neq_uch():
    m: MagicMock = mock_open(read_data="".join(MockUch))
    with patch("builtins.open", m):
        arq1 = Uch.read(ARQ_TESTE)
        arq2 = Uch.read(ARQ_TESTE)
        arq1.opcao_usina()[0].codigo_usina = -1
        assert arq1 != arq2
