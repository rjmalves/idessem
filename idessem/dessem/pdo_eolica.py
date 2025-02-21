from idessem.dessem.modelos.pdo_eolica import TabelaPdoEolica
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoEolica(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as usinas renovaveis.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_EOLICA.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEolica]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das usinas renováveis.

        - estagio (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - barra (`int`)
        - nome_submercado (`str`)
        - potencia (`float`)
        - fator_de_capacidade (`float`)
        - geracao_pre_definida (`float`)
        - geracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
