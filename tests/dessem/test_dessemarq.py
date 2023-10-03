from idessem.dessem.modelos.dessemarq import (
    RegistroCaso,
    RegistroTitulo,
    RegistroVazoes,
    RegistroDadger,
    RegistroMapfcf,
    RegistroCortfcf,
    RegistroCadusih,
    RegistroOperuh,
    RegistroDeflant,
    RegistroCadterm,
    RegistroOperut,
    RegistroIndelet,
    RegistroIlstri,
    RegistroCotasR11,
    RegistroSimul,
    RegistroAreacont,
    RegistroRespot,
    RegistroMlt,
    RegistroTolperd,
    RegistroCurvtviag,
    RegistroPtoper,
    RegistroInfofcf,
    RegistroMetas,
    RegistroREE,
    RegistroEolica,
    RegistroRampas,
    RegistroRstlpp,
    RegistroRestseg,
    RegistroRespotele,
    RegistroIlibs,
    RegistroUch,
)
from idessem.dessem.dessemarq import DessemArq
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dessemarq import (
    MockRegistroCaso,
    MockRegistroTitulo,
    MockRegistroVazoes,
    MockRegistroDadger,
    MockRegistroMapfcf,
    MockRegistroCortfcf,
    MockRegistroCadusih,
    MockRegistroOperuh,
    MockRegistroDeflant,
    MockRegistroCadterm,
    MockRegistroOperut,
    MockRegistroIndelet,
    MockRegistroIlstri,
    MockRegistroCotasr11,
    MockRegistroSimul,
    MockRegistroAreacont,
    MockRegistroRespot,
    MockRegistroMlt,
    MockRegistroTolperd,
    MockRegistroCurvtviag,
    MockRegistroPtoper,
    MockRegistroInfofcf,
    MockRegistroMeta,
    MockRegistroREE,
    MockRegistroEolica,
    MockRegistroRampas,
    MockRegistroRstlpp,
    MockRegistroRestseg,
    MockRegistroRespotele,
    MockRegistroIlibs,
    MockRegistroUch,
    MockDessemArq,
)

ARQ_TESTE = "./tests/__init__.py"


def test_registro_caso():
    m: MagicMock = mock_open(read_data="".join(MockRegistroCaso))
    r = RegistroCaso()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "NOME DO CASO                   (F)",
        "DAT",
    ]
    assert r.descricao == "NOME DO CASO                   (F)"
    r.descricao = "NOME"
    assert r.descricao == "NOME"
    assert r.valor == "DAT"
    r.valor = "dat"
    assert r.valor == "dat"


def test_registro_titulo():
    m: MagicMock = mock_open(read_data="".join(MockRegistroTitulo))
    r = RegistroTitulo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "TITULO DO ESTUDO               (F)",
        "TE  PMO - AGOSTO/22 - SETEMBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPER",
    ]
    assert r.descricao == "TITULO DO ESTUDO               (F)"
    r.descricao = "TITULO"
    assert r.descricao == "TITULO"
    assert (
        r.valor
        == "TE  PMO - AGOSTO/22 - SETEMBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPER"
    )
    r.valor = "PMO"
    assert r.valor == "PMO"


def test_registro_vazoes():
    m: MagicMock = mock_open(read_data="".join(MockRegistroVazoes))
    r = RegistroVazoes()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "VAZOES NATURAIS                (F)",
        "dadvaz.dat",
    ]
    assert r.descricao == "VAZOES NATURAIS                (F)"
    r.descricao = "VAZOES"
    assert r.descricao == "VAZOES"
    assert r.valor == "dadvaz.dat"
    r.valor = "dadvaz.dat2"
    assert r.valor == "dadvaz.dat2"


def test_registro_dadger():
    m: MagicMock = mock_open(read_data="".join(MockRegistroDadger))
    r = RegistroDadger()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "DADOS GERAIS DO PROBLEMA       (F)",
        "entdados.dat",
    ]
    assert r.descricao == "DADOS GERAIS DO PROBLEMA       (F)"
    r.descricao = "DADOS"
    assert r.descricao == "DADOS"
    assert r.valor == "entdados.dat"
    r.valor = "entdados.dat2"
    assert r.valor == "entdados.dat2"


