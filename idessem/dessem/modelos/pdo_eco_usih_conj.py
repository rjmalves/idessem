from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoEcoUsihConj(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_ECO_USIH_CONJ.
    """

    BEGIN_PATTERN = "-----;--------------;---;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=3),
            IntegerField(size=5),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=7, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "codigo_usina",
        "nome_usina",
        "codigo_conjunto",
        "numero_unidades",
        "potencia_efetiva",
        "vazao_efetiva",
        "altura_efetiva",
    ]
    END_PATTERN = ""
