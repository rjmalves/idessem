from idessem.dessem.modelos.pdo_elev import TabelaPdoElev
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoElev(ArquivoCSV):
    """
    Armazena os dados das saídas referentes às usinas elevatórias.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ELEV.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoElev]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referentes à operação das usinas elevatórias.

        - estagio (`int`)
        - nome_patamar (`int`),
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
        - bombeamento_minimo (`float`)
        - bombeamento (`float`)
        - bombeamento_maximo (`float`)
        - consumo (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
