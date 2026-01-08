from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoCmosist(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_CMOSIST.
    """

    BEGIN_PATTERN = "------;-------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            LiteralField(size=7),
            LiteralField(size=6),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "nome_patamar",
        "nome_submercado",
        "cmo",
        "pi_demanda",
    ]
    END_PATTERN = ""