def test_registro_mapfcf():
    m: MagicMock = mock_open(read_data="".join(MockRegistroMapfcf))
    r = RegistroMapfcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "MAPA DOS CORTES DO DECOMP     (NF)",
        "mapcut.rv1",
    ]
    assert r.descricao == "MAPA DOS CORTES DO DECOMP     (NF)"
    r.descricao = "CORTESH"
    assert r.descricao == "CORTESH"
    assert r.valor == "mapcut.rv1"
    r.valor = "cortesh.rv1"
    assert r.valor == "cortesh.rv1"


def test_registro_cortfcf():
    m: MagicMock = mock_open(read_data="".join(MockRegistroCortfcf))
    r = RegistroCortfcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "CORTES DO DECOMP              (NF)",
        "cortdeco.rv1",
    ]
    assert r.descricao == "CORTES DO DECOMP              (NF)"
    r.descricao = "CORTES"
    assert r.descricao == "CORTES"
    assert r.valor == "cortdeco.rv1"
    r.valor = "cortes.rv1"
    assert r.valor == "cortes.rv1"


def test_registro_cadusih():
    m: MagicMock = mock_open(read_data="".join(MockRegistroCadusih))
    r = RegistroCadusih()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "CADASTRO DAS USINAS HIDROELETRICAS",
        "hidr.dat",
    ]
    assert r.descricao == "CADASTRO DAS USINAS HIDROELETRICAS"
    r.descricao = "USINAS"
    assert r.descricao == "USINAS"
    assert r.valor == "hidr.dat"
    r.valor = "hidr"
    assert r.valor == "hidr"


def test_registro_operuh():
    m: MagicMock = mock_open(read_data="".join(MockRegistroOperuh))
    r = RegistroOperuh()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "RESTRICOES DE OPERACAO HIDRAULICA",
        "operuh.dat",
    ]
    assert r.descricao == "RESTRICOES DE OPERACAO HIDRAULICA"
    r.descricao = "USINAS"
    assert r.descricao == "USINAS"
    assert r.valor == "operuh.dat"
    r.valor = "operuh"
    assert r.valor == "operuh"


def test_registro_deflant():
    m: MagicMock = mock_open(read_data="".join(MockRegistroDeflant))
    r = RegistroDeflant()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "DEFLUENCIAS ANTERIORES         (F)",
        "deflant.dat",
    ]
    assert r.descricao == "DEFLUENCIAS ANTERIORES         (F)"
    r.descricao = "DEFLUENCIAS"
    assert r.descricao == "DEFLUENCIAS"
    assert r.valor == "deflant.dat"
    r.valor = "deflant"
    assert r.valor == "deflant"


def test_registro_cadterm():
    m: MagicMock = mock_open(read_data="".join(MockRegistroCadterm))
    r = RegistroCadterm()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "CADASTRO DAS USINAS TERMICAS   (F)",
        "termdat.dat",
    ]
    assert r.descricao == "CADASTRO DAS USINAS TERMICAS   (F)"
    r.descricao = "DEFLUENCIAS"
    assert r.descricao == "DEFLUENCIAS"
    assert r.valor == "termdat.dat"
    r.valor = "term"
    assert r.valor == "term"


def test_registro_operut():
    m: MagicMock = mock_open(read_data="".join(MockRegistroOperut))
    r = RegistroOperut()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "OPERACAO DAS UNIDADES TERMICAS (F)",
        "operut.dat",
    ]
    assert r.descricao == "OPERACAO DAS UNIDADES TERMICAS (F)"
    r.descricao = "OPERACAO"
    assert r.descricao == "OPERACAO"
    assert r.valor == "operut.dat"
    r.valor = "operut"
    assert r.valor == "operut"


def test_registro_indelet():
    m: MagicMock = mock_open(read_data="".join(MockRegistroIndelet))
    r = RegistroIndelet()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "ARQ. INDICE DA REDE ELETRICA   (F)",
        "desselet.dat",
    ]
    assert r.descricao == "ARQ. INDICE DA REDE ELETRICA   (F)"
    r.descricao = "REDE"
    assert r.descricao == "REDE"
    assert r.valor == "desselet.dat"
    r.valor = "elet"
    assert r.valor == "elet"


