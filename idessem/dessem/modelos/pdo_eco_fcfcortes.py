from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoEcoFcfCortes(TabelaCSV):
    """
    Bloco com as informações dos cortes da FCF do arquivo PDO_ECO_FCFCORTES e
    PDO_ECO_FCFCORTES_AJUSTES, válido a partir da versão 20.1.
    """

    BEGIN_PATTERN = "------;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            LiteralField(size=8),
            IntegerField(size=6),
            LiteralField(size=15),
            LiteralField(size=7),
            IntegerField(size=5),
            IntegerField(size=5),
            FloatField(size=30, decimal_digits=8),
            LiteralField(size=16),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_corte",
        "tipo_entidade",
        "indice_entidade",
        "nome_entidade",
        "tipo_coeficiente",
        "indice_lag",
        "indice_patamar",
        "valor_coeficiente",
        "unidade",
    ]
    END_PATTERN = ""


class TabelaPdoEcoFcfCortes19(TabelaCSV):
    """
    Bloco com as informações dos cortes da FCF do arquivo PDO_ECO_FCFCORTES e
    PDO_ECO_FCFCORTES_AJUSTES, válido a partir da versão 19.
    """

    BEGIN_PATTERN = "------;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=6),
            LiteralField(size=8),
            IntegerField(size=6),
            LiteralField(size=15),
            LiteralField(size=7),
            IntegerField(size=5),
            IntegerField(size=5),
            FloatField(size=24, decimal_digits=7),
            LiteralField(size=16),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_corte",
        "tipo_entidade",
        "indice_entidade",
        "nome_entidade",
        "tipo_coeficiente",
        "indice_lag",
        "indice_patamar",
        "valor_coeficiente",
        "unidade",
    ]
    END_PATTERN = ""
