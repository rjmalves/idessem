from typing import Optional, TypeVar

import pandas as pd  # type: ignore
from cfinterface.files.blockfile import BlockFile

from idessem.dessem.modelos.areacont import BlocoArea, BlocoUsina


class Areacont(BlockFile):
    """
    Armazena os dados de entrada do DESSEM referentes às
    áreas de controle.

    """

    T = TypeVar("T")

    BLOCKS = [BlocoArea, BlocoUsina]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @property
    def area(self) -> Optional[pd.DataFrame]:
        """
        Tabela com as areas de controle.

        - codigo_area (`int`)
        - nome_area (`str`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoArea)
        if isinstance(b, BlocoArea):
            return b.data[1]
        return None

    @area.setter
    def area(self, valor: pd.DataFrame):
        b = self.data.get_blocks_of_type(BlocoArea)
        if isinstance(b, BlocoArea):
            b.data[1] = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def usina(self) -> Optional[pd.DataFrame]:
        """
        Tabela com a composição das áreas de controle.

        - codigo_area (`int`)
        - codigo_conjunto (`int`)
        - tipo_componente (`str`)
        - codigo_componente (`str`)
        - nome_componente (`str`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoUsina)
        if isinstance(b, BlocoUsina):
            return b.data[1]
        return None

    @usina.setter
    def usina(self, valor: pd.DataFrame):
        b = self.data.get_blocks_of_type(BlocoUsina)
        if isinstance(b, BlocoUsina):
            b.data[1] = valor
        else:
            raise ValueError("Campo não lido")
