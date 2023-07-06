from idessem.dessem.modelos.entdados import UH, SIST, REE, TM, RIVAR, RD
from idessem.dessem.entdados import Entdados
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.entdados import (
    MockUHliteral,
    MockUHinteiro,
    MockSIST,
    MockREE,
    MockTM,
    MockRIVAR,
    MockRD,
)

ARQ_TESTE = "./tests/__init__.py"


def test_registro_rd_entdados():
    m: MagicMock = mock_open(read_data="".join(MockRD))
    r = RD()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        800,
        0,
        1,
        None,
        None,
        None,
    ]

    assert r.variaveis_de_folga == 1
    r.variaveis_de_folga = -1
    assert r.variaveis_de_folga == -1
    assert r.maximo_circuitos_violados == 800
    r.maximo_circuitos_violados = -1
    assert r.maximo_circuitos_violados == -1
    assert r.carga_registro_dbar == 0
    r.carga_registro_dbar = -1
    assert r.carga_registro_dbar == -1
    assert r.limites_circuitos_transformadores_elevadores == 1
    r.limites_circuitos_transformadores_elevadores = -1
    assert r.limites_circuitos_transformadores_elevadores == -1
    assert r.limites_circuitos_e_drefs is None
    r.limites_circuitos_e_drefs = -1
    assert r.limites_circuitos_e_drefs == -1
    assert r.consideracao_perdas is None
    r.consideracao_perdas = -1
    assert r.consideracao_perdas == -1
    assert r.formato_arquivos_rede is None
    r.formato_arquivos_rede = -1
    assert r.formato_arquivos_rede == -1


def test_registro_rivar_entdados():
    m: MagicMock = mock_open(read_data="".join(MockRIVAR))
    r = RIVAR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        999,
        None,
        4,
        None,
    ]

    assert r.codigo_entidade == 999
    r.codigo_entidade = -1
    assert r.codigo_entidade == -1
    assert r.sistema_para is None
    r.sistema_para = -1
    assert r.sistema_para == -1
    assert r.tipo_variavel == 4
    r.tipo_variavel = -1
    assert r.tipo_variavel == -1
    assert r.penalidade is None
    r.penalidade = -1
    assert r.penalidade == -1


def test_registro_tm_entdados():
    m: MagicMock = mock_open(read_data="".join(MockTM))
    r = TM()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        11,
        0,
        0,
        0.5,
        1,
        "LEVE",
    ]

    assert r.dia_inicial == 11
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.duracao == 0.5
    r.duracao = -1
    assert r.duracao == -1
    assert r.consideracao_rede_eletrica == 1
    r.consideracao_rede_eletrica = -1
    assert r.consideracao_rede_eletrica == -1
    assert r.patamar_de_carga == "LEVE"
    r.patamar_de_carga = "XX"
    assert r.patamar_de_carga == "XX"


def test_registro_sist_entdados():
    m: MagicMock = mock_open(read_data="".join(MockSIST))
    r = SIST()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        "SE",
        0,
        "SUDESTE",
    ]

    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.mnemonico == "SE"
    r.mnemonico = "XX"
    assert r.mnemonico == "XX"
    assert r.ficticio == 0
    r.ficticio = -1
    assert r.ficticio == -1
    assert r.nome == "SUDESTE"
    r.nome = "XX"
    assert r.nome == "XX"


def test_registro_ree_entdados():
    m: MagicMock = mock_open(read_data="".join(MockREE))
    r = REE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        1,
        "SUDESTE",
    ]

    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.submercado == 1
    r.submercado = -1
    assert r.submercado == -1
    assert r.nome == "SUDESTE"
    r.nome = "XX"
    assert r.nome == "XX"


