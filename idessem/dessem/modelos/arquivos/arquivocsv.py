from idessem.dessem.modelos.blocos.versaomodelo import VersaoModelo
from idessem.dessem.modelos.blocos.dataestudo import DataEstudo
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV

from cfinterface.files.blockfile import BlockFile
from datetime import datetime
import pandas as pd  # type: ignore
from typing import TypeVar, Optional


class ArquivoCSV(BlockFile):
    """
    Modelo de arquivo baseado em blocos específico para o formato
    dos arquivos de saída .CSV do DESSEM. Espera conter
    a implementação de três blocos específicos:

    - Versão do modelo
    - Data do estudo
    - Tabela de dados

    Os dois primeiros são genéricos, mas o terceiro deve ser
    implementado para cada arquivo específico a ser lido.
    """

    BLOCKS = [VersaoModelo, DataEstudo]
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

    def _tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(TabelaCSV)
        if isinstance(b, TabelaCSV):
            return b.data
        return None
