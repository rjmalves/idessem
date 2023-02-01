from idessem.dessem.modelos.blocos.versaomodelo import VersaoModelo
from idessem.dessem.modelos.blocos.dataestudo import DataEstudo
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV

from cfinterface.files.blockfile import BlockFile
from datetime import datetime
import pandas as pd  # type: ignore
from typing import Type, TypeVar, Optional


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

    def _bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.

        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        :return: O gerador de blocos, se houver
        :rtype: Optional[Generator[T], None, None]
        """
        try:
            return next(
                b
                for i, b in enumerate(self.data.of_type(bloco))
                if i == indice
            )
        except StopIteration:
            return None

    @property
    def versao(self) -> Optional[str]:
        """
        A versão do modelo utilizada para executar o caso.

        :return: A versão do modelo
        :rtype: str | None
        """
        b = self._bloco_por_tipo(VersaoModelo, 0)
        if b is not None:
            return b.data
        return None

    @property
    def data_estudo(self) -> Optional[datetime]:
        """
        A data base utilizada na configuração do estudo.

        :return: A data como objeto
        :rtype: datetime | None
        """
        b = self._bloco_por_tipo(DataEstudo, 0)
        if b is not None:
            return b.data
        return None

    def _tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self._bloco_por_tipo(TabelaCSV, 0)
        if b is not None:
            return b.data
        return None