def test_registro_uh_entdados_literal():
    m: MagicMock = mock_open(read_data="".join(MockUHliteral))
    r = UH()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        34,
        "I. SOLTEIRA",
        10,
        80.77,
        1,
        "I",
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo == 34
    r.codigo = 0
    assert r.codigo == 0
    assert r.nome == "I. SOLTEIRA"
    r.nome = "ILHA"
    assert r.nome == "ILHA"
    assert r.ree == 10
    r.ree = 0
    assert r.ree == 0
    assert r.volume_inicial == 80.77
    r.volume_inicial = 0
    assert r.volume_inicial == 0
    assert r.evaporacao == 1
    r.evaporacao = 0
    assert r.evaporacao == 0
    assert r.dia_inicial == "I"
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial is None
    r.hora_inicial = 0
    assert r.hora_inicial == 0
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 0
    assert r.meia_hora_inicial == 0
    assert r.volume_morto_inicial is None
    r.volume_morto_inicial = 0
    assert r.volume_morto_inicial == 0
    assert r.produtividade is None
    r.produtividade = 0
    assert r.produtividade == 0
    assert r.penaliza_restricao_geracao is None
    r.penaliza_restricao_geracao = 0
    assert r.penaliza_restricao_geracao == 0


def test_registro_uh_entdados_inteiro():
    m: MagicMock = mock_open(read_data="".join(MockUHinteiro))
    r = UH()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        34,
        "I. SOLTEIRA",
        10,
        80.77,
        1,
        "30",
        1,
        1,
        50.60,
        1,
        1,
    ]

    assert r.codigo == 34
    r.codigo = 0
    assert r.codigo == 0
    assert r.nome == "I. SOLTEIRA"
    r.nome = "ILHA"
    assert r.nome == "ILHA"
    assert r.ree == 10
    r.ree = 0
    assert r.ree == 0
    assert r.volume_inicial == 80.77
    r.volume_inicial = 0
    assert r.volume_inicial == 0
    assert r.evaporacao == 1
    r.evaporacao = 0
    assert r.evaporacao == 0
    assert r.dia_inicial == 30
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial == 1
    r.hora_inicial = 0
    assert r.hora_inicial == 0
    assert r.meia_hora_inicial == 1
    r.meia_hora_inicial = 0
    assert r.meia_hora_inicial == 0
    assert r.volume_morto_inicial == 50.60
    r.volume_morto_inicial = 0
    assert r.volume_morto_inicial == 0
    assert r.produtividade == 1
    r.produtividade = 0
    assert r.produtividade == 0
    assert r.penaliza_restricao_geracao == 1
    r.penaliza_restricao_geracao = 0
    assert r.penaliza_restricao_geracao == 0


# def test_campos_nao_encontrados_entdados():
#     m: MagicMock = mock_open(read_data="")
#     with patch("builtins.open", m):
#         d = Entdados.le_arquivo("", "")
#     # assert d.te is None
#     # assert d.sb(0) is None
#     assert d.uh(0) is None
#     # assert d.ct(0, 0) is None
#     # assert d.dp(0, 0) is None
#     # assert d.ac(0, ACNUMCON, mes="", revisao=0, ano=0) is None
#     # assert d.cd(0, 0) is None
#     # assert d.tx is None
#     # assert d.gp is None
#     # assert d.ni is None
#     # assert d.dt is None
#     # assert d.re(0) is None
#     # assert d.lu(0, 0) is None
#     # assert d.vi(0) is None
#     # assert d.ir("") is None
#     # assert d.rt("") is None
#     # assert d.fc("") is None
#     # assert d.ti(0) is None
#     # assert d.fp(0, 0) is None
#     # assert d.ve(0) is None
#     # assert d.hv(0) is None
#     # assert d.lv(0, 0) is None
#     # assert d.hq(0) is None
#     # assert d.lq(0, 0) is None
#     # assert d.he(0, 0) is None
#     # assert d.cm(0) is None


