from idessem.dessem.modelos.pdo_sist import TabelaPdoSist
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoSist(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos submercados.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_SIST.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoSist]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação por submercado.

        - estagio (`int`)
        - nome_patamar (`str`)
        - nome_submercado (`str`)
        - cmo (`float`)
        - demanda (`float`)
        - perdas (`str`)
        - geracao_pequenas_usinas (`float`)
        - geracao_fixa_barra (`float`)
        - geracao_renovavel (`float`)
        - geracao_hidraulica (`float`)
        - geracao_termica (`float`)
        - consumo_elevatorias (`float`)
        - importacao (`float`)
        - exportacao (`float`)
        - corte_carga (`float`)
        - saldo (`float`)
        - recebimento (`float`)
        - geracao_termica_minima (`float`)
        - geracao_termica_maxima (`float`)
        - energia_armazenada (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
