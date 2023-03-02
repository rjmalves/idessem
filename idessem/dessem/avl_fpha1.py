from idessem.dessem.modelos.avl_fpha1 import TabelaAvlFpha1
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
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="AVL_FPHA1.DAT"
    ) -> "AvlFpha1":
        return cls.read(diretorio, nome_arquivo)

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