def test_registro_ilstri():
    m: MagicMock = mock_open(read_data="".join(MockRegistroIlstri))
    r = RegistroIlstri()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "CANAL PEREIRA BARRETO          (F)",
        "ils_tri.dat",
    ]
    assert r.descricao == "CANAL PEREIRA BARRETO          (F)"
    r.descricao = "CANAL"
    assert r.descricao == "CANAL"
    assert r.valor == "ils_tri.dat"
    r.valor = "canal"
    assert r.valor == "canal"


def test_registro_cotasr11():
    m: MagicMock = mock_open(read_data="".join(MockRegistroCotasr11))
    r = RegistroCotasR11()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "COTAS NA R11 ANTERIORES        (F)",
        "cotasr11.dat",
    ]
    assert r.descricao == "COTAS NA R11 ANTERIORES        (F)"
    r.descricao = "COTAS"
    assert r.descricao == "COTAS"
    assert r.valor == "cotasr11.dat"
    r.valor = "r11"
    assert r.valor == "r11"


def test_registro_simul():
    m: MagicMock = mock_open(read_data="".join(MockRegistroSimul))
    r = RegistroSimul()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "ARQ. COM DADOS PARA A SIMULACAO(F)",
        "",
    ]
    assert r.descricao == "ARQ. COM DADOS PARA A SIMULACAO(F)"
    r.descricao = "COTAS"
    assert r.descricao == "COTAS"
    assert r.valor == ""
    r.valor = "simul"
    assert r.valor == "simul"


def test_registro_areacont():
    m: MagicMock = mock_open(read_data="".join(MockRegistroAreacont))
    r = RegistroAreacont()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "CADASTRO DE RESERVA DE POTENCIA(F)",
        "areacont.dat",
    ]
    assert r.descricao == "CADASTRO DE RESERVA DE POTENCIA(F)"
    r.descricao = "CADASTRO"
    assert r.descricao == "CADASTRO"
    assert r.valor == "areacont.dat"
    r.valor = "area"
    assert r.valor == "area"


def test_registro_respot():
    m: MagicMock = mock_open(read_data="".join(MockRegistroRespot))
    r = RegistroRespot()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "ESTUDO DE  RESERVA DE POTENCIA (F)",
        "respot.dat",
    ]
    assert r.descricao == "ESTUDO DE  RESERVA DE POTENCIA (F)"
    r.descricao = "ESTUDO"
    assert r.descricao == "ESTUDO"
    assert r.valor == "respot.dat"
    r.valor = "respot"
    assert r.valor == "respot"


def test_registro_mlt():
    m: MagicMock = mock_open(read_data="".join(MockRegistroMlt))
    r = RegistroMlt()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "DADOS PARA A FPHA (MLT)        (F)",
        "mlt.dat",
    ]
    assert r.descricao == "DADOS PARA A FPHA (MLT)        (F)"
    r.descricao = "DADOS"
    assert r.descricao == "DADOS"
    assert r.valor == "mlt.dat"
    r.valor = "mlt"
    assert r.valor == "mlt"


def test_registro_tolperd():
    m: MagicMock = mock_open(read_data="".join(MockRegistroTolperd))
    r = RegistroTolperd()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "ARQ. DE TOLERANCIAS DAS PERDAS (F)",
        "",
    ]
    assert r.descricao == "ARQ. DE TOLERANCIAS DAS PERDAS (F)"
    r.descricao = "ARQUIVO"
    assert r.descricao == "ARQUIVO"
    assert r.valor == ""
    r.valor = "tolperd"
    assert r.valor == "tolperd"


def test_registro_curvtviag():
    m: MagicMock = mock_open(read_data="".join(MockRegistroCurvtviag))
    r = RegistroCurvtviag()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "CURVA DE PROPAGACAO DO TVIAG   (F)",
        "curvtviag.dat",
    ]
    assert r.descricao == "CURVA DE PROPAGACAO DO TVIAG   (F)"
    r.descricao = "CURVA"
    assert r.descricao == "CURVA"
    assert r.valor == "curvtviag.dat"
    r.valor = "curvtviag"
    assert r.valor == "curvtviag"


