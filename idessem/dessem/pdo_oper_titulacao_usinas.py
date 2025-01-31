from idessem.dessem.modelos.pdo_oper_titulacao_usinas import (
    TabelaPdoOperTitulacaoUsinas,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoOperTitulacaoUsinas(ArquivoCSV):
    """
    Armazena os dados das saídas referentes a titulação das usinas térmicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo
    PDO_OPER_TITULACAO_USINAS.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoOperTitulacaoUsinas]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_OPER_TITULACAO_USINAS.DAT"
    ) -> "PdoOperTitulacaoUsinas":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a titulação das usinas térmicas.

        - estagio (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
        - geracao (`float`)
        - titulacao_ordem_merito (`float`)
        - titulacao_inflexibilidade (`float`)
        - geracao_unit_commitment (`float`)
        - geracao_tempo_off (`float`)
        - ordem_merito_total (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
