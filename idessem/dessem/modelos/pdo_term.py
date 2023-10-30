from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoTerm(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_TERM.
    """

    BEGIN_PATTERN = "----;-------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=4),
            LiteralField(size=7),
            IntegerField(size=4),
            LiteralField(size=13),
            IntegerField(size=4),
            LiteralField(size=4),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            LiteralField(size=5),
            FloatField(size=11, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "nome_patamar",
        "codigo_usina",
        "nome_usina",
        "codigo_unidade",
        "nome_submercado",
        "geracao",
        "geracao_minima",
        "geracao_maxima",
        "capacidade",
        "status",
        "custo_linear",
    ]
    END_PATTERN = ""
