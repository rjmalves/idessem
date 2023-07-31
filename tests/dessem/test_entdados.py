from idessem.dessem.modelos.entdados import (
    UH,
    SIST,
    REE,
    TM,
    RIVAR,
    RD,
    TVIAG,
    UT,
    USIE,
    DP,
    DE,
    CD,
    PQ,
    RI,
    IA,
    GP,
    IT,
    NI,
    VE,
    FP,
    TX,
    EZ,
    R11,
    CR,
    SECR,
    DA,
    RE,
    LU,
    FH,
    FT,
    FI,
    FE,
    FR,
    FC,
    CI,
    CE,
    MH,
    PE,
    ACVTFUGA,
    ACVOLMAX,
    ACVOLMIN,
    ACVSVERT,
    ACVMDESV,
    ACCOTVAZ,
    ACCOTVOL,
    ACCOTTAR,
    ACNUMCON,
    ACNUMJUS,
    ACNUMPOS,
    ACJUSENA,
    ACJUSMED,
    ACCOFEVA,
    ACNUMMAQ,
    ACPOTEFE,
    ACDESVIO,
)
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
    MockTVIAG,
    MockUTliteral,
    MockUTinteiro,
    MockUSIE,
    MockDPliteral,
    MockDPinteiro,
    MockDE,
    MockCD,
    MockPQ,
    MockIT,
    MockRI,
    MockIA,
    MockGP,
    MockNI,
    MockVE,
    MockFP,
    MockTX,
    MockEZ,
    MockR11,
    MockCR,
    MockSECR,
    MockDA,
    MockRE,
    MockLU,
    MockFH,
    MockFT,
    MockFI,
    MockFE,
    MockFR,
    MockFC,
    MockCI,
    MockCE,
    MockMH,
    MockPE,
    MockACVTFUGA,
    MockACVOLMAX,
    MockACVOLMIN,
    MockACVSVERT,
    MockACVMDESV,
    MockACCOTVAZ,
    MockEntDados,
    MockACCOTVOL,
    MockACCOTTAR,
    MockACNUMCON,
    MockACNUMJUS,
    MockACNUMPOS,
    MockACJUSENA,
    MockACJUSMED,
    MockACCOFEVA,
    MockACNUMMAQ,
    MockACDESVIO,
    MockACPOTEFE,
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
        ["I", None, None],
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
        [30, 1, 1],
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


def test_registro_tviag_entdados():
    m: MagicMock = mock_open(read_data="".join(MockTVIAG))
    r = TVIAG()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        66,
        1,
        "S",
        24,
        2,
    ]

    assert r.uhe_montante == 66
    r.uhe_montante = -1
    assert r.uhe_montante == -1
    assert r.elemento_jusante == 1
    r.elemento_jusante = -1
    assert r.elemento_jusante == -1
    assert r.tipo_elemento_jusante == "S"
    r.tipo_elemento_jusante = "X"
    assert r.tipo_elemento_jusante == "X"
    assert r.duracao == 24
    r.duracao = -1
    assert r.duracao == -1
    assert r.tipo_tempo_viagem == 2
    r.tipo_tempo_viagem = -1
    assert r.tipo_tempo_viagem == -1


def test_registro_ut_entdados_literal():
    m: MagicMock = mock_open(read_data="".join(MockUTliteral))
    r = UT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        "ANGRA 1",
        1,
        2,
        ["I", None, None],
        ["F", None, None],
        None,
        582.0,
        582.0,
    ]
    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.nome == "ANGRA 1"
    r.nome = "ILHA"
    assert r.nome == "ILHA"
    assert r.submercado == 1
    r.submercado = 0
    assert r.submercado == 0
    assert r.tipo_restricao == 2
    r.tipo_restricao = 0
    assert r.tipo_restricao == 0
    assert r.dia_inicial == "I"
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial is None
    r.hora_inicial = 0
    assert r.hora_inicial == 0
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 0
    assert r.meia_hora_inicial == 0
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 0
    assert r.hora_final == 0
    assert r.meia_hora_final is None
    r.meia_hora_final = 0
    assert r.meia_hora_final == 0
    assert r.unidade_restricao is None
    r.unidade_restricao = 0
    assert r.unidade_restricao == 0
    assert r.geracao_minima == 582.0
    r.geracao_minima = 0
    assert r.geracao_minima == 0
    assert r.geracao_maxima == 582.0
    r.geracao_maxima = 0
    assert r.geracao_maxima == 0


