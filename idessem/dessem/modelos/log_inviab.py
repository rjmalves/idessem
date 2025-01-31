from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField

from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaLogInviab(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo LOG_INVIAB.
    """

    BEGIN_PATTERN = (
        "------;------------------------------------;---------------;"
    )
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            LiteralField(size=36),
            FloatField(size=15, decimal_digits=5),
            LiteralField(size=9),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "restricao",
        "violacao",
        "unidade",
    ]
    END_PATTERN = ""
