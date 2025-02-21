from typing import Optional, TypeVar

import pandas as pd  # type: ignore
from cfinterface.files.sectionfile import SectionFile

from idessem.dessem.modelos.desselet import (
    BlocoCasosBase,
    BlocoCasosModificacao,
)


class Desselet(SectionFile):
    """
    Armazena os dados para a rede elétrica nos estágios do DESSEM.

    Esta classe lida com informações de entrada fornecidas ao DESSEM e
    que podem ser modificadas através do arquivo `desselet.dat`.

    """

    T = TypeVar("T")

    SECTIONS = [BlocoCasosBase, BlocoCasosModificacao]

    @property
    def dados_casos_base(self) -> Optional[pd.DataFrame]:
        """
        Tabela com os dados dos casos base.

        - indice_caso_base (`int`)
        - nome_caso_base (`str`)
        - arquivo (`str`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_sections_of_type(BlocoCasosBase)
        if isinstance(b, BlocoCasosBase):
            return b.data
        return None

    @dados_casos_base.setter
    def dados_casos_base(self, valor: pd.DataFrame):
        b = self.data.get_sections_of_type(BlocoCasosBase)
        if isinstance(b, BlocoCasosBase):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def dados_modificacao(self) -> Optional[pd.DataFrame]:
        """
        Tabela com os dados de modificação dos casos base por estágio.

        - codigo_estagio (`int`)
        - nome_estagio (`str`)
        - ano (`int`)
        - mes (`int`)
        - dia (`int`)
        - hora (`int`)
        - minuto (`int`)
        - duracao_estagio (`float`)
        - indice_caso_base (`int`)
        - arquivo (`str`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_sections_of_type(BlocoCasosModificacao)
        if isinstance(b, BlocoCasosModificacao):
            return b.data
        return None

    @dados_modificacao.setter
    def dados_modificacao(self, valor: pd.DataFrame):
        b = self.data.get_sections_of_type(BlocoCasosModificacao)
        if isinstance(b, BlocoCasosModificacao):
            b.data = valor
        else:
            raise ValueError("Campo não lido")
