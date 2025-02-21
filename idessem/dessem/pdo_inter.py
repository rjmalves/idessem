from idessem.dessem.modelos.pdo_inter import TabelaPdoInter
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoInter(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos intercâmbios.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_INTER.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoInter]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos intercâmbios.

        - estagio (`int`)
        - nome_patamar (`str`)
        - indice_intercambio (`int`)
        - nome_submercado_de (`str`)
        - nome_submercado_para (`str`)
        - intercambio (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