def test_registro_ut_entdados_inteiro():
    m: MagicMock = mock_open(read_data="".join(MockUTinteiro))
    r = UT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        "ANGRA 1",
        1,
        2,
        [11, 0, 0],
        [12, 0, 0],
        None,
        582.0,
        582.0,
    ]
    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.nome == "ANGRA 1"
    r.nome = "ILHA"
    assert r.nome == "ILHA"
    assert r.submercado == 1
    r.submercado = 0
    assert r.submercado == 0
    assert r.tipo_restricao == 2
    r.tipo_restricao = 0
    assert r.tipo_restricao == 0
    assert r.dia_inicial == 11
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial == 0
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == 12
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final == 0
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final == 0
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.unidade_restricao is None
    r.unidade_restricao = 0
    assert r.unidade_restricao == 0
    assert r.geracao_minima == 582.0
    r.geracao_minima = 0
    assert r.geracao_minima == 0
    assert r.geracao_maxima == 582.0
    r.geracao_maxima = 0
    assert r.geracao_maxima == 0


def test_registro_usie_entdados():
    m: MagicMock = mock_open(read_data="".join(MockUSIE))
    r = USIE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        1,
        "Sta Cecilia",
        181,
        125,
        0.00,
        160.0,
        0.20,
    ]

    assert r.codigo == 1
    r.codigo = -1
    assert r.codigo == -1
    assert r.submercado == 1
    r.submercado = -1
    assert r.submercado == -1
    assert r.nome == "Sta Cecilia"
    r.nome = "XX"
    assert r.nome == "XX"
    assert r.uhe_montante == 181
    r.uhe_montante = -1
    assert r.uhe_montante == -1
    assert r.uhe_jusante == 125
    r.uhe_jusante = -1
    assert r.uhe_jusante == -1
    assert r.vazao_minima_bombeavel == 0.00
    r.vazao_minima_bombeavel = -1
    assert r.vazao_minima_bombeavel == -1
    assert r.vazao_maxima_bombeavel == 160.00
    r.vazao_maxima_bombeavel = -1
    assert r.vazao_maxima_bombeavel == -1
    assert r.taxa_consumo == 0.20
    r.taxa_consumo = -1
    assert r.taxa_consumo == -1


def test_registro_dp_entdados_literal():
    m: MagicMock = mock_open(read_data="".join(MockDPliteral))
    r = DP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        ["I", None, None],
        ["F", None, None],
        36904,
    ]
    assert r.submercado == 1
    r.submercado = -1
    assert r.submercado == -1
    assert r.dia_inicial == "I"
    r.dia_inicial = 0
    assert r.dia_inicial == 0
    assert r.hora_inicial is None
    r.hora_inicial = 0
    assert r.hora_inicial == 0
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 0
    assert r.meia_hora_inicial == 0
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 0
    assert r.hora_final == 0
    assert r.meia_hora_final is None
    r.meia_hora_final = 0
    assert r.meia_hora_final == 0
    assert r.demanda == 36904
    r.demanda = -1
    assert r.demanda == -1


def test_registro_dp_entdados_inteiro():
    m: MagicMock = mock_open(read_data="".join(MockDPinteiro))
    r = DP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        [11, 0, 0],
        [12, 1, 1],
        36904,
    ]
    assert r.submercado == 1
    r.submercado = -1
    assert r.submercado == -1
    assert r.dia_inicial == 11
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == 12
    r.dia_final = -1
    assert r.dia_final == -1
    assert r.hora_final == 1
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final == 1
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.demanda == 36904
    r.demanda = -1
    assert r.demanda == -1


def test_registro_de_entdados():
    m: MagicMock = mock_open(read_data="".join(MockDE))
    r = DE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, [11, 0, 0], ["F", None, None], 1469, ""]
    assert r.codigo == 1
    r.codigo = -1
    assert r.codigo == -1
    assert r.dia_inicial == 11
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == "F"
    r.dia_final = -1
    assert r.dia_final == -1
    assert r.hora_final is None
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final is None
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.demanda == 1469
    r.demanda = -1
    assert r.demanda == -1
    assert r.justificativa == ""
    r.justificativa = -1
    assert r.justificativa == -1