def test_registro_ptoper():
    m: MagicMock = mock_open(read_data="".join(MockRegistroPtoper))
    r = RegistroPtoper()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "PONTO DE OPERACAO DE USINAS GNL (F)",
        "ptoper.dat",
    ]
    assert r.descricao == "PONTO DE OPERACAO DE USINAS GNL (F)"
    r.descricao = "PTOPER"
    assert r.descricao == "PTOPER"
    assert r.valor == "ptoper.dat"
    r.valor = "ptoper"
    assert r.valor == "ptoper"


def test_registro_infofcf():
    m: MagicMock = mock_open(read_data="".join(MockRegistroInfofcf))
    r = RegistroInfofcf()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "INFORMACAO SOBRE OS CORTES      (F)",
        "infofcf.dat",
    ]
    assert r.descricao == "INFORMACAO SOBRE OS CORTES      (F)"
    r.descricao = "INFORMACAO"
    assert r.descricao == "INFORMACAO"
    assert r.valor == "infofcf.dat"
    r.valor = "info"
    assert r.valor == "info"


def test_registro_meta():
    m: MagicMock = mock_open(read_data="".join(MockRegistroMeta))
    r = RegistroMetas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "RESTRICOES DE METAS             (F)",
        "metas.dat",
    ]
    assert r.descricao == "RESTRICOES DE METAS             (F)"
    r.descricao = "RESTRICOES"
    assert r.descricao == "RESTRICOES"
    assert r.valor == "metas.dat"
    r.valor = "metas"
    assert r.valor == "metas"


def test_registro_ree():
    m: MagicMock = mock_open(read_data="".join(MockRegistroREE))
    r = RegistroREE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "RESERVATORIO EQUIVALENTES DE ENERGIA",
        "entdados.dat",
    ]
    assert r.descricao == "RESERVATORIO EQUIVALENTES DE ENERGIA"
    r.descricao = "REES"
    assert r.descricao == "REES"
    assert r.valor == "entdados.dat"
    r.valor = "rees"
    assert r.valor == "rees"


def test_registro_eolica():
    m: MagicMock = mock_open(read_data="".join(MockRegistroEolica))
    r = RegistroEolica()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "USINAS EOLICAS - RENOVAVEIS",
        "renovaveis.dat",
    ]
    assert r.descricao == "USINAS EOLICAS - RENOVAVEIS"
    r.descricao = "RENOVAVEIS"
    assert r.descricao == "RENOVAVEIS"
    assert r.valor == "renovaveis.dat"
    r.valor = "renovaveis"
    assert r.valor == "renovaveis"


def test_registro_rampas():
    m: MagicMock = mock_open(read_data="".join(MockRegistroRampas))
    r = RegistroRampas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "ARQUIVO DE TRAJETORIAS",
        "rampas.dat",
    ]
    assert r.descricao == "ARQUIVO DE TRAJETORIAS"
    r.descricao = "RAMPAS"
    assert r.descricao == "RAMPAS"
    assert r.valor == "rampas.dat"
    r.valor = "rampas"
    assert r.valor == "rampas"


def test_registro_lpp():
    m: MagicMock = mock_open(read_data="".join(MockRegistroRstlpp))
    r = RegistroRstlpp()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "RESTRICOES LPP",
        "rstlpp.dat",
    ]
    assert r.descricao == "RESTRICOES LPP"
    r.descricao = "LPP"
    assert r.descricao == "LPP"
    assert r.valor == "rstlpp.dat"
    r.valor = "lpp"
    assert r.valor == "lpp"


def test_registro_restseg():
    m: MagicMock = mock_open(read_data="".join(MockRegistroRestseg))
    r = RegistroRestseg()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "RESTRICOES TABELA",
        "restseg.dat",
    ]
    assert r.descricao == "RESTRICOES TABELA"
    r.descricao = "TABELA"
    assert r.descricao == "TABELA"
    assert r.valor == "restseg.dat"
    r.valor = "tabela"
    assert r.valor == "tabela"


