from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaAvlDesvFpha(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo AVL_DESVFPHA.
    """

    BEGIN_PATTERN = "-----;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=15, decimal_digits=6),
            FloatField(size=7, decimal_digits=2),
            IntegerField(size=6),
            IntegerField(size=4),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "indiceUsina",
        "nomeUsina",
        "volumeMedioHm3",
        "volumeMedioPerc",
        "vazaoTurbinadaM3s",
        "vazaoVertidaM3s",
        "vazaoJusanteM3s",
        "vazaoLateralUsinaM3s",
        "vazaoLateralPostoM3s",
        "alturaJusante",
        "alturaMontante",
        "produtibilidaEspecifica",
        "perdasHidraulicas",
        "influenciaVertimentoCanalFuga",
        "afogamentoCanalFuga",
        "geracaoFph",
        "geracaoPl",
        "geracaoFpha",
        "desvioAbsolutoFphPl",
        "desvioPercentualFphPl",
        "desvioAbsolutoFphFpha",
        "desvioPercentualFphFpha",
    ]
    END_PATTERN = ""
