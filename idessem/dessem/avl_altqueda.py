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
        - indiceUsina (`int`)
        - nomeUsina (`str`)
        - alturaMontante (`float`)
        - alturaJusante (`float`)
        - alturaLiquida (`float`)
        - vazaoDefluenteM3s (`float`)
        - problema (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()