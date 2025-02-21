from idessem.dessem.modelos.arquivos.arquivocsv import (
    ArquivoCSV,
    DataEstudo,
    VersaoModelo,
)
from idessem.dessem.modelos.log_inviab import TabelaLogInviab


class LogInviab(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as violações de restrições.

    Essa classe lida com as informações de saída fornecidas pelo arquivo LOG_INVIAB.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaLogInviab]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referentes aos custos marginais de
        operação por barra.

        - estagio (`int`)
        - restricao (`str`)
        - violacao (`float`)
        - unidade (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
