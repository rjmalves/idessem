import warnings

# Para compatibilidade - até versão 1.0.0
from os.path import join

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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="LOG_INVIAB.DAT"
    ) -> "LogInviab":
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
        - restricao (`str`)
        - violacao (`float`)
        - unidade (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
