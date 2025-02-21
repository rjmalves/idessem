from idessem.dessem.modelos.avl_estatfpha import (
    BlocoDesvios,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
)
from cfinterface.files.blockfile import BlockFile
from typing import Optional, TypeVar
from datetime import datetime
import pandas as pd  # type: ignore


class AvlEstatFpha(BlockFile):
    """
    Armazena os dados referentes a estatísticas da função de produção do DESSEM.

    Essa classe lida com as informações de saída fornecidas pelo arquivo AVL_ESTAT_FPHA.
    """

    BLOCKS = [
        VersaoModelo,
        DataEstudo,
        BlocoDesvios,
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
    def estatisticas_desvios(self) -> pd.DataFrame:
        """
        Obtém tabela com informações referentes às estatísticas
        de desvios da função de produção.

        - variaveis (`str`)
        - valor (`float`)

        :return: As variáveis como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoDesvios)
        if isinstance(b, BlocoDesvios):
            return b.data
        return None
