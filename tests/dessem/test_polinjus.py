from idessem.dessem.polinjus import Polinjus
from idessem.dessem.polinjus import (
    HidreletricaCurvaJusante,
    HidreletricaCurvaJusantePolinomioPorPartes,
    HidreletricaCurvaJusantePolinomioPorPartesSegmento,
    HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
    HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
)
import pandas as pd  # type: ignore
from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.polinjus import (
    MockPolinjus,
    MockHidreletricaCurvaJusante,
    MockHidreletricaCurvaJusantePolinomio,
    MockHidreletricaCurvaJusantePolinomioSegmento,
    MockHidreletricaCurvaJusanteAfogamentoExplicitoUsina,
    MockHidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_polinjus():
    m: MagicMock = mock_open(read_data="".join(MockPolinjus))
    with patch("builtins.open", m):
        polinjus = Polinjus.read(ARQ_TESTE)
        assert polinjus.hidreletrica_curvajusante() is not None
        assert polinjus.hidreletrica_curvajusante_polinomio() is not None
        assert (
            polinjus.hidreletrica_curvajusante_polinomio_segmento() is not None
        )
        assert (
            polinjus.hidreletrica_curvajusante_afogamentoexplicito_usina()
            is not None
        )
        assert (
            polinjus.hidreletrica_curvajusante_afogamentoexplicito_padrao()
            is not None
        )


def test_df_polinjus_hidreletrica_curvajusante():
    m: MagicMock = mock_open(read_data="".join(MockPolinjus))
    with patch("builtins.open", m):
        polinjus = Polinjus.read(ARQ_TESTE)
        df_curvajusante = polinjus.hidreletrica_curvajusante(df=True)
        assert df_curvajusante.at[2, "codigo_usina"] == 1
        assert df_curvajusante.at[2, "indice_familia"] == 3
        assert df_curvajusante.at[2, "nivel_montante_referencia"] == 885.70


def test_registro_polinjus_hidreletrica_curvajusante():
    m: MagicMock = mock_open(read_data="".join(MockHidreletricaCurvaJusante))
    r = HidreletricaCurvaJusante()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 885.3052]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.indice_familia == 1
    r.indice_familia = 0
    assert r.indice_familia == 0
    assert r.nivel_montante_referencia == 885.3052
    r.nivel_montante_referencia = 0
    assert r.nivel_montante_referencia == 0


def test_df_polinjus_hidreletrica_curvajusante_polinomio():
    m: MagicMock = mock_open(read_data="".join(MockPolinjus))
    with patch("builtins.open", m):
        polinjus = Polinjus.read(ARQ_TESTE)
        df_curvajusante_polinomio = (
            polinjus.hidreletrica_curvajusante_polinomio(df=True)
        )
        assert df_curvajusante_polinomio.at[2, "codigo_usina"] == 1
        assert df_curvajusante_polinomio.at[2, "indice_familia"] == 3
        assert df_curvajusante_polinomio.at[2, "numero_polinomios"] == 3


def test_registro_polinjus_hidreletrica_curvajusante_polinomio():
    m: MagicMock = mock_open(
        read_data="".join(MockHidreletricaCurvaJusantePolinomio)
    )
    r = HidreletricaCurvaJusantePolinomioPorPartes()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 2]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.indice_familia == 1
    r.indice_familia = 0
    assert r.indice_familia == 0
    assert r.numero_polinomios == 2
    r.numero_polinomios = 0
    assert r.numero_polinomios == 0


def test_df_polinjus_hidreletrica_curvajusante_polinomio_segmento():
    m: MagicMock = mock_open(read_data="".join(MockPolinjus))
    with patch("builtins.open", m):
        polinjus = Polinjus.read(ARQ_TESTE)
        df_curvajusante_polinomio_segmento = (
            polinjus.hidreletrica_curvajusante_polinomio_segmento(df=True)
        )
        assert df_curvajusante_polinomio_segmento.at[2, "codigo_usina"] == 1
        assert df_curvajusante_polinomio_segmento.at[2, "indice_familia"] == 2
        assert (
            df_curvajusante_polinomio_segmento.at[2, "indice_polinomio"] == 1
        )
        assert (
            df_curvajusante_polinomio_segmento.at[
                2, "limite_inferior_vazao_jusante"
            ]
            == 0.0
        )
        assert (
            df_curvajusante_polinomio_segmento.at[
                2, "limite_superior_vazao_jusante"
            ]
            == 123.055
        )
        assert (
            df_curvajusante_polinomio_segmento.at[2, "coeficiente_a0"] == 885.4
        )
        assert (
            df_curvajusante_polinomio_segmento.at[2, "coeficiente_a1"]
            == 0.002226482
        )
        assert (
            df_curvajusante_polinomio_segmento.at[2, "coeficiente_a2"]
            == 7.226778e-06
        )
        assert (
            df_curvajusante_polinomio_segmento.at[2, "coeficiente_a3"]
            == -4.675277e-07
        )
        assert (
            df_curvajusante_polinomio_segmento.at[2, "coeficiente_a4"]
            == 2.806664e-09
        )


