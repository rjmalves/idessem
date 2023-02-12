from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaAvlAltQueda(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo AVL_ALTQUEDA.
    """

    BEGIN_PATTERN = "------;------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            IntegerField(size=6),
            LiteralField(size=4),
            LiteralField(size=7),
            IntegerField(size=6),
            LiteralField(size=14),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=19, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "iteracao",
        "ides",
        "patamar",
        "indice_usina",
        "nome_usina",
        "altura_montante",
        "altura_jusante",
        "altura_liquida",
        "vazao_defluente_m3s",
        "problema",
    ]
    END_PATTERN = ""