def test_registro_cd_entdados():
    m: MagicMock = mock_open(read_data="".join(MockCD))
    r = CD()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, [6, 0, 0], ["F", None, None], 7643.82, 100]
    assert r.submercado == 1
    r.submercado = -1
    assert r.submercado == -1
    assert r.numero_curva == 1
    r.numero_curva = -1
    assert r.numero_curva == -1
    assert r.dia_inicial == 6
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == "F"
    r.dia_final = -1
    assert r.dia_final == -1
    assert r.hora_final is None
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final is None
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.custo == 7643.82
    r.custo = -1
    assert r.custo == -1
    assert r.limite_superior == 100
    r.limite_superior = -1
    assert r.limite_superior == -1


def test_registro_pq_entdados():
    m: MagicMock = mock_open(read_data="".join(MockPQ))
    r = PQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, "SE-Eolica", 1, ["I", None, None], [24, 0, 0], 3]
    assert r.codigo == 1
    r.codigo = -1
    assert r.codigo == -1
    assert r.nome == "SE-Eolica"
    r.nome = -1
    assert r.nome == -1
    assert r.localizacao == 1
    r.localizacao = -1
    assert r.localizacao == -1
    assert r.dia_inicial == "I"
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == 24
    r.dia_final = -1
    assert r.dia_final == -1
    assert r.hora_final == 0
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final == 0
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.geracao == 3


def test_registro_it_entdados():
    m: MagicMock = mock_open(read_data="".join(MockIT))
    r = IT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        7.8120269e01,
        3.4278554e-03,
        -1.6012117e-07,
        4.1770037e-12,
        -4.0930359e-17,
    ]
    assert r.ree == 1
    r.ree = -1
    assert r.ree == -1
    assert r.coeficiente_a0 == 7.8120269e01
    r.coeficiente_a0 = 0
    assert r.coeficiente_a0 == 0
    assert r.coeficiente_a1 == 3.4278554e-03
    r.coeficiente_a1 = 0
    assert r.coeficiente_a1 == 0
    assert r.coeficiente_a2 == -1.6012117e-07
    r.coeficiente_a2 = 0
    assert r.coeficiente_a2 == 0
    assert r.coeficiente_a3 == 4.1770037e-12
    r.coeficiente_a3 = 0
    assert r.coeficiente_a3 == 0
    assert r.coeficiente_a4 == -4.0930359e-17
    r.coeficiente_a4 = 0
    assert r.coeficiente_a4 == 0


def test_registro_ri_entdados():
    m: MagicMock = mock_open(read_data="".join(MockRI))
    r = RI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        [17, 0, 0],
        ["F", None, None],
        2500,
        7000,
        2000,
        7000,
        1530,
    ]
    assert r.dia_inicial == 17
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == "F"
    r.dia_final = -1
    assert r.dia_final == -1
    assert r.hora_final is None
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final is None
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.geracao_minima_50hz == 2500
    r.geracao_minima_50hz = -1
    assert r.geracao_minima_50hz == -1
    assert r.geracao_maxima_50hz == 7000
    r.geracao_maxima_50hz = -1
    assert r.geracao_maxima_50hz == -1
    assert r.geracao_minima_60hz == 2000
    r.geracao_minima_60hz = -1
    assert r.geracao_minima_60hz == -1
    assert r.geracao_maxima_60hz == 7000
    r.geracao_maxima_60hz = -1
    assert r.geracao_maxima_60hz == -1
    assert r.carga_ande == 1530
    r.carga_ande = -1
    assert r.carga_ande == -1


def test_registro_ia_entdados():
    m: MagicMock = mock_open(read_data="".join(MockIA))
    r = IA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "IV",
        "S",
        ["I", None, None],
        ["F", None, None],
        99999,
        99999,
    ]
    assert r.submercado_de == "IV"
    r.submercado_de = -1
    assert r.submercado_de == -1
    assert r.submercado_para == "S"
    r.submercado_para = -1
    assert r.submercado_para == -1
    assert r.dia_inicial == "I"
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == "F"
    r.dia_final = -1
    assert r.dia_final == -1
    assert r.hora_final is None
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final is None
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.capacidade_de == 99999
    r.capacidade_de = -1
    assert r.capacidade_de == -1
    assert r.capacidade_para == 99999
    r.capacidade_para = -1
    assert r.capacidade_para == -1


def test_registro_gp_entdados():
    m: MagicMock = mock_open(read_data="".join(MockGP))
    r = GP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [0.00001, 0.001]
    assert r.gap_pdd == 0.00001
    r.gap_pdd = 0
    assert r.gap_pdd == 0
    assert r.gap_milp == 0.001
    r.gap_milp = 0
    assert r.gap_milp == 0


