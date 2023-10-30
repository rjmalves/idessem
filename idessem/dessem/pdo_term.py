from idessem.dessem.modelos.pdo_term import TabelaPdoTerm
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoTerm(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as unidades térmicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_TERM.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoTerm]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_TERM.DAT"
    ) -> "PdoTerm":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades térmicas.

        - estagio (`int`)
        - nome_patamar (`str`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_unidade (`int`)
        - nome_submercado (`str`)
        - geracao (`float`)
        - geracao_minima (`float`)
        - geracao_maxima (`float`)
        - capacidade (`float`)
        - status (`int`)
        - custo_linear (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
