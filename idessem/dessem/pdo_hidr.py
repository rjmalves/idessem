from idessem.dessem.modelos.pdo_hidr import TabelaPdoHidr
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoHidr(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as unidades hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_HIDR.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoHidr]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades hidráulicas.

        - estagio (`int`)
        - nome_patamar (`str`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
        - conjunto (`int`)
        - unidade (`int`)
        - valor_agua (`float`)
        - volume_final_hm3 (`float`)
        - volume_final_percentual (`float`)
        - vazao_incremental_m3s (`float`)
        - vazao_incremental_hm3 (`float`)
        - vazao_montante_m3s (`float`)
        - vazao_montante_hm3 (`float`)
        - vazao_montante_tempo_viagem_m3s (`float`)
        - vazao_montante_tempo_viagem_hm3 (`float`)
        - vazao_desviada_m3s (`float`)
        - vazao_desviada_hm3 (`float`)
        - vazao_evaporada_m3s (`float`)
        - vazao_evaporada_hm3 (`float`)
        - vazao_uso_alternativo_m3s (`float`)
        - vazao_uso_alternativo_hm3 (`float`)
        - vazao_turbinada_m3s (`float`)
        - vazao_turbinada_hm3 (`float`)
        - vazao_turbinada_minima_m3s (`float`)
        - vazao_turbinada_minima_hm3 (`float`)
        - vazao_turbinada_maxima_m3s (`float`)
        - vazao_turbinada_maxima_hm3 (`float`)
        - engolimento_maximo_m3s (`float`)
        - engolimento_maximo_hm3 (`float`)
        - vazao_vertida_m3s (`float`)
        - vazao_vertida_hm3 (`float`)
        - geracao (`float`)
        - geracao_maxima (`float`)
        - capacidade (`float`)
        - status (`str`)
        - perdas_hidraulicas (`float`)
        - altura_queda (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
