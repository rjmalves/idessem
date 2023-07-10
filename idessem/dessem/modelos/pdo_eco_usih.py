from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoEcoUsih(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_ECO_USIH,
    válido a partir da versão 19.4.2.
    """

    BEGIN_PATTERN = "-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=14),
            LiteralField(size=8),
            IntegerField(size=7),
            IntegerField(size=7),
            IntegerField(size=8),
            IntegerField(size=5),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            LiteralField(size=7),
            LiteralField(size=7),
            IntegerField(size=7),
            IntegerField(size=3),
            FloatField(size=15, decimal_digits=6),
            LiteralField(size=5),
            FloatField(size=7, decimal_digits=3),
            FloatField(size=8, decimal_digits=2),
            IntegerField(size=6),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_usina",
        "nome_usina",
        "submercado",
        "indice_usina_jusante",
        "indice_usina_desvio",
        "indice_usina_jusante_earm",
        "estagio_inicial",
        "volume_morto_inicial_hm3",
        "volume_morto_inicial_percentual",
        "volume_util_inicial_hm3",
        "volume_util_inicial_percentual",
        "volume_armazenado_minimo_hm3",
        "volume_armazenado_maximo_hm3",
        "volume_soleira_vertedouro_hm3",
        "volume_soleira_vertedouro_util_percentual",
        "volume_soleira_desvio_hm3",
        "volume_soleira_desvio_util_percentual",
        "volume_referencia_hm3",
        "tipo_reservatorio",
        "tipo_regularizacao",
        "flag_evaporacao",
        "numero_conjuntos",
        "produtibilidade_especifica",
        "tipo_perdas",
        "perdas_hidraulicas",
        "canal_fuga_medio",
        "influencia_vertimento_canal_fuga",
    ]
    END_PATTERN = ""


class TabelaPdoEcoUsih190301(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_ECO_USIH,
    válido a partir da versão 19.3.1.
    """

    BEGIN_PATTERN = "-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=14),
            LiteralField(size=8),
            IntegerField(size=7),
            IntegerField(size=7),
            IntegerField(size=8),
            IntegerField(size=5),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            LiteralField(size=7),
            IntegerField(size=7),
            IntegerField(size=3),
            FloatField(size=15, decimal_digits=6),
            LiteralField(size=5),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=8, decimal_digits=2),
            IntegerField(size=6),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_usina",
        "nome_usina",
        "submercado",
        "indice_usina_jusante",
        "indice_usina_desvio",
        "indice_usina_jusante_earm",
        "estagio_inicial",
        "volume_morto_inicial_hm3",
        "volume_morto_inicial_percentual",
        "volume_util_inicial_hm3",
        "volume_util_inicial_percentual",
        "volume_armazenado_minimo_hm3",
        "volume_armazenado_maximo_hm3",
        "volume_soleira_vertedouro_hm3",
        "volume_soleira_vertedouro_util_percentual",
        "volume_soleira_desvio_hm3",
        "volume_soleira_desvio_util_percentual",
        "volume_referencia_hm3",
        "tipo_regularizacao",
        "flag_evaporacao",
        "numero_conjuntos",
        "produtibilidade_especifica",
        "tipo_perdas",
        "perdas_hidraulicas",
        "canal_fuga_medio",
        "influencia_vertimento_canal_fuga",
    ]
    END_PATTERN = ""