def test_registro_ni_entdados():
    m: MagicMock = mock_open(read_data="".join(MockNI))
    r = NI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [0, 500]
    assert r.tipo_limite == 0
    r.tipo_limite = 1
    assert r.tipo_limite == 1
    assert r.iteracoes == 500
    r.iteracoes = 0
    assert r.iteracoes == 0


def test_registro_ve_entdados():
    m: MagicMock = mock_open(read_data="".join(MockVE))
    r = VE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        190,
        [11, 23, 1],
        [12, 0, 0],
        100.0,
    ]
    assert r.codigo == 190
    r.codigo = -1
    assert r.codigo == -1
    assert r.dia_inicial == 11
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 23
    r.hora_inicial = -1
    assert r.hora_inicial == -1
    assert r.meia_hora_inicial == 1
    r.meia_hora_inicial = -1
    assert r.meia_hora_inicial == -1
    assert r.dia_final == 12
    r.dia_final = -1
    assert r.dia_final == -1
    assert r.hora_final == 0
    r.hora_final = -1
    assert r.hora_final == -1
    assert r.meia_hora_final == 0
    r.meia_hora_final = -1
    assert r.meia_hora_final == -1
    assert r.volume == 100
    r.volume = -1
    assert r.volume == -1


def test_registro_fp_entdados():
    m: MagicMock = mock_open(read_data="".join(MockFP))
    r = FP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 5, 3, None, None, 10, None]
    assert r.codigo == 1
    r.codigo = -1
    assert r.codigo == -1
    assert r.tipo_tratamento_volume == 1
    r.tipo_tratamento_volume = 2
    assert r.tipo_tratamento_volume == 2
    assert r.numero_pontos_turbinamento == 5
    r.numero_pontos_turbinamento = 2
    assert r.numero_pontos_turbinamento == 2
    assert r.numero_pontos_volume == 3
    r.numero_pontos_volume = 2
    assert r.numero_pontos_volume == 2
    assert r.verifica_concavidade is None
    r.verifica_concavidade = 2
    assert r.verifica_concavidade == 2
    assert r.ajuste_minimos_quadrados is None
    r.ajuste_minimos_quadrados = 2
    assert r.ajuste_minimos_quadrados == 2
    assert r.comprimento_janela_volume == 10.0
    r.comprimento_janela_volume = -1
    assert r.comprimento_janela_volume == -1
    assert r.tolerancia_desvio is None
    r.tolerancia_desvio = -1
    assert r.tolerancia_desvio == -1


def test_registro_tx_entdados():
    m: MagicMock = mock_open(read_data="".join(MockTX))
    r = TX()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [12.0]
    assert r.taxa == 12.0
    r.taxa = 0
    assert r.taxa == 0


def test_registro_ez_entdados():
    m: MagicMock = mock_open(read_data="".join(MockEZ))
    r = EZ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [251, 55.0]
    assert r.uhe == 251
    r.uhe = 0
    assert r.uhe == 0
    assert r.volume == 55.0
    r.uhe = 0
    assert r.uhe == 0


def test_registro_r11_entdados():
    m: MagicMock = mock_open(read_data="".join(MockR11))
    r = R11()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        [11, 0, 0],
        ["F", None, None],
        98.26,
        0.50,
        2.0,
    ]
    assert r.dia_inicial == 11
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.cota_inicial == 98.26
    r.cota_inicial = -1
    assert r.cota_inicial == -1
    assert r.variacao_maxima_horaria == 0.50
    r.variacao_maxima_horaria = -1
    assert r.variacao_maxima_horaria == -1
    assert r.variacao_maxima_diaria == 2.0
    r.variacao_maxima_diaria = -1
    assert r.variacao_maxima_diaria == -1


