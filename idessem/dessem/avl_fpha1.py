from idessem.dessem.modelos.avl_fpha1 import (
    TabelaAvlFpha1,
    TabelaAvlFpha1v1903,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class AvlFpha1(ArquivoCSV):
    """
    Armazena os dados referentes aos coeficientes da função de produção das usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo AVL_FPHA1.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaAvlFpha1]
    VERSIONS = {
        "19.3": [VersaoModelo, DataEstudo, TabelaAvlFpha1v1903],
        "19.3.1": [VersaoModelo, DataEstudo, TabelaAvlFpha1],
    }
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos coeficientes da função de produção.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - segmento_fpha (`int`)
        - fator_correcao (`float`)
        - vazao_lateral_media (`float`)
        - rhs (`float`)
        - coeficiente_volume_util (`float`)
        - coeficiente_vazao_turbinada (`float`)
        - coeficiente_vazao_lateral (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
