from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField

from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoSomFlux(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_SOMFLUX.
    """

    BEGIN_PATTERN = "-----;------;-------;-;-;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            LiteralField(size=7),
            LiteralField(size=1),
            LiteralField(size=1),
            IntegerField(size=5),
            LiteralField(size=50),
            IntegerField(size=8),
            IntegerField(size=8),
            IntegerField(size=3),
            FloatField(size=11, decimal_digits=3),
            FloatField(size=11, decimal_digits=3),
            FloatField(size=11, decimal_digits=3),
            FloatField(size=11, decimal_digits=3),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "indice_restricao",
        "nome_patamar",
        "restricao_violada",
        "restricao_liberada",
        "codigo_restricao",
        "nome_restricao",
        "codigo_barra_de",
        "codigo_barra_para",
        "indice_circuito",
        "valor",
        "limite_inferior",
        "limite_superior",
        "multiplicador",
    ]
    END_PATTERN = ""
