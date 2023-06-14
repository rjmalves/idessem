from idessem.dessem.modelos.pdo_eco_usih_polin import TabelaPdoEcoUsihPolin
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoEcoUsihPolin(ArquivoCSV):
    """
    Armazena os dados de eco dos polinômios referentes as usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_USIH_POLIN.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoUsihPolin]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_ECO_USIH_POLIN.DAT"
    ) -> "PdoEcoUsihPolin":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos polinômios utilizados
        para cálculo das grandezas das usinas hidrelétricas.

        - indice_usina (`int`)
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
