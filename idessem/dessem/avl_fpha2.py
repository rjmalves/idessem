from idessem.dessem.modelos.avl_fpha2 import TabelaAvlFpha2
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
)
from cfinterface.files.blockfile import BlockFile
from typing import Optional, TypeVar
import pandas as pd  # type: ignore
from datetime import datetime

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class AvlFpha2(BlockFile):
    """
    Armazena os dados referentes aos desvios da função de produção das usinas hidráulicas
    nos planos de volume armazenado e vazão turbinada (V-Q).

    Essa classe lida com as informações de saída fornecidas pelo arquivo AVL_FPHA2.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaAvlFpha2]
    ENCODING = "iso-8859-1"

    T = TypeVar("T")

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__df_completo: Optional[pd.DataFrame] = None

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="AVL_FPHA2.DAT"
    ) -> "AvlFpha2":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações de desvios da função de produção contida
        no arquivo AVL_FPHA2.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - volume_armazenado_percentual (`float`)
        - vazao_turbinada_m3s (`float`)
        - desvio_percentual (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """

        if self.__df_completo is None:
            tabelas = self.data.of_type(TabelaAvlFpha2)
            tabelas_validas = [t.data for t in tabelas if t is not None]
            self.__df_completo = pd.concat(
                [t for t in tabelas_validas if isinstance(t, pd.DataFrame)],
                ignore_index=True,
            )
        return self.__df_completo

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
