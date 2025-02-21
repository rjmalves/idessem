from idessem.dessem.modelos.pdo_eco_fcfcortes import (
    TabelaPdoEcoFcfCortes,
    TabelaPdoEcoFcfCortes19,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoEcoFcfCortes(ArquivoCSV):
    """
    Armazena os dados de eco dos dados lidos dos cortes da FCF.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_FCFCORTES.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoFcfCortes]
    VERSIONS = {
        "19": [VersaoModelo, DataEstudo, TabelaPdoEcoFcfCortes19],
        "20.1": [VersaoModelo, DataEstudo, TabelaPdoEcoFcfCortes],
    }
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações dos cortes da FCF.

        - indice_corte (`int`)
        - tipo_entidade (`str`)
        - indice_entidade (`int`)
        - nome_entidade (`str`)
        - tipo_coeficiente (`str`)
        - indice_lag (`int`)
        - indice_patamar (`int`)
        - valor_coeficiente (`float`)
        - unidade (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
