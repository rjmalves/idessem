from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoOperTerm(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_OPER_TERM.
    """

    BEGIN_PATTERN = "-----;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            IntegerField(size=6),
            LiteralField(size=14),
            LiteralField(size=8),
            IntegerField(size=8),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "codigo_usina",
        "codigo_unidade",
        "nome_usina",
        "nome_submercado",
        "barra",
        "geracao",
        "custo_linear",
        "cmo",
        "cmb",
    ]
    END_PATTERN = ""