def test_registro_cr_entdados():
    m: MagicMock = mock_open(read_data="".join(MockCR))
    r = CR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        "R11",
        6,
        7.6677112e01,
        2.8660334e-03,
        -1.0474654e-07,
        2.6583003e-12,
        -3.8245459e-17,
        2.8607867e-22,
        -8.6322234e-28,
    ]
    assert r.codigo_secao == 1
    r.codigo_secao = 40
    assert r.codigo_secao == 40
    assert r.nome_secao == "R11"
    r.nome_secao = 0
    assert r.nome_secao == 0
    assert r.grau == 6
    r.grau = 0
    assert r.grau == 0
    assert r.coeficiente_a0 == 7.6677112e01
    r.coeficiente_a0 = 0
    assert r.coeficiente_a0 == 0
    assert r.coeficiente_a1 == 2.8660334e-03
    r.coeficiente_a1 = 0
    assert r.coeficiente_a1 == 0
    assert r.coeficiente_a2 == -1.0474654e-07
    r.coeficiente_a2 = 0
    assert r.coeficiente_a2 == 0
    assert r.coeficiente_a3 == 2.6583003e-12
    r.coeficiente_a3 = 0
    assert r.coeficiente_a3 == 0
    assert r.coeficiente_a4 == -3.8245459e-17
    r.coeficiente_a4 = 0
    assert r.coeficiente_a4 == 0
    assert r.coeficiente_a5 == 2.8607867e-22
    r.coeficiente_a5 = 0
    assert r.coeficiente_a5 == 0
    assert r.coeficiente_a6 == -8.6322234e-28
    r.coeficiente_a6 = 0
    assert r.coeficiente_a6 == 0


def test_registro_secr_entdados():
    m: MagicMock = mock_open(read_data="".join(MockSECR))
    r = SECR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        "R11",
        66,
        1.03,
        83,
        1.17,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_secao == 1
    r.codigo_secao = 40
    assert r.codigo_secao == 40
    assert r.nome_secao == "R11"
    r.nome_secao = 0
    assert r.nome_secao == 0
    assert r.codigo_usina_montante_1 == 66
    r.codigo_usina_montante_1 = 0
    assert r.codigo_usina_montante_1 == 0
    assert r.fator_participacao_1 == 1.03
    r.fator_participacao_1 = 0
    assert r.fator_participacao_1 == 0
    assert r.codigo_usina_montante_2 == 83
    r.codigo_usina_montante_2 = 0
    assert r.codigo_usina_montante_2 == 0
    assert r.fator_participacao_2 == 1.17
    r.fator_participacao_2 = 0
    assert r.fator_participacao_2 == 0
    assert r.codigo_usina_montante_3 is None
    r.codigo_usina_montante_3 = 0
    assert r.codigo_usina_montante_3 == 0
    assert r.fator_participacao_3 is None
    r.fator_participacao_3 = 0
    assert r.fator_participacao_3 == 0
    assert r.codigo_usina_montante_4 is None
    r.codigo_usina_montante_4 = 0
    assert r.codigo_usina_montante_4 == 0
    assert r.fator_participacao_4 is None
    r.fator_participacao_4 = 0
    assert r.fator_participacao_4 == 0
    assert r.codigo_usina_montante_5 is None
    r.codigo_usina_montante_5 = 0
    assert r.codigo_usina_montante_5 == 0
    assert r.fator_participacao_5 is None
    r.fator_participacao_5 = 0
    assert r.fator_participacao_5 == 0


def test_registro_da_entdados():
    m: MagicMock = mock_open(read_data="".join(MockDA))
    r = DA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [230, [6, None, None], ["F", None, None], -10.5]
    assert r.codigo_usina == 230
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.dia_inicial == 6
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.taxa == -10.5
    r.taxa = -1
    assert r.taxa == -1


def test_registro_re_entdados():
    m: MagicMock = mock_open(read_data="".join(MockRE))
    r = RE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [16, [6, None, None], [13, 0, 0]]
    assert r.codigo_restricao == 16
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 6
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == 13
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final == 0
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final == 0
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2


def test_registro_lu_entdados():
    m: MagicMock = mock_open(read_data="".join(MockLU))
    r = LU()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [16, [6, 0, 0], ["F", None, None], 16, 63.8]
    assert r.codigo_restricao == 16
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 6
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.limite_inferior == 16
    r.limite_inferior = -1
    assert r.limite_inferior == -1
    assert r.limite_superior == 63.8
    r.limite_superior = -1
    assert r.limite_superior == -1


