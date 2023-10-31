from idessem.dessem.vazaolateral import VazaoLateral
from idessem.dessem.modelos.vazaolateral import (
    HidreletricaVazaoJusanteInfluenciaUsina,
    HidreletricaVazaoJusanteInfluenciaDefluencia,
    HidreletricaVazaoJusanteInfluenciaPosto,
)
import pandas as pd  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.vazaolateral import (
    MockVazaoLateral,
    MockHidreletricaVazaoJusanteInfluenciaUsina,
    MockHidreletricaVazaoJusanteInfluenciaPosto,
    MockHidreletricaVazaoJusanteInfluenciaDefluencia,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_uch():
    m: MagicMock = mock_open(read_data="".join(MockVazaoLateral))
    with patch("builtins.open", m):
        vazaolateral = VazaoLateral.read(ARQ_TESTE)
        assert vazaolateral.vazao_jusante_influencia_defluencia() is not None
        assert vazaolateral.vazao_jusante_influencia_usina() is not None
        assert vazaolateral.vazao_jusante_influencia_posto() is not None


def test_registro_influencia_defluencia():
    m: MagicMock = mock_open(
        read_data="".join(MockHidreletricaVazaoJusanteInfluenciaDefluencia)
    )
    r = HidreletricaVazaoJusanteInfluenciaDefluencia()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [288, 1, 1]
    assert r.codigo_usina_influenciada == 288
    r.codigo_usina_influenciada = 0
    assert r.codigo_usina_influenciada == 0
    assert r.fator_impacto_turbinamento == 1
    r.fator_impacto_turbinamento = 0
    assert r.fator_impacto_turbinamento == 0
    assert r.fator_impacto_vertimento == 1
    r.fator_impacto_vertimento = 0
    assert r.fator_impacto_vertimento == 0


def test_registro_influencia_usina():
    m: MagicMock = mock_open(
        read_data="".join(MockHidreletricaVazaoJusanteInfluenciaUsina)
    )
    r = HidreletricaVazaoJusanteInfluenciaUsina()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [288, 314, 1]
    assert r.codigo_usina_influenciada == 288
    r.codigo_usina_influenciada = 0
    assert r.codigo_usina_influenciada == 0
    assert r.codigo_usina_influenciadora == 314
    r.codigo_usina_influenciadora = 0
    assert r.codigo_usina_influenciadora == 0
    assert r.fator_impacto == 1
    r.fator_impacto = 0
    assert r.fator_impacto == 0


def test_registro_influencia_posto():
    m: MagicMock = mock_open(
        read_data="".join(MockHidreletricaVazaoJusanteInfluenciaPosto)
    )
    r = HidreletricaVazaoJusanteInfluenciaPosto()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [288, 314, 0.07]
    assert r.codigo_usina_influenciada == 288
    r.codigo_usina_influenciada = 0
    assert r.codigo_usina_influenciada == 0
    assert r.codigo_usina_influenciadora == 314
    r.codigo_usina_influenciadora = 0
    assert r.codigo_usina_influenciadora == 0
    assert r.fator_impacto == 0.07
    r.fator_impacto = 0
    assert r.fator_impacto == 0


def test_eq_vazaolateral():
    m: MagicMock = mock_open(read_data="".join(MockVazaoLateral))
    with patch("builtins.open", m):
        arq1 = VazaoLateral.read(ARQ_TESTE)
        arq2 = VazaoLateral.read(ARQ_TESTE)
        assert arq1 == arq2


def test_neq_vazaolateral():
    m: MagicMock = mock_open(read_data="".join(MockVazaoLateral))
    with patch("builtins.open", m):
        arq1 = VazaoLateral.read(ARQ_TESTE)
        arq2 = VazaoLateral.read(ARQ_TESTE)
        arq1.vazao_jusante_influencia_defluencia()[
            0
        ].codigo_usina_influenciada = 200
        assert arq1 != arq2
