from idessem.dessem.modelos.avl_fpha1 import (
    TabelaAvlFpha1,
    TabelaAvlFpha1v1903,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="AVL_FPHA1.DAT"
    ) -> "AvlFpha1":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos coeficientes da função de produção.

        - indice_usina (`int`)
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
