from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoEcoUsihPolin(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_ECO_USIH_POLIN.
    """

    BEGIN_PATTERN = "-----;--------------;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=5),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=7, decimal_digits=2),
            FloatField(size=21, decimal_digits=8),
            FloatField(size=7, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_usina",
        "nome_usina",
        "indice_coeficiente",
        "coeficiente_cota_volume",
        "coeficiente_area_cota",
        "cota_vazao_hjus1",
        "hjus1",
        "cota_vazao_hjus2",
        "hjus2",
        "cota_vazao_hjus3",
        "hjus3",
        "cota_vazao_hjus4",
        "hjus4",
        "cota_vazao_hjus5",
        "hjus5",
        "cota_vazao_hjus6",
        "hjus6",
    ]
    END_PATTERN = ""
