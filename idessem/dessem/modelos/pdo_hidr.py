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
        "indice_usina",
        "nome_usina",
        "submercado",
        "conjunto",
        "unidade",
        "valor_agua",
        "volume_final_hm3",
        "volume_final_percentual",
        "vazao_incremental_m3s",
        "vazao_incremental_hm3",
        "vazao_montante_m3s",
        "vazao_montante_hm3",
        "vazao_montante_tempo_viagem_m3s",
        "vazao_montante_tempo_viagem_hm3",
        "vazao_desviada_m3s",
        "vazao_desviada_hm3",
        "vazao_evaporada_m3s",
        "vazao_evaporada_hm3",
        "vazao_uso_alternativo_m3s",
        "vazao_uso_alternativo_hm3",
        "vazao_turbinada_m3s",
        "vazao_turbinada_hm3",
        "vazao_turbinada_minima_m3s",
        "vazao_turbinada_minima_hm3",
        "vazao_turbinada_maxima_m3s",
        "vazao_turbinada_maxima_hm3",
        "engolimento_maximo_m3s",
        "engolimento_maximo_hm3",
        "vazao_vertida_m3s",
        "vazao_vertida_hm3",
        "geracao",
        "geracao_maxima",
        "capacidade",
        "ld",
        "perdas_hidraulicas",
        "altura_queda",
    ]
    END_PATTERN = ""
