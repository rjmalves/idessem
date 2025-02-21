from idessem.dessem.modelos.pdo_eco_usih_conj import (
    TabelaPdoEcoUsihConj,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoEcoUsihConj(ArquivoCSV):
    """
    Armazena os dados de eco referentes aos conjuntos das usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_USIH_CONJ.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoUsihConj]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos conjuntos de unidades
        geradoras das usinas hidrelétricas.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_conjunto (`int`)
        - numero_unidades (`int`)
        - potencia_efetiva (`float`)
        - vazao_efetiva (`float`)
        - altura_efetiva (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
