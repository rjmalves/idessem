from idessem.dessem.modelos.avl_altqueda import TabelaAvlAltQueda
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class AvlAltQueda(ArquivoCSV):
    """
    Armazena os dados das saídas referentes a altura de queda de usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo AVL_ALTQUEDA.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaAvlAltQueda]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="AVL_ALTQUEDA.DAT"
    ) -> "AvlAltQueda":
        return cls.read(diretorio, nome_arquivo)

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a altura de queda.

        - estagio (`int`)
        - iteracao (`int`)
        - ides (`str`)
        - patamar (`str`)
        - indice_usina (`int`)
        - nome_usina (`str`)
        - altura_montante (`float`)
        - altura_jusante (`float`)
        - altura_liquida (`float`)
        - vazao_defluente_m3s (`float`)
        - problema (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
