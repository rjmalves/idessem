from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoOperTitulacaoUsinas(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_OPER_TITULACAO_USINAS.
    """

    BEGIN_PATTERN = "-----;-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            LiteralField(size=8),
            FloatField(size=8, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=17, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            LiteralField(size=13),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "codigo_usina",
        "nome_usina",
        "nome_submercado",
        "geracao",
        "titulacao_ordem_merito",
        "titulacao_inflexibilidade",
        "geracao_unit_commitment",
        "geracao_tempo_off",
        "ordem_merito_total",
    ]
    END_PATTERN = ""
