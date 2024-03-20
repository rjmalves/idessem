from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoAvalQmaxUsih(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_AVAL_QMAXUSIH_XXX.
    """

    BEGIN_PATTERN = "-----;-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "codigo_usina",
        "nome_usina",
        "volume_medio_percentual",
        "vazao_turbinada_m3s",
        "vazao_vertida_m3s",
        "vazao_turbinada_maxima_m3s",
        "engolimento_maximo_m3s",
        "geracao_maxima",
    ]
    END_PATTERN = ""
