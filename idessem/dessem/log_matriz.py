from idessem.dessem.modelos.log_matriz import TabelaLogMatriz
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class LogMatriz(ArquivoCSV):
    """
    Armazena os dados das saídas referentes ao processo iterativo de resolução.

    Essa classe lida com as informações de saída fornecidas pelo arquivo LOG_MATRIZ.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaLogMatriz]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente ao processo iterativo de convergência.

        - iteracao (`int`)
        - tipo (`str`)
        - variaveis (`int`)
        - variaveis_inteiras (`int`)
        - restricoes (`int`)
        - restricoes_inteiras (`int`)
        - elementos (`int`)
        - tempo_min (`float`)
        - funcao_objetivo (`float`)
        - status (`int`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
