from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoOperTviagCalha(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_OPER_TVIAG_CALHA.
    """

    BEGIN_PATTERN = "-----;-----;-------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            FloatField(size=5, decimal_digits=1),
            IntegerField(size=7),
            LiteralField(size=14),
            LiteralField(size=9),
            IntegerField(size=10),
            LiteralField(size=14),
            FloatField(size=8, decimal_digits=2),
            LiteralField(size=7),
            FloatField(size=8, decimal_digits=1),
            FloatField(size=8, decimal_digits=2),
            FloatField(size=10, decimal_digits=1),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "duracao",
        "codigo_usina_montante",
        "nome_usina_montante",
        "tipo_elemento_jusante",
        "codigo_elemento_jusante",
        "nome_elemento_jusante",
        "tempo_viagem",
        "tipo_tempo_viagem",
        "tempo_restante",
        "percentual_volume_calha",
        "volume_calha_hm3",
    ]
    END_PATTERN = ""
