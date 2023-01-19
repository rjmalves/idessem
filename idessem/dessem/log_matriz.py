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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="LOG_MATRIZ.DAT"
    ) -> "LogMatriz":
        return cls.read(diretorio, nome_arquivo)

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente ao processo iterativo de convergência.

        - iteracao (`int`)
        - tipo (`str`)
        - variaveis (`int`)
        - variaveisInteiras (`int`)
        - restricoes (`int`)
        - restricoesInteiras (`int`)
        - elementos (`int`)
        - tempoMin (`float`)
        - funcaoObjetivo (`float`)
        - status (`int`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
