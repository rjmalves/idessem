from idessem.dessem.modelos.pdo_oper_usih import TabelaPdoOperUsih
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoOperUsih(ArquivoCSV):
    """
    Armazena os dados das saídas referentes às unidades hidrelétricas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_OPER_USIH.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoOperUsih]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referentes à operação das usinas hidrelétricas.

        - estagio (`int`)
        - patamar (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
        - volume_util_inicial (`float`)
        - volume_util_inicial_p (`float`)
        - volume_util_final (`float`)
        - volume_util_final_p (`float`)
        - volume_util_maximo (`float`)
        - vazao_incremental_natural (`float`)
        - volume_incremental_natural (`float`)
        - vazao_retirada_para_usos_alternativos (`float`)
        - volume_retirado_para_usos_alternativos (`float`)
        - vazao_evaporada (`float`)
        - volume_evaporado (`float`)
        - vazao_montante (`float`)
        - volume_montante (`float`)
        - vazao_montante_periodos_passados (`float`)
        - volume_montante_periodos_passados (`float`)
        - vazao_turbinada (`float`)
        - vazao_turbinada_maxima (`float`)
        - engolimento_maximo (`float`)
        - volume_turbinado (`float`)
        - vazao_vertida (`float`)
        - volume_vertido (`float`)
        - vazao_desviada (`float`)
        - volume_desviado (`float`)
        - vazao_bombeada (`float`)
        - volume_bombeado (`float`)
        - taxa_enchimento_volume_morto (`float`)
        - volume_enchimento_volume_morto (`float`)
        - taxa_descarga_fundo (`float`)
        - volume_descaga_fundo (`float`)
        - geracao (`float`)
        - geracao_maxima (`float`)
        - geracao_minima (`float`)
        - potencia_instalada (`float`)
        - valor_agua (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
