from idessem.dessem.modelos.pdo_eco_usih_polin import TabelaPdoEcoUsihPolin
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoEcoUsihPolin(ArquivoCSV):
    """
    Armazena os dados de eco dos polinômios referentes as usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_USIH_POLIN.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoUsihPolin]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos polinômios utilizados
        para cálculo das grandezas das usinas hidrelétricas.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - indice_coeficiente (`int`)
        - coeficiente_cota_volume (`float`)
        - coeficiente_area_cota (`float`)
        - cota_vazao_hjus1 (`float`)
        - hjus1 (`float`)
        - cota_vazao_hjus2 (`float`)
        - hjus2 (`float`)
        - cota_vazao_hjus3 (`float`)
        - hjus3 (`float`)
        - cota_vazao_hjus4 (`float`)
        - hjus4 (`float`)
        - cota_vazao_hjus5 (`float`)
        - hjus5 (`float`)
        - cota_vazao_hjus6 (`float`)
        - hjus6 (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
