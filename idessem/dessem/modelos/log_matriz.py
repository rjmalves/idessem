from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaLogMatriz(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo LOG_MATRIZ.
    """

    BEGIN_PATTERN = "----;------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=4),
            LiteralField(size=12),
            IntegerField(size=9),
            IntegerField(size=9),
            IntegerField(size=9),
            IntegerField(size=9),
            IntegerField(size=9),
            FloatField(size=9, decimal_digits=1),
            FloatField(size=17, decimal_digits=3),
            IntegerField(size=5),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "iteracao",
        "tipo",
        "variaveis",
        "variaveis_inteiras",
        "restricoes",
        "restricoes_inteiras",
        "elementos",
        "tempo_min",
        "funcao_objetivo",
        "status",
    ]
    END_PATTERN = ""