def test_registro_fh_entdados():
    m: MagicMock = mock_open(read_data="".join(MockFH))
    r = FH()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [16, [6, None, None], ["F", None, None], 155, None, 1]
    assert r.codigo_restricao == 16
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 6
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.codigo_usina == 155
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.conjunto is None
    r.conjunto = -1
    assert r.conjunto == -1
    assert r.coeficiente == 1
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_ft_entdados():
    m: MagicMock = mock_open(read_data="".join(MockFT))
    r = FT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [908, [12, None, None], ["F", None, None], 21, 1]
    assert r.codigo_restricao == 908
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 12
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.codigo_usina == 21
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.coeficiente == 1
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_fi_entdados():
    m: MagicMock = mock_open(read_data="".join(MockFI))
    r = FI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [908, [12, None, None], ["F", None, None], "FC", "N", 1]
    assert r.codigo_restricao == 908
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 12
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.submercado_de == "FC"
    r.submercado_de = -1
    assert r.submercado_de == -1
    assert r.submercado_para == "N"
    r.submercado_para = -1
    assert r.submercado_para == -1
    assert r.coeficiente == 1
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_fe_entdados():
    m: MagicMock = mock_open(read_data="".join(MockFE))
    r = FE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [912, [12, None, None], ["F", None, None], 601, 1]
    assert r.codigo_restricao == 912
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 12
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.codigo_contrato == 601
    r.codigo_contrato = -1
    assert r.codigo_contrato == -1
    assert r.coeficiente == 1
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_fr_entdados():
    m: MagicMock = mock_open(read_data="".join(MockFR))
    r = FR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [919, [12, None, None], ["F", None, None], 1358, 1]
    assert r.codigo_restricao == 919
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 12
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.codigo_usina == 1358
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.coeficiente == 1
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_fc_entdados():
    m: MagicMock = mock_open(read_data="".join(MockFC))
    r = FC()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [921, [12, None, None], ["F", None, None], 4, -1]
    assert r.codigo_restricao == 921
    r.codigo_restricao = -1
    assert r.codigo_restricao == -1
    assert r.dia_inicial == 12
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial is None
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial is None
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == "F"
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final is None
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final is None
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.codigo_demanda == 4
    r.codigo_demanda = -1
    assert r.codigo_demanda == -1
    assert r.coeficiente == -1
    r.coeficiente = 2
    assert r.coeficiente == 2


def test_registro_ci_entdados():
    m: MagicMock = mock_open(read_data="".join(MockCI))
    r = CI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        131,
        "E2POL1-I-F",
        7057,
        2,
        ["I", None, None],
        ["F", None, None],
        None,
        0,
        1575.0,
        0,
        None,
        None,
        None,
    ]


def test_registro_ce_entdados():
    m: MagicMock = mock_open(read_data="".join(MockCE))
    r = CE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        142,
        "E3POL4-E-F",
        7055,
        2,
        ["I", None, None],
        ["F", None, None],
        None,
        0,
        1575.0,
        0,
        None,
        None,
        None,
    ]


def test_registro_mh_entdados():
    m: MagicMock = mock_open(read_data="".join(MockMH))
    r = MH()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [34, 2, 3, [11, 0, 0], [13, 0, 0], 0]
    assert r.codigo_usina == 34
    r.codigo_usina = -1
    assert r.codigo_usina == -1
    assert r.codigo_conjunto == 2
    r.codigo_conjunto = -1
    assert r.codigo_conjunto == -1
    assert r.codigo_unidade == 3
    r.codigo_unidade = -1
    assert r.codigo_unidade == -1
    assert r.dia_inicial == 11
    r.dia_inicial = -1
    assert r.dia_inicial == -1
    assert r.hora_inicial == 0
    r.hora_inicial = 2
    assert r.hora_inicial == 2
    assert r.meia_hora_inicial == 0
    r.meia_hora_inicial = 2
    assert r.meia_hora_inicial == 2
    assert r.dia_final == 13
    r.dia_final = 0
    assert r.dia_final == 0
    assert r.hora_final == 0
    r.hora_final = 2
    assert r.hora_final == 2
    assert r.meia_hora_final == 0
    r.meia_hora_final = 2
    assert r.meia_hora_final == 2
    assert r.disponivel == 0
    r.disponivel = 2
    assert r.disponivel == 2


def test_registro_pe_entdados():
    m: MagicMock = mock_open(read_data="".join(MockPE))
    r = PE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [0.002, 1.0]
    assert r.penalidade_vertimento == 0.002
    r.penalidade_vertimento = 1
    assert r.penalidade_vertimento == 1
    assert r.fator_penalidade_violacao == 1
    r.fator_penalidade_violacao = 0
    assert r.fator_penalidade_violacao == 0


def test_registro_acvtfuga_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACVTFUGA))
    r = ACVTFUGA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [103, 1]
    assert r.uhe == 103
    r.uhe = 40
    assert r.uhe == 40
    assert r.influi == 1
    r.influi = 0
    assert r.influi == 0


def test_registro_acvolmax_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACVOLMAX))
    r = ACVOLMAX()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [38, 544.2]
    assert r.uhe == 38
    r.uhe = 40
    assert r.uhe == 40
    assert r.volume == 544.2
    r.volume = 0
    assert r.volume == 0


