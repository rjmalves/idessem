from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaAvlDesvFpha(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo AVL_DESVFPHA,
    válido a partir da versão 19.4.2.
    """

    BEGIN_PATTERN = "-----;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=3),
            FloatField(size=9, decimal_digits=3),
            FloatField(size=15, decimal_digits=6),
            LiteralField(5),
            FloatField(size=7, decimal_digits=3),
            IntegerField(size=6),
            IntegerField(size=4),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "indice_usina",
        "nome_usina",
        "volume_medio_hm3",
        "volume_medio_percentual",
        "vazao_incremental_m3s",
        "vazao_turbinada_m3s",
        "vazao_vertida_m3s",
        "vazao_jusante_m3s",
        "vazao_lateral_usina_m3s",
        "vazao_lateral_posto_m3s",
        "altura_jusante",
        "altura_montante",
        "produtibilidade_especifica",
        "tipo_perdas",
        "perdas_hidraulicas",
        "influencia_vertimento_canal_fuga",
        "afogamento_canal_fuga",
        "potencia_instalada",
        "geracao_fph",
        "geracao_pl",
        "geracao_fpha",
        "desvio_absoluto_fph_pl",
        "desvio_percentual_fph_pl",
        "desvio_absoluto_fph_fpha",
        "desvio_percentual_fph_fpha",
    ]
    END_PATTERN = ""


class TabelaAvlDesvFpha190300(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo AVL_DESVFPHA,
    válido a partir da versão 19.3.
    """

    BEGIN_PATTERN = "-----;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=15, decimal_digits=6),
            FloatField(size=7, decimal_digits=2),
            IntegerField(size=6),
            IntegerField(size=4),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "indice_usina",
        "nome_usina",
        "volume_medio_hm3",
        "volume_medio_percentual",
        "vazao_turbinada_m3s",
        "vazao_vertida_m3s",
        "vazao_jusante_m3s",
        "vazao_lateral_usina_m3s",
        "vazao_lateral_posto_m3s",
        "altura_jusante",
        "altura_montante",
        "produtibilidade_especifica",
        "perdas_hidraulicas",
        "influencia_vertimento_canal_fuga",
        "afogamento_canal_fuga",
        "geracao_fph",
        "geracao_pl",
        "geracao_fpha",
        "desvio_absoluto_fph_pl",
        "desvio_percentual_fph_pl",
        "desvio_absoluto_fph_fpha",
        "desvio_percentual_fph_fpha",
    ]
    END_PATTERN = ""
