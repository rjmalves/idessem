from idessem.dessem.modelos.arquivos.arquivocsv import (
    ArquivoCSV,
    DataEstudo,
    VersaoModelo,
)
from idessem.dessem.modelos.pdo_cmobar import TabelaPdoCmoBar


class PdoCmoBar(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos custos marginais de operação por barra.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_CMOBAR.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoCmoBar]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referentes aos custos marginais de
        operação por barra.

        - estagio (`int`)
        - nome_patamar (`str`)
        - codigo_barra (`int`)
        - nome_barra (`str`)
        - nome_submercado (`str`)
        - cmo (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
