from idessem.dessem.modelos.des_log_relato import (
    BlocoVariaveisOtimizacao,
    BlocoTempoProcessamento,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
)
from cfinterface.files.blockfile import BlockFile
from typing import Optional, TypeVar
from datetime import datetime
import pandas as pd  # type: ignore


class DesLogRelato(BlockFile):
    """
    Armazena os dados referentes ao resultado do processamentdo do DESSEM.

    Essa classe lida com as informações de saída fornecidas pelo arquivo DES_LOG_RELATO.
    """

    BLOCKS = [
        BlocoTempoProcessamento,
        VersaoModelo,
        DataEstudo,
        BlocoVariaveisOtimizacao,
    ]
    ENCODING = "iso-8859-1"
    T = TypeVar("T")

    @property
    def versao(self) -> Optional[str]:
        """
        A versão do modelo utilizada para executar o caso.

        :return: A versão do modelo
        :rtype: str | None
        """
        b = self.data.get_blocks_of_type(VersaoModelo)
        if isinstance(b, VersaoModelo):
            return b.data
        return None

    @property
    def data_estudo(self) -> Optional[datetime]:
        """
        A data base utilizada na configuração do estudo.

        :return: A data como objeto
        :rtype: datetime | None
        """
        b = self.data.get_blocks_of_type(DataEstudo)
        if isinstance(b, DataEstudo):
            return b.data
        return None

    @property
    def tempo_processamento(self):
        """
        O tempo de processamento do estudo.

        :return: O tempo como objeto
        :rtype: timedelta | None
        """
        b = self.data.get_blocks_of_type(BlocoTempoProcessamento)
        if isinstance(b, BlocoTempoProcessamento):
            return b.data
        return None

    @property
    def variaveis_otimizacao(self) -> pd.DataFrame:
        """
        Obtém tabela com informações referente a otimização.

        - variaveis (`str`)
        - valor (`float`)

        :return: As variáveis como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoVariaveisOtimizacao)
        if isinstance(b, BlocoVariaveisOtimizacao):
            return b.data
        return None
