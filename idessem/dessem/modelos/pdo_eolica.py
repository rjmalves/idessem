from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoEolica(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_EOLICA.
    """

    BEGIN_PATTERN = "-----;-------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=7),
            LiteralField(size=14),
            IntegerField(size=9),
            LiteralField(size=9),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=17, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "codigo_usina",
        "nome_usina",
        "barra",
        "submercado",
        "potencia",
        "fator_de_capacidade",
        "geracao_pre_definida",
        "geracao",
    ]
    END_PATTERN = ""
