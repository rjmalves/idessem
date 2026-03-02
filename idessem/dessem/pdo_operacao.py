from idessem.dessem.modelos.pdo_operacao import (
    BlocoCustos,
    BlocoCortesAtivos,
    BlocoDiscretizacaoTempo,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
)
from cfinterface.files.blockfile import BlockFile
from typing import Any, Optional, Type, TypeVar
from datetime import datetime
import pandas as pd  # type: ignore[import-untyped]  # no pandas-stubs package
from cfinterface.components.block import Block


class PdoOperacao(BlockFile):
    """
    Armazena os dados de operação do DESSEM.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_OPERACAO.
    """

    BLOCKS = [
        VersaoModelo,
        DataEstudo,
        BlocoDiscretizacaoTempo,
        BlocoCustos,
        BlocoCortesAtivos,
    ]
    ENCODING = "iso-8859-1"
    T = TypeVar("T")

    def __init__(self, data: Any = ...) -> None:
        super().__init__(data)
        self.__custos_operacao = None

    def __concatena_blocos(self, bloco: Type[T]) -> Optional[pd.DataFrame]:
        """Adiciona uma coluna com o estágio de cada bloco."""
        frames: list[pd.DataFrame] = []
        for b in self.data.of_type(bloco):
            if isinstance(b.data, pd.DataFrame):
                frames.append(b.data)
        return pd.concat(frames, ignore_index=True) if frames else None

    @property
    def versao(self) -> Optional[str]:
        """A versão do modelo utilizada para executar o caso."""
        b = self.data.get_blocks_of_type(VersaoModelo)
        return b.data if isinstance(b, VersaoModelo) else None

    @property
    def data_estudo(self) -> Optional[datetime]:
        """A data base utilizada na configuração do estudo."""
        b = self.data.get_blocks_of_type(DataEstudo)
        return b.data if isinstance(b, DataEstudo) else None

    @property
    def discretizacao(self) -> pd.DataFrame:
        """Obtém tabela com informações referentes a discretização de tempo."""
        b = self.data.get_blocks_of_type(BlocoDiscretizacaoTempo)
        return b.data if isinstance(b, BlocoDiscretizacaoTempo) else None

    @property
    def custos_operacao(self) -> pd.DataFrame:
        """Obtém tabela com informações referentes aos custos de operação."""
        if self.__custos_operacao is None:
            self.__custos_operacao = self.__concatena_blocos(BlocoCustos)
        return self.__custos_operacao

    @property
    def cortes_ativos(self) -> pd.DataFrame:
        """Obtém tabela com informações referentes aos multiplicadores dos cortes."""
        b = self.data.get_blocks_of_type(BlocoCortesAtivos)
        return b.data if isinstance(b, BlocoCortesAtivos) else None
