import warnings

# Para compatibilidade - até versão 1.0.0
from os.path import join

from idessem.dessem.modelos.arquivos.arquivocsv import (
    ArquivoCSV,
    DataEstudo,
    VersaoModelo,
)
from idessem.dessem.modelos.pdo_cmobar import TabelaPdoCmoBar


class PdoCmoBar(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos custos marginais de operação por barra.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_CMOBAR.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoCmoBar]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="PDO_CMOBAR.DAT") -> "PdoCmoBar":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referentes aos custos marginais de
        operação por barra.

        - estagio (`int`)
        - nome_patamar (`str`)
        - codigo_barra (`int`)
        - nome_barra (`str`)
        - nome_submercado (`str`)
        - cmo (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
