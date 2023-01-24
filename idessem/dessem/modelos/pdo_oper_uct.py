from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoOperUct(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_OPER_UCT.
    """

    BEGIN_PATTERN = "-----;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            IntegerField(size=6),
            LiteralField(size=14),
            LiteralField(size=8),
            IntegerField(size=8),
            IntegerField(size=7),
            IntegerField(size=8),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=3),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            IntegerField(size=5),
            IntegerField(size=5),
            IntegerField(size=3),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=10, decimal_digits=1),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            LiteralField(size=30),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            IntegerField(size=5),
            FloatField(size=12, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "indiceUsina",
        "unidade",
        "nomeUsina",
        "submercado",
        "barra",
        "numeroMaximoOscilacoes",
        "flagGeracaoMinimaMaxima",
        "geracaoMinima",
        "geracaoMinimaUnidade",
        "geracaoMaxima",
        "geracaoMaximaUnidade",
        "geracaoMinimaAcionamento",
        "tempoOn",
        "tempoOff",
        "status",
        "geracao",
        "tempo",
        "custoLinear",
        "custoPartidaUnidade",
        "cmo",
        "cmb",
        "variavelDual",
        "titulacao",
        "rampaSubida",
        "rampaDescida",
        "unidadeEquivalente",
        "rampaTransicao",
    ]
    END_PATTERN = ""
