from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.line import Line
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV


class TabelaPdoOperUsih(TabelaCSV):
    """
    Bloco com as informações da tabela do arquivo PDO_OPER_USIH.
    """

    BEGIN_PATTERN = "-----;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            LiteralField(size=8),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=20, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "patamar",
        "codigo_usina",
        "nome_usina",
        "nome_submercado",
        "volume_util_inicial",
        "volume_util_inicial_p",
        "volume_util_final",
        "volume_util_final_p",
        "volume_util_maximo",
        "vazao_incremental_natural",
        "volume_incremental_natural",
        "vazao_retirada_para_usos_alternativos",
        "volume_retirado_para_usos_alternativos",
        "vazao_evaporada",
        "volume_evaporado",
        "vazao_montante",
        "volume_montante",
        "vazao_montante_periodos_passados",
        "volume_montante_periodos_passados",
        "vazao_turbinada",
        "vazao_turbinada_maxima",
        "engolimento_maximo",
        "volume_turbinado",
        "vazao_vertida",
        "volume_vertido",
        "vazao_desviada",
        "volume_desviado",
        "vazao_bombeada",
        "volume_bombeado",
        "taxa_enchimento_volume_morto",
        "volume_enchimento_volume_morto",
        "taxa_descarga_fundo",
        "volume_descaga_fundo",
        "geracao",
        "geracao_maxima",
        "geracao_minima",
        "potencia_instalada",
        "valor_agua",
    ]
    END_PATTERN = ""
