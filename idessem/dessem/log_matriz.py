from idessem.dessem.modelos.log_matriz import TabelaLogMatriz
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class LogMatriz(ArquivoCSV):
    """
    Armazena os dados das saídas referentes ao processo iterativo de resolução.

    Essa classe lida com as informações de saída fornecidas pelo arquivo LOG_MATRIZ.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaLogMatriz]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="LOG_MATRIZ.DAT"
    ) -> "LogMatriz":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

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
