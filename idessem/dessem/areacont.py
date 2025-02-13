import warnings

# Para compatibilidade - até versão 1.0.0
from os.path import join
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

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="areacont.dat") -> "Areacont":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="areacont.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    @property
    def area(self) -> Optional[pd.DataFrame]:
        """
        Tabela com as condições iniciais das UTEs.

        - codigo_area (`int`)
        - nome_area (`str`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoArea)
        if isinstance(b, BlocoArea):
            return b.data[1]

    @area.setter
    def area(self, valor: pd.DataFrame):
        b = self.data.get_blocks_of_type(BlocoArea)
        if b is not None:
            b.data[1] = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def usina(self) -> Optional[pd.DataFrame]:
        """
        Tabela com os limites e condições oeprativas das unidades.

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

    @usina.setter
    def usina(self, valor: pd.DataFrame):
        b = self.data.get_blocks_of_type(BlocoUsina)
        if b is not None:
            b.data[1] = valor
        else:
            raise ValueError("Campo não lido")