def test_registro_respotele():
    m: MagicMock = mock_open(read_data="".join(MockRegistroRespotele))
    r = RegistroRespotele()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "RESERVA DE POTENCIA REDE ELETR (F)",
        "respotele.dat",
    ]
    assert r.descricao == "RESERVA DE POTENCIA REDE ELETR (F)"
    r.descricao = "RESERVA"
    assert r.descricao == "RESERVA"
    assert r.valor == "respotele.dat"
    r.valor = "reserva"
    assert r.valor == "reserva"


def test_registro_ilibs():
    m: MagicMock = mock_open(read_data="".join(MockRegistroIlibs))
    r = RegistroIlibs()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "FUNCIONALIDADES LIBS",
        "indice_csv.csv",
    ]
    assert r.descricao == "FUNCIONALIDADES LIBS"
    r.descricao = "LIBS"
    assert r.descricao == "LIBS"
    assert r.valor == "indice_csv.csv"
    r.valor = "indice"
    assert r.valor == "indice"


def test_registro_uch():
    m: MagicMock = mock_open(read_data="".join(MockRegistroUch))
    r = RegistroUch()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "Dados UCH",
        "uch.csv",
    ]
    assert r.descricao == "Dados UCH"
    r.descricao = "UCH"
    assert r.descricao == "UCH"
    assert r.valor == "uch.csv"
    r.valor = "uch"
    assert r.valor == "uch"


def test_campos_nao_encontrados_dessemarq():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = DessemArq.read(ARQ_TESTE)
    assert d.caso is None
    assert d.titulo is None
    assert d.vazoes is None
    assert d.dadger is None
    assert d.mapfcf is None
    assert d.cortfcf is None
    assert d.cadusih is None
    assert d.operuh is None
    assert d.deflant is None
    assert d.cadterm is None
    assert d.operut is None
    assert d.indelet is None
    assert d.ilstri is None
    assert d.cotasr11 is None
    assert d.simul is None
    assert d.areacont is None
    assert d.respot is None
    assert d.mlt is None
    assert d.tolperd is None
    assert d.curvtviag is None
    assert d.ptoper is None
    assert d.infofcf is None
    assert d.meta is None
    assert d.ree is None
    assert d.eolica is None
    assert d.rampas is None
    assert d.rstlpp is None
    assert d.restseg is None
    assert d.respotele is None
    assert d.ilibs is None
    assert d.uch is None


def test_campos_encontrados_dessemarq():
    m: MagicMock = mock_open(read_data="".join(MockDessemArq))
    with patch("builtins.open", m):
        d = DessemArq.read(ARQ_TESTE)
    assert d.caso is not None
    assert d.titulo is not None
    assert d.vazoes is not None
    assert d.dadger is not None
    assert d.mapfcf is not None
    assert d.cortfcf is not None
    assert d.cadusih is not None
    assert d.operuh is not None
    assert d.deflant is not None
    assert d.cadterm is not None
    assert d.operut is not None
    assert d.indelet is not None
    assert d.ilstri is not None
    assert d.cotasr11 is not None
    assert d.simul is not None
    assert d.areacont is not None
    assert d.respot is not None
    assert d.mlt is not None
    assert d.tolperd is not None
    assert d.curvtviag is not None
    assert d.ptoper is not None
    assert d.infofcf is not None
    assert d.meta is not None
    assert d.ree is not None
    assert d.eolica is not None
    assert d.rampas is not None
    assert d.rstlpp is not None
    assert d.restseg is not None
    assert d.respotele is not None
    assert d.ilibs is not None
    assert d.uch is None


def test_eq_dessemarq():
    m: MagicMock = mock_open(read_data="".join(MockDessemArq))
    with patch("builtins.open", m):
        d1 = DessemArq.read(ARQ_TESTE)
        d2 = DessemArq.read(ARQ_TESTE)
        assert d1 == d2


def test_neq_dessemarq():
    m: MagicMock = mock_open(read_data="".join(MockDessemArq))
    with patch("builtins.open", m):
        d1 = DessemArq.read(ARQ_TESTE)
        d2 = DessemArq.read(ARQ_TESTE)
        d2.caso.valor = "txt"
        assert d1 != d2


def test_leitura_escrita_dessemarq():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDessemArq))
    with patch("builtins.open", m_leitura):
        d1 = DessemArq.read(ARQ_TESTE)
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
        d2 = DessemArq.read(ARQ_TESTE)
        assert d1 == d2
