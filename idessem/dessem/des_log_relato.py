from idessem.dessem.modelos.des_log_relato import (
    BlocoVariaveisOtimizacao,
    BlocoTempoProcessamento,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
)
from cfinterface.files.blockfile import BlockFile
from typing import Optional, Type, TypeVar
from datetime import datetime
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="DES_LOG_RELATO.DAT"
    ) -> "DesLogRelato":
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
    def tempo_processamento(self):
        """
        O tempo de processamento do estudo.

        :return: O tempo como objeto
        :rtype: timedelta | None
        """
        b = self._bloco_por_tipo(BlocoTempoProcessamento, 0)
        if b is not None:
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
        b = self._bloco_por_tipo(BlocoVariaveisOtimizacao, 0)
        if b is not None:
            return b.data
        return None
