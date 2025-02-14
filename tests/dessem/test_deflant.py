from idessem.dessem.deflant import Deflant
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
from tests.mocks.arquivos.deflant import (
    MockDeflant
)

ARQ_TESTE = "./tests/__init__.py"

def test_campos_encontrados_deflant():
    m: MagicMock = mock_open(read_data="".join(MockDeflant))
    with patch("builtins.open", m):
        d = Deflant.read("./tests/mocks/arquivos/deflant.py")

    assert d.defant(codigo_usina_montante=2) is not None
    assert d.defant(codigo_elemento_jusante=6) is not None
    assert d.defant(codigo_usina_montante=1) is None
    assert d.defant(df=True).at[0,"defluencia"] == 110

    reg = d.defant(codigo_usina_montante=2)
    assert reg.data == [
        2,
        4,
        "H",
        [10, 0, 0],
        ["F", None, None],
         110
        ]

    assert reg.codigo_usina_montante == 2
    reg.codigo_usina_montante = -1
    assert reg.codigo_usina_montante == -1
    assert reg.codigo_elemento_jusante == 4
    reg.codigo_elemento_jusante = -1
    assert reg.codigo_elemento_jusante == -1
    assert reg.tipo_elemento_jusante == "H"
    reg.tipo_elemento_jusante = "X"
    assert reg.tipo_elemento_jusante == "X"
    assert reg.dia_inicial == 10
    reg.dia_inicial = 9
    assert reg.dia_inicial == 9
    assert reg.hora_inicial == 00
    reg.hora_inicial = 9
    assert reg.hora_inicial == 9
    assert reg.meia_hora_inicial == 0
    reg.meia_hora_inicial = 9
    assert reg.meia_hora_inicial == 9
    assert reg.dia_final == "F"
    reg.dia_final = 0
    assert reg.dia_final == 0
    assert reg.hora_final is None
    reg.hora_final = 0
    assert reg.hora_final == 0
    assert reg.meia_hora_final is None
    reg.meia_hora_final = 0
    assert reg.meia_hora_final == 0
    assert reg.defluencia == 110
    reg.defluencia = -1
    assert reg.defluencia == -1
    

def test_eq_deflant():
    m: MagicMock = mock_open(read_data="".join(MockDeflant))
    with patch("builtins.open", m):
        d1 = Deflant.read("./tests/mocks/arquivos/deflant.py")
        d2 = Deflant.read("./tests/mocks/arquivos/deflant.py")
        assert d1 == d2


def test_neq_deflant():
    m: MagicMock = mock_open(read_data="".join(MockDeflant))
    with patch("builtins.open", m):
        d1 = Deflant.read("./tests/mocks/arquivos/deflant.py")
        d2 = Deflant.read("./tests/mocks/arquivos/deflant.py")
        d2.defant(codigo_usina_montante=2).codigo_elemento_jusante = 999
        assert d1 != d2


def test_leitura_escrita_deflant():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDeflant))
    with patch("builtins.open", m_leitura):
        d1 = Deflant.read("./tests/mocks/arquivos/deflant.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/deflant.py")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Deflant.read("./tests/mocks/arquivos/deflant.py")
        assert d1 == d2
