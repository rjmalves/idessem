from idessem.dessem.modelos.pdo_reserva import TabelaPdoReserva
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoReserva(ArquivoCSV):
    """
    Armazena os dados das saídas referentes a reserva de potência operativa.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_RESERVA.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoReserva]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_RESERVA.DAT"
    ) -> "PdoReserva":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a reserva de potência operativa.

        - estagio (`int`)
        - nome_patamar (`str`)
        - codigo_entidade (`int`)
        - nome_entidade (`str`)
        - tipo_entidade (`str`)
        - codigo_area (`int`)
        - codigo_conjunto (`int`)
        - reserva (`float`)
        - geracao (`float`)
        - reserva_minima (`float`)
        - multiplicador (`float`)
        - geracao_maxima (`float`)


        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
