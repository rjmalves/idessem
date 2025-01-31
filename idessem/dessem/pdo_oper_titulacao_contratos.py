from idessem.dessem.modelos.pdo_oper_titulacao_contratos import (
    TabelaPdoOperTitulacaoContratos,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoOperTitulacaoContratos(ArquivoCSV):
    """
    Armazena os dados das saídas referentes a titulação dos contratos de
    importação e exportação de energia.

    Essa classe lida com as informações de saída fornecidas pelo arquivo
    PDO_OPER_TITULACAO_CONTRATOS.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoOperTitulacaoContratos]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_OPER_TITULACAO_CONTRATOS.DAT"
    ) -> "PdoOperTitulacaoContratos":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a titulação dos contratos de energia.

        - estagio (`int`)
        - tipo_contrato (`str`)
        - codigo_contrato (`int`)
        - nome_contrato (`str`)
        - codigo_barra (`int`)
        - codigo_submercado (`int`)
        - titulacao_inflexibilidade (`float`)
        - custo_contrato (`float`)
        - geracao (`float`)
        - cmo (`float`)
        - cmb (`float`)
        - ordem_merito_total (`str`)
        - titulacao (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