def test_registro_acvolmin_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACVOLMIN))
    r = ACVOLMIN()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [34, 15563]
    assert r.uhe == 34
    r.uhe = 40
    assert r.uhe == 40
    assert r.volume == 15563
    r.volume = 0
    assert r.volume == 0


def test_registro_acvsvert_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACVSVERT))
    r = ACVSVERT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [124, 200]
    assert r.uhe == 124
    r.uhe = 40
    assert r.uhe == 40
    assert r.volume == 200.0
    r.volume = 0
    assert r.volume == 0


def test_registro_acvmdesv_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACVMDESV))
    r = ACVMDESV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [124, 102]
    assert r.uhe == 124
    r.uhe = 40
    assert r.uhe == 40
    assert r.volume == 102.0
    r.volume = 0
    assert r.volume == 0


def test_registro_accotvaz_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACCOTVAZ))
    r = ACCOTVAZ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [288, 1, -8.635887e-19, None]
    assert r.uhe == 288
    r.uhe = 40
    assert r.uhe == 40
    assert r.ordem == 1
    r.ordem = 0
    assert r.ordem == 0
    assert r.coeficiente == -8.635887e-19
    r.coeficiente = -1
    assert r.coeficiente == -1
    assert r.polimonio is None
    r.polimonio = 0
    assert r.polimonio == 0


def test_registro_accotvol_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACCOTVOL))
    r = ACCOTVOL()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [252, 2, -6.59226600e-06]
    assert r.uhe == 252
    r.uhe = 40
    assert r.uhe == 40
    assert r.ordem == 2
    r.ordem = 0
    assert r.ordem == 0
    assert r.coeficiente == -6.59226600e-06
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_accottar_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACCOTTAR))
    r = ACCOTTAR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [252, 2, -6.59226600e-06]
    assert r.uhe == 252
    r.uhe = 40
    assert r.uhe == 40
    assert r.ordem == 2
    r.ordem = 0
    assert r.ordem == 0
    assert r.coeficiente == -6.59226600e-06
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_acnumcon_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACNUMCON))
    r = ACNUMCON()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [88, 1]
    assert r.uhe == 88
    r.uhe = 40
    assert r.uhe == 40
    assert r.numero_conjuntos == 1
    r.numero_conjuntos = 0
    assert r.numero_conjuntos == 0


def test_registro_acnumjus_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACNUMJUS))
    r = ACNUMJUS()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [34, 45]
    assert r.uhe == 34
    r.uhe = 40
    assert r.uhe == 40
    assert r.jusante == 45
    r.jusante = 0
    assert r.jusante == 0


def test_registro_acnumpos_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACNUMPOS))
    r = ACNUMPOS()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [305, 300]
    assert r.uhe == 305
    r.uhe = 40
    assert r.uhe == 40
    assert r.posto == 300
    r.posto = 0
    assert r.posto == 0


def test_registro_acjusena_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACJUSENA))
    r = ACJUSENA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [125, 131]
    assert r.uhe == 125
    r.uhe = 40
    assert r.uhe == 40
    assert r.aproveitamento == 131
    r.aproveitamento = 0
    assert r.aproveitamento == 0


def test_registro_acjusmed_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACJUSMED))
    r = ACJUSMED()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [275, 4.90]
    assert r.uhe == 275
    r.uhe = 40
    assert r.uhe == 40
    assert r.cota == 4.9
    r.cota = 0
    assert r.cota == 0


def test_registro_accofeva_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACCOFEVA))
    r = ACCOFEVA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [95, 10, 0]
    assert r.uhe == 95
    r.uhe = 40
    assert r.uhe == 40
    assert r.mes_coeficiente == 10
    r.mes_coeficiente = 0
    assert r.mes_coeficiente == 0
    assert r.coeficiente == 0
    r.coeficiente = -1
    assert r.coeficiente == -1


def test_registro_acnummaq_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACNUMMAQ))
    r = ACNUMMAQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [272, 1, 2]
    assert r.uhe == 272
    r.uhe = 40
    assert r.uhe == 40
    assert r.conjunto == 1
    r.conjunto = 0
    assert r.conjunto == 0
    assert r.maquinas == 2
    r.maquinas = -1
    assert r.maquinas == -1


