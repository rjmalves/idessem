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
    ACVTFUGA,
    ACVOLMAX,
    ACVOLMIN,
    ACVSVERT,
    ACVMDESV,
    ACCOTVAZ,
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
    MockACVTFUGA,
    MockACVOLMAX,
    MockACVOLMIN,
    MockACVSVERT,
    MockACVMDESV,
    MockACCOTVAZ,
    MockEntDados,
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
    assert d.ac(0, ACCOTVAZ) is None
    # assert d.ct(0, 0) is None
    # assert d.dp(0, 0) is None
    # assert d.ac(0, ACNUMCON, mes="", revisao=0, ano=0) is None
    # assert d.cd(0, 0) is None
    # assert d.tx is None
    # assert d.gp is None
    # assert d.ni is None
    # assert d.dt is None
    # assert d.re(0) is None
    # assert d.lu(0, 0) is None
    # assert d.vi(0) is None
    # assert d.ir("") is None
    # assert d.rt("") is None
    # assert d.fc("") is None
    # assert d.ti(0) is None
    # assert d.fp(0, 0) is None
    # assert d.ve(0) is None
    # assert d.hv(0) is None
    # assert d.lv(0, 0) is None
    # assert d.hq(0) is None
    # assert d.lq(0, 0) is None
    # assert d.he(0, 0) is None
    # assert d.cm(0) is None


def test_campos_encontrados_entdados():
    m: MagicMock = mock_open(read_data="".join(MockEntDados))
    with patch("builtins.open", m):
        d = Entdados.read("./tests/mocks/arquivos/entdados.py")

    assert d.sist(1) is not None
    assert d.uh(1) is not None
    assert d.ree(1) is not None
    assert (
        d.tm(dia_inicial=11, hora_inicial=0, meia_hora_inicial=1) is not None
    )
    assert d.rivar(999) is not None
    assert d.rd is not None
    assert d.tviag(83) is not None
    assert d.ut(108) is not None
    assert d.usie(4) is not None
    assert d.dp(1) is not None
    assert d.de(1) is not None
    assert d.cd(1) is not None
    assert d.it is not None
    assert d.ri() is not None
    assert d.ia("IV", "S") is not None
    assert d.gp is not None
    assert d.ac(38, modificacao=ACVOLMIN) is not None
    assert d.ac(45, modificacao=ACVMDESV) is not None


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
