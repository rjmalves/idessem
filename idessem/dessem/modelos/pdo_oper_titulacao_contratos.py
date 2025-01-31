from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoOperTitulacaoContratos(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_OPER_TITULACAO_CONTRATOS.
    """

    BEGIN_PATTERN = "-----;----;-----;-----------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=4),
            IntegerField(size=5),
            LiteralField(size=11),
            IntegerField(size=6),
            IntegerField(size=4),
            FloatField(size=17, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=17, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            LiteralField(size=13),
            LiteralField(size=30),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "tipo_contrato",
        "codigo_contrato",
        "nome_contrato",
        "codigo_barra",
        "codigo_submercado",
        "titulacao_inflexibilidade",
        "custo_contrato",
        "geracao",
        "cmo",
        "cmb",
        "ordem_merito_total",
        "titulacao",
    ]
    END_PATTERN = ""
