from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField

from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoCmoBar(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_CMOBAR.
    """

    BEGIN_PATTERN = "------;-------;-------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            LiteralField(size=7),
            IntegerField(size=7),
            LiteralField(size=13),
            LiteralField(size=7),
            FloatField(size=13, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "nome_patamar",
        "codigo_barra",
        "nome_barra",
        "nome_submercado",
        "cmo",
    ]
    END_PATTERN = ""
