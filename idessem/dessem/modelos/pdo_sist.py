from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoSist(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_SIST.
    """

    BEGIN_PATTERN = "------;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            LiteralField(size=8),
            LiteralField(size=6),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            LiteralField(size=12),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "patamar",
        "submercado",
        "cmo",
        "demanda",
        "perdas",
        "geracaoPequenasUsinas",
        "geracaoFixaBarra",
        "geracaoRenovavel",
        "geracaoHidraulica",
        "geracaoTermica",
        "consumoElevatorias",
        "importacao",
        "exportacao",
        "corteCarga",
        "saldo",
        "recebimento",
        "geracaoTermicaMinima",
        "geracaoTermicaMaxima",
        "energiaArmazenada",
    ]
    END_PATTERN = ""
