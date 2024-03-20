from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoReserva(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_RESERVA.
    """

    BEGIN_PATTERN = "-----;--------;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=8),
            IntegerField(size=5),
            LiteralField(size=14),
            LiteralField(size=5),
            IntegerField(size=5),
            IntegerField(size=4),
            FloatField(size=13, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "nome_patamar",
        "codigo_entidade",
        "nome_entidade",
        "tipo_entidade",
        "codigo_area",
        "codigo_conjunto",
        "reserva",
        "geracao",
        "reserva_minima",
        "multiplicador",
        "geracao_maxima",
    ]
    END_PATTERN = ""
