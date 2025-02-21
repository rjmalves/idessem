from idessem.dessem.modelos.pdo_term import TabelaPdoTerm
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoTerm(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as unidades térmicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_TERM.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoTerm]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades térmicas.

        - estagio (`int`)
        - nome_patamar (`str`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_unidade (`int`)
        - nome_submercado (`str`)
        - geracao (`float`)
        - geracao_minima (`float`)
        - geracao_maxima (`float`)
        - capacidade (`float`)
        - status (`int`)
        - custo_linear (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
