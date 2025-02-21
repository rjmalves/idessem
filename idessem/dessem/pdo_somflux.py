from idessem.dessem.modelos.arquivos.arquivocsv import (
    ArquivoCSV,
    DataEstudo,
    VersaoModelo,
)
from idessem.dessem.modelos.pdo_somflux import TabelaPdoSomFlux


class PdoSomFlux(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as restrições de somatório de fluxo.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_SOMFLUX.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoSomFlux]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referentes as restrições de somatório
        de fluxos.

        - estagio (`int`)
        - indice_restricao (`int`)
        - nome_patamar (`str`)
        - restricao_violada (`str`)
        - restricao_liberada (`str`)
        - codigo_restricao (`int`)
        - nome_restricao (`str`)
        - codigo_barra_de (`int`)
        - codigo_barra_para (`int`)
        - indice_circuito (`int`)
        - valor (`float`)
        - limite_inferior (`float`)
        - limite_superior (`float`)
        - multiplicador (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
