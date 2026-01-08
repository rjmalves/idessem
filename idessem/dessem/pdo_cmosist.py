from idessem.dessem.modelos.pdo_cmosist import TabelaPdoCmosist
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoCmosist(ArquivoCSV):
    """
    Armazena o custo marginal da operação (CMO) e o valor da variável
    dual associada à equação de atendimento à demanda ("Pi" da demanda)
    para cada estágio e cada submercado.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_CMOSIST.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoCmosist]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com o custo marginal da operação (CMO) e o valor
        da variável dual associada à equação de atendimento à demanda
        ("Pi" da demanda).

        - estagio (`int`)
        - nome_patamar (`str`)
        - nome_submercado (`str`)
        - cmo (`float`)
        - pi_demanda (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None

        """
        return self._tabela()
