from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoHidr(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_HIDR.
    """

    BEGIN_PATTERN = "----;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=4),
            LiteralField(size=8),
            IntegerField(size=4),
            LiteralField(size=14),
            LiteralField(size=4),
            IntegerField(size=5),
            IntegerField(size=7),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            LiteralField(size=5),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "patamar",
        "indiceUsina",
        "nomeUsina",
        "submercado",
        "conjunto",
        "unidade",
        "valorAgua",
        "volumeFinalHm3",
        "volumeFinalPerc",
        "vazaoIncrementalM3s",
        "vazaoIncrementalHm3",
        "vazaoMontanteM3s",
        "vazaoMontanteHm3",
        "vazaoMontanteTempoViagemM3s",
        "vazaoMontanteTempoViagemHm3",
        "vazaoDesviadaM3s",
        "vazaoDesviadaHm3",
        "vazaoEvaporadaM3s",
        "vazaoEvaporadaHm3",
        "vazaoUsoAlternativoM3s",
        "vazaoUsoAlternativoHm3",
        "vazaoTurbinadaM3s",
        "vazaoTurbinadaHm3",
        "vazaoTurbinadaMinimaM3s",
        "vazaoTurbinadaMinimaHm3",
        "vazaoTurbinadaMaximaM3s",
        "vazaoTurbinadaMaximaHm3",
        "engolimentoMaximoM3s",
        "engolimentoMaximoHm3",
        "vazaoVertidaM3s",
        "vazaoVertidaHm3",
        "geracao",
        "geracaoMaxima",
        "capacidade",
        "ld",
        "perdasHidraulicas",
        "alturaQueda",
    ]
    END_PATTERN = ""