# def test_campos_encontrados_entdados():
#     m: MagicMock = mock_open(read_data="".join(MockEntDados))
#     with patch("builtins.open", m):
#         d = Entdados.le_arquivo("", "")
#     # assert d.te is not None
#     # assert d.sb(1) is not None
#     assert d.uh(1) is not None
#     # assert d.ct(65, 1) is not None
#     # assert d.dp(1, 1) is not None
#     # assert d.ac(285, ACJUSMED) is not None
#     # assert d.cd(1, 1) is not None
#     # assert d.tx is not None
#     # assert d.gp is not None
#     # assert d.ni is not None
#     # assert d.dt is not None
#     # assert d.re(449) is not None
#     # assert d.lu(449, 1) is not None
#     # assert d.vi(156) is not None
#     # assert d.ir("GRAFICO") is not None
#     # assert d.rt("CRISTA") is not None
#     # assert d.fc("NEWV21") is not None
#     # assert d.ti(1) is not None
#     # assert d.fp(999, 1) is not None
#     # assert d.ve(1) is not None
#     # assert d.hv(101) is not None
#     # assert d.lv(101, 1) is not None
#     # assert d.hq(254) is not None
#     # assert d.lq(254, 1) is not None
#     # assert d.he(1, 1) is not None
#     # assert d.cm(1) is not None


# def test_cria_lu_entdados():
#     m: MagicMock = mock_open(read_data="".join(MockEntDados))
#     with patch("builtins.open", m):
#         d = Entdados.le_arquivo("", "")
#         lu = d.lu(1, 2)
#         assert lu is not None
#         assert lu.limites_inferiores == d.lu(1, 1).limites_inferiores
#         lu.limites_inferiores = [0.0]
#         assert lu.limites_inferiores != d.lu(1, 1).limites_inferiores
#         assert lu.limites_superiores == d.lu(1, 1).limites_superiores
#         lu.limites_superiores = [0.0]
#         assert lu.limites_superiores != d.lu(1, 1).limites_superiores


# def test_cria_lv_entdados():
#     m: MagicMock = mock_open(read_data="".join(MockEntDados))
#     with patch("builtins.open", m):
#         d = Entdados.le_arquivo("", "")
#         lv = d.lv(3, 2)
#         assert lv is not None
#         assert lv.limite_inferior == d.lv(3, 1).limite_inferior
#         lv.limite_inferior = 0.0
#         assert lv.limite_inferior != d.lv(3, 1).limite_inferior
#         assert lv.limite_superior == d.lv(3, 1).limite_superior
#         lv.limite_superior = 0.0
#         assert lv.limite_superior != d.lv(3, 1).limite_superior


# def test_cria_lq_entdados():
#     m: MagicMock = mock_open(read_data="".join(MockEntDados))
#     with patch("builtins.open", m):
#         d = Entdados.le_arquivo("", "")
#         lq = d.lq(5, 2)
#         assert lq is not None
#         assert lq.limites_inferiores == d.lq(5, 1).limites_inferiores
#         lq.limites_inferiores = [0.0]
#         assert lq.limites_inferiores != d.lq(5, 1).limites_inferiores
#         assert lq.limites_superiores == d.lq(5, 1).limites_superiores
#         lq.limites_superiores = [0.0]
#         assert lq.limites_superiores != d.lq(5, 1).limites_superiores


# def test_eq_entdados():
#     m: MagicMock = mock_open(read_data="".join(MockEntDados))
#     with patch("builtins.open", m):
#         d1 = Entdados.le_arquivo("")
#         d2 = Entdados.le_arquivo("")
#         assert d1 == d2


# def test_neq_entdados():
#     m: MagicMock = mock_open(read_data="".join(MockEntDados))
#     with patch("builtins.open", m):
#         d1 = Entdados.le_arquivo("")
#         d2 = Entdados.le_arquivo("")
#         d2.te.titulo = "Teste"
#         assert d1 != d2


# def test_leitura_escrita_entdados():
#     m_leitura: MagicMock = mock_open(read_data="".join(MockEntDados))
#     with patch("builtins.open", m_leitura):
#         d1 = Entdados.le_arquivo("")
#     m_escrita: MagicMock = mock_open(read_data="")
#     with patch("builtins.open", m_escrita):
#         d1.escreve_arquivo("", "")
#         # Recupera o que foi escrito
#         chamadas = m_escrita.mock_calls
#         linhas_escritas = [
#             chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
#         ]
#     m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
#     with patch("builtins.open", m_releitura):
#         d2 = Entdados.le_arquivo("")
#         assert d1 == d2
