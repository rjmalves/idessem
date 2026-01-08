from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoElev(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_ELEV.
    """

    BEGIN_PATTERN = "------;-------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            LiteralField(size=7),
            IntegerField(size=6),
            LiteralField(size=14),
            LiteralField(size=6),
            FloatField(size=13, decimal_digits=1),
            FloatField(size=13, decimal_digits=1),
            FloatField(size=13, decimal_digits=1),
            FloatField(size=14, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "nome_patamar",
        "codigo_usina",
        "nome_usina",
        "nome_submercado",
        "bombeamento_minimo",
        "bombeamento",
        "bombeamento_maximo",
        "consumo",
    ]
    END_PATTERN = ""
