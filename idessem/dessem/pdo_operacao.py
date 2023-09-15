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
from typing import Optional, Type, TypeVar
from datetime import datetime
import pandas as pd  # type: ignore
from cfinterface.components.block import Block

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__custos_operacao = None

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_OPERACAO.DAT"
    ) -> "PdoOperacao":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

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

    def __concatena_blocos(self, bloco: Type[T]) -> Optional[pd.DataFrame]:
        """
        Adiciona uma coluna com o estágio de cada bloco.
        :param bloco: O tipo de bloco
        :type bloco: Type[T]
        :return: O DataFrame com os estágios
        :rtype: pd.DataFrame
        """
        df = None
        for i, b in enumerate(self.data.of_type(bloco)):
            if not isinstance(b, Block):
                continue
            df_estagio = b.data
            if df is None:
                df = df_estagio
            else:
                df = pd.concat([df, df_estagio], ignore_index=True)
        if df is not None:
            return df
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

    @property
    def discretizacao(self) -> pd.DataFrame:
        """
        Obtém tabela com informações referentes a discretização
        de tempo do estudo.

        - estagio (`int`)
        - data_inicial (`datetime`)
        - data_final (`datetime`)
        - duracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self._bloco_por_tipo(BlocoDiscretizacaoTempo, 0)
        if b is not None:
            return b.data
        return None

    @property
    def custos_operacao(self) -> pd.DataFrame:
        """
        Obtém tabela com informações referentes aos custos de operação.

        - estagio (`int`)
        - custo_presente (`float`)
        - custo_futuro (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        if self.__custos_operacao is None:
            self.__custos_operacao = self.__concatena_blocos(BlocoCustos)
        return self.__custos_operacao

    @property
    def cortes_ativos(self) -> pd.DataFrame:
        """
        Obtém tabela com informações referentes aos multiplicadores dos
        cortes.

        - estagio (`int`)
        - indice_corte (`int`)
        - multiplicador (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self._bloco_por_tipo(BlocoCortesAtivos, 0)
        if b is not None:
            return b.data
        return None
