from idessem.dessem.modelos.pdo_aval_qmaxusih import (
    TabelaPdoAvalQmaxUsih,
    TabelaPdoAvalQmaxUsih2001,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoAvalQmaxUsih(ArquivoCSV):
    """
    Armazena os dados de avaliação do engolimento máximo das usinas hidrelétricas
    ao longo das iterações do DESSEM.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_AVAL_QMAXUSIH_XXX.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoAvalQmaxUsih]
    VERSIONS = {
        "20.1": [VersaoModelo, DataEstudo, TabelaPdoAvalQmaxUsih2001],
        "20.4": [VersaoModelo, DataEstudo, TabelaPdoAvalQmaxUsih],
    }
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_AVAL_QMAXUSIH.DAT"
    ) -> "PdoAvalQmaxUsih":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades hidráulicas.

        - estagio (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - volume_medio_percentual (`float`)
        - vazao_turbinada_m3s (`float`)
        - vazao_vertida_m3s (`float`)
        - altura_montante (`float`)
        - vazao_jusante_m3s (`float`)
        - altura_jusante (`float`)
        - altura_liquida (`float`)
        - vazao_turbinada_maxima_m3s (`float`)
        - engolimento_maximo_m3s (`float`)
        - geracao_maxima (`float`)


        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
