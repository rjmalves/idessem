from idessem.dessem.modelos.pdo_sist import TabelaPdoSist
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


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
        return cls.read(diretorio, nome_arquivo)

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
        - geracaoPequenasUsinas (`float`)
        - geracaoFixaBarra (`float`)
        - geracaoRenovavel (`float`)
        - geracaoHidraulica (`float`)
        - geracaoTermica (`float`)
        - consumoElevatorias (`float`)
        - importacao (`float`)
        - exportacao (`float`)
        - corteCarga (`float`)
        - saldo (`float`)
        - recebimento (`float`)
        - geracaoTermicaMinima (`float`)
        - geracaoTermicaMaxima (`float`)
        - energiaArmazenada (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