def test_registro_acdesvio_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACDESVIO))
    r = ACDESVIO()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [314, 288, 9999999.0]
    assert r.uhe == 314
    r.uhe = 40
    assert r.uhe == 40
    assert r.jusante == 288
    r.jusante = 0
    assert r.jusante == 0
    assert r.limite_vazao == 9999999.0
    r.limite_vazao = -1
    assert r.limite_vazao == -1


def test_registro_acpotefe_entdados():
    m: MagicMock = mock_open(read_data="".join(MockACPOTEFE))
    r = ACPOTEFE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [272, 1, 10.0]
    assert r.uhe == 272
    r.uhe = 40
    assert r.uhe == 40
    assert r.conjunto == 1
    r.conjunto = 0
    assert r.conjunto == 0
    assert r.potencia == 10
    r.potencia = -1
    assert r.potencia == -1


def test_campos_nao_encontrados_entdados():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Entdados.read(".")
    assert d.sist(0) is None
    assert d.uh(0) is None
    assert d.ree(0) is None
    assert d.tm(0) is None
    assert d.rivar(0) is None
    assert d.rd is None
    assert d.tviag(0) is None
    assert d.ut(0, 0) is None
    assert d.usie(0) is None
    assert d.dp(0) is None
    assert d.de(0) is None
    assert d.cd(0, 0) is None
    assert d.pq(0) is None
    assert d.it is None
    assert d.ri() is None
    assert d.ia(0) is None
    assert d.gp is None
    assert d.ni is None
    assert d.ac(0, ACCOTVAZ) is None
    assert d.ve() is None
    assert d.fp() is None
    assert d.tx is None
    assert d.ez() is None
    assert d.r11() is None
    assert d.cr() is None
    assert d.re() is None
    assert d.lu() is None
    assert d.fh() is None
    assert d.ft() is None
    assert d.fi() is None
    assert d.fe() is None
    assert d.fr() is None
    assert d.fc() is None
    assert d.mh() is None
    assert d.pe is None


def test_campos_encontrados_entdados():
    m: MagicMock = mock_open(read_data="".join(MockEntDados))
    with patch("builtins.open", m):
        d = Entdados.read("./tests/mocks/arquivos/entdados.py")

    assert d.rd is not None
    assert d.rivar(999) is not None
    assert (
        d.tm(dia_inicial=11, hora_inicial=0, meia_hora_inicial=1) is not None
    )
    assert d.sist(1) is not None
    assert d.ree(1) is not None
    assert d.uh(1) is not None
    assert d.tviag(83) is not None
    assert d.ut(108) is not None
    assert d.usie(4) is not None
    assert d.dp(1) is not None
    assert d.de(1) is not None
    assert d.cd(1) is not None
    assert d.pq() is None
    assert d.it is not None
    assert d.ri() is not None
    assert d.ia("IV", "S") is not None
    assert d.gp is not None
    assert d.ac(38, modificacao=ACVOLMIN) is not None
    assert d.ac(45, modificacao=ACVMDESV) is not None
    assert d.ni is not None
    assert d.ve() is not None
    assert d.fp() is not None
    assert d.tx is not None
    assert d.ez is not None
    assert d.r11() is not None
    assert d.cr() is not None
    assert d.re() is not None
    assert d.lu() is not None
    assert d.fh() is not None
    assert d.ft() is not None
    assert d.fi() is not None
    assert d.fe() is not None
    assert d.fr() is not None
    assert d.fc() is not None
    assert d.mh() is not None
    assert d.pe is None


def test_eq_entdados():
    m: MagicMock = mock_open(read_data="".join(MockEntDados))
    with patch("builtins.open", m):
        d1 = Entdados.read("./tests/mocks/arquivos/entdados.py")
        d2 = Entdados.read("./tests/mocks/arquivos/entdados.py")
        assert d1 == d2


def test_neq_entdados():
    m: MagicMock = mock_open(read_data="".join(MockEntDados))
    with patch("builtins.open", m):
        d1 = Entdados.read("./tests/mocks/arquivos/entdados.py")
        d2 = Entdados.read("./tests/mocks/arquivos/entdados.py")
        d2.gp.gap_milp = 5
        assert d1 != d2


def test_leitura_escrita_entdados():
    m_leitura: MagicMock = mock_open(read_data="".join(MockEntDados))
    with patch("builtins.open", m_leitura):
        d1 = Entdados.read("./tests/mocks/arquivos/entdados.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/entdados.py")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Entdados.read("./tests/mocks/arquivos/entdados.py")
        assert d1 == d2
