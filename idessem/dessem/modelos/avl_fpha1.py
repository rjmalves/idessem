from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaAvlFpha1(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo AVL_FPHA1.
    """

    BEGIN_PATTERN = "-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=7),
            FloatField(size=9, decimal_digits=5),
            FloatField(size=8, decimal_digits=2),
            FloatField(size=12, decimal_digits=4),
            FloatField(size=13, decimal_digits=6),
            FloatField(size=13, decimal_digits=6),
            FloatField(size=13, decimal_digits=6),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_usina",
        "nome_usina",
        "segmento_fpha",
        "fator_correcao",
        "vazao_lateral_media",
        "rhs",
        "coeficiente_volume_util",
        "coeficiente_vazao_turbinada",
        "coeficiente_vazao_lateral",
    ]
    END_PATTERN = "-----;--------------;"


class TabelaAvlFpha1v1903(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo AVL_FPHA1.
    Válido a partir da versão 19.3.
    """

    BEGIN_PATTERN = "-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=7),
            FloatField(size=9, decimal_digits=5),
            FloatField(size=12, decimal_digits=4),
            FloatField(size=13, decimal_digits=6),
            FloatField(size=13, decimal_digits=6),
            FloatField(size=13, decimal_digits=6),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_usina",
        "nome_usina",
        "segmento_fpha",
        "fator_correcao",
        "rhs",
        "coeficiente_volume_util",
        "coeficiente_vazao_turbinada",
        "coeficiente_vazao_lateral",
    ]
    END_PATTERN = "-----;--------------;"
