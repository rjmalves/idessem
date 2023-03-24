from idessem.dessem.modelos.operut import (
    BlocoInitUT,
)

from cfinterface.files.blockfile import BlockFile
from typing import Type, TypeVar, Optional
import pandas as pd  # type: ignore


class Operut(BlockFile):
    """
    Armazena os dados de entrada do DESSEM referentes às
    configurações da operação das usinas térmelétricas.

    """

    T = TypeVar("T")

    BLOCKS = [BlocoInitUT]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="operut.dat") -> "Operut":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="operut.dat"):
        self.write(diretorio, nome_arquivo)

    def __bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
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
    def condicoes_iniciais(self) -> Optional[pd.DataFrame]:
        """
        Tabela com as condições iniciais das UTEs.

        - indice_usina (`int`)
        - nome_usina (`str`)
        - indice_unidade_geradora (`int`)
        - estado (`int`)
        - geracao_inicial (`float`)
        - tempo_permanencia_estado (`int`)
        - meia_hora (`int`)
        - rampa_acionamento_desligamento (`int`)
        - titulacao_inicial (`int`)
        - inflexibilidade_titulacao (`float`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoInitUT, 0)
        if b is not None:
            return b.data[1]
        return None

    @condicoes_iniciais.setter
    def condicoes_iniciais(self, valor: pd.DataFrame):
        b = self.__bloco_por_tipo(BlocoInitUT, 0)
        if b is not None:
            b.data[1] = valor
        else:
            raise ValueError("Campo não lido")
