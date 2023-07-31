from idessem.dessem.modelos.pdo_inter import TabelaPdoInter
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoInter(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos intercâmbios.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_INTER.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoInter]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_INTER.DAT"
    ) -> "PdoInter":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos intercâmbios.

        - estagio (`int`)
        - patamar (`str`)
        - indice_intercambio (`int`)
        - nome_submercado_de (`str`)
        - nome_submercado_para (`str`)
        - intercambio (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