def test_registro_polinjus_hidreletrica_curvajusante_polinomio_segmento():
    m: MagicMock = mock_open(
        read_data="".join(MockHidreletricaCurvaJusantePolinomioSegmento)
    )
    r = HidreletricaCurvaJusantePolinomioPorPartesSegmento()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        1,
        1,
        0,
        408.649,
        0.88530520000000e03,
        -0.31521360000000e-17,
        0.19686530000000e-04,
        -0.25518040000000e-07,
        0.00000000000000e01,
    ]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.indice_familia == 1
    r.indice_familia = 0
    assert r.indice_familia == 0
    assert r.indice_polinomio == 1
    r.indice_polinomio = 0
    assert r.indice_polinomio == 0
    assert r.limite_inferior_vazao_jusante == 0
    r.limite_inferior_vazao_jusante = -1
    assert r.limite_inferior_vazao_jusante == -1
    assert r.limite_superior_vazao_jusante == 408.649
    r.limite_superior_vazao_jusante = -1
    assert r.limite_superior_vazao_jusante == -1

    assert r.coeficiente_a0 == 0.88530520000000e03
    r.coeficiente_a0 = -1
    assert r.coeficiente_a0 == -1
    assert r.coeficiente_a1 == -0.31521360000000e-17
    r.coeficiente_a1 = -1
    assert r.coeficiente_a1 == -1
    assert r.coeficiente_a2 == 0.19686530000000e-04
    r.coeficiente_a2 = -1
    assert r.coeficiente_a2 == -1
    assert r.coeficiente_a3 == -0.25518040000000e-07
    r.coeficiente_a3 = -1
    assert r.coeficiente_a3 == -1
    assert r.coeficiente_a4 == 0.00000000000000e01
    r.coeficiente_a4 = -1
    assert r.coeficiente_a4 == -1


def test_df_polinjus_hidreletrica_curvajusante_afogamentoexplicito_usina():
    m: MagicMock = mock_open(read_data="".join(MockPolinjus))
    with patch("builtins.open", m):
        polinjus = Polinjus.read(ARQ_TESTE)
        df_curvajusante_afogamentoexplicito_usina = (
            polinjus.hidreletrica_curvajusante_afogamentoexplicito_usina(
                df=True
            )
        )
        assert (
            df_curvajusante_afogamentoexplicito_usina.at[2, "codigo_usina"]
            == 54
        )
        assert (
            df_curvajusante_afogamentoexplicito_usina.at[
                2, "considera_afogamento"
            ]
            == "nao"
        )


def test_registro_polinjus_hidreletrica_curvajusante_afogamentoexplicito_usina():
    m: MagicMock = mock_open(
        read_data="".join(MockHidreletricaCurvaJusanteAfogamentoExplicitoUsina)
    )
    r = HidreletricaCurvaJusanteAfogamentoExplicitoUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [22, "sim"]
    assert r.codigo_usina == 22
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.considera_afogamento == "sim"
    r.considera_afogamento = "nao"
    assert r.considera_afogamento == "nao"


def test_registro_polinjus_hidreletrica_curvajusante_afogamentoexplicito_padrao():
    m: MagicMock = mock_open(
        read_data="".join(
            MockHidreletricaCurvaJusanteAfogamentoExplicitoPadrao
        )
    )
    r = HidreletricaCurvaJusanteAfogamentoExplicitoPadrao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == ["nao"]
    assert r.considera_afogamento == "nao"
    r.considera_afogamento = "sim"
    assert r.considera_afogamento == "sim"


def test_eq_polinjus():
    m: MagicMock = mock_open(read_data="".join(MockPolinjus))
    with patch("builtins.open", m):
        log1 = Polinjus.read(ARQ_TESTE)
        log2 = Polinjus.read(ARQ_TESTE)
        assert log1 == log2


def test_neq_polinjus():
    m: MagicMock = mock_open(read_data="".join(MockPolinjus))
    with patch("builtins.open", m):
        log1 = Polinjus.read(ARQ_TESTE)
        log2 = Polinjus.read(ARQ_TESTE)
        log1.hidreletrica_curvajusante_polinomio_segmento()[
            0
        ].codigo_usina = -1
        assert log1 != log2
