from idessem.dessem.modelos.pdo_sist import TabelaPdoSist
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoSist(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos submercados.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_SIST.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoSist]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_SIST.DAT"
    ) -> "PdoSist":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação por submercado.

        - estagio (`int`)
        - patamar (`float`)
        - submercado (`str`)
        - cmo (`float`)
        - demanda (`float`)
        - perdas (`str`)
        - geracao_pequenas_usinas (`float`)
        - geracao_fixa_barra (`float`)
        - geracao_renovavel (`float`)
        - geracao_hidraulica (`float`)
        - geracao_termica (`float`)
        - consumo_elevatorias (`float`)
        - importacao (`float`)
        - exportacao (`float`)
        - corte_carga (`float`)
        - saldo (`float`)
        - recebimento (`float`)
        - geracao_termica_minima (`float`)
        - geracao_termica_maxima (`float`)
        - energia_armazenada (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
