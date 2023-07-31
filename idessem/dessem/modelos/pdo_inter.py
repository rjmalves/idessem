from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoInter(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_INTER.
    """

    BEGIN_PATTERN = "-----;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=8),
            IntegerField(size=7),
            LiteralField(size=8),
            LiteralField(size=10),
            FloatField(size=11, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "patamar",
        "indice_intercambio",
        "nome_submercado_de",
        "nome_submercado_para",
        "intercambio",
    ]
    END_PATTERN = ""
