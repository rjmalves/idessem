from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaaPdoOperLpp(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_OPER_LPP.
    """

    BEGIN_PATTERN = "-----;--------;-------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=8),
            IntegerField(size=7),
            IntegerField(size=9),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            IntegerField(size=8),
            FloatField(size=12, decimal_digits=2),
            LiteralField(size=12),
            LiteralField(size=12),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=4),
            FloatField(size=12, decimal_digits=8),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "codigo_lpp",
        "codigo_dref",
        "codigo_re",
        "valor",
        "limite_superior",
        "indice_corte_ativo",
        "coeficiente_linear",
        "codigo_controladora",
        "tipo_controladora",
        "valor_parametro",
        "coeficiente_angular",
        "multiplicador",
    ]
    END_PATTERN = ""
