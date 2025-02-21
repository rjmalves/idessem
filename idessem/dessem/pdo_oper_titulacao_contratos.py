from idessem.dessem.modelos.pdo_oper_titulacao_contratos import (
    TabelaPdoOperTitulacaoContratos,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoOperTitulacaoContratos(ArquivoCSV):
    """
    Armazena os dados das saídas referentes a titulação dos contratos de
    importação e exportação de energia.

    Essa classe lida com as informações de saída fornecidas pelo arquivo
    PDO_OPER_TITULACAO_CONTRATOS.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoOperTitulacaoContratos]
    ENCODING = "iso-8859-1"

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
