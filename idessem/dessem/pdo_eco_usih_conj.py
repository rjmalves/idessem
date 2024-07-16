from idessem.dessem.modelos.pdo_eco_usih_conj import (
    TabelaPdoEcoUsihConj,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoEcoUsihConj(ArquivoCSV):
    """
    Armazena os dados de eco referentes aos conjuntos das usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_USIH_CONJ.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoUsihConj]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_ECO_USIH_CONJ.DAT"
    ) -> "PdoEcoUsihConj":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

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
