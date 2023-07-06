from idessem.dessem.modelos.pdo_eco_fcfcortes import TabelaPdoEcoFcfCortes
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoEcoFcfCortes(ArquivoCSV):
    """
    Armazena os dados de eco dos dados lidos dos cortes da FCF.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_FCFCORTES.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoFcfCortes]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_ECO_FCFCORTES.DAT"
    ) -> "PdoEcoFcfCortes":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

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
