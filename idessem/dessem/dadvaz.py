from datetime import datetime
from typing import Optional, TypeVar

import pandas as pd  # type: ignore
from cfinterface.files.sectionfile import SectionFile

from idessem.dessem.modelos.dadvaz import (
    BlocoDadosHorizonte,
    BlocoDataInicioEstudo,
    BlocoVazoes,
)


class Dadvaz(SectionFile):
    """
    Armazena os dados de início do estudo, configuração do horizonte e acoplamento,
    e de vazão das usinas hidrelétricas no DESSEM.

    Esta classe lida com informações de entrada fornecidas ao DESSEM e
    que podem ser modificadas através do arquivo `dadvaz.dat`.

    """

    T = TypeVar("T")

    SECTIONS = [BlocoDataInicioEstudo, BlocoDadosHorizonte, BlocoVazoes]

    @property
    def data_inicio(self) -> Optional[datetime]:
        """
        A data de referência para realização do estudo

        :return: A data
        :rtype: datetime | None
        """
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            return b.data_inicio
        return None

    @data_inicio.setter
    def data_inicio(self, n: datetime):
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            b.data_inicio = n

    @property
    def dia_semana_inicial(self) -> Optional[int]:
        """
        O código para o dia da semana inicial (1=sex,...,7=sex)

        :return: O código do dia
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            return b.dia_semana_inicial
        return None

    @dia_semana_inicial.setter
    def dia_semana_inicial(self, n: int):
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            b.dia_semana_inicial = n

    @property
    def semana_acoplamento_fcf(self) -> Optional[int]:
        """
        O índice da semana da FCF acoplada

        :return: O código do dia
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            return b.semana_acoplamento_fcf
        return None

    @semana_acoplamento_fcf.setter
    def semana_acoplamento_fcf(self, n: int):
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            b.semana_acoplamento_fcf = n

    @property
    def numero_semanas(self) -> Optional[int]:
        """
        O número de semanas no estudo

        :return: O código do dia
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            return b.numero_semanas
        return None

    @numero_semanas.setter
    def numero_semanas(self, n: int):
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            b.numero_semanas = n

    @property
    def considera_periodo_simulacao(self) -> Optional[int]:
        """
        O flag que indica presença de período de simulação

        :return: O código do dia
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            return b.considera_periodo_simulacao
        return None

    @considera_periodo_simulacao.setter
    def considera_periodo_simulacao(self, n: int):
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            b.considera_periodo_simulacao = n

    @property
    def vazoes(self) -> Optional[pd.DataFrame]:
        """
        Tabela com as vazões das usinas.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - tipo_dado (`int`)
        - dia_inicial (`str`)
        - hora_inicial (`int`)
        - meia_hora_inicial (`int`)
        - dia_final (`str`)
        - hora_final (`int`)
        - meia_hora_final (`int`)
        - vazao  (`float`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_sections_of_type(BlocoVazoes)
        if isinstance(b, BlocoVazoes):
            return b.data
        return None

    @vazoes.setter
    def vazoes(self, valor: pd.DataFrame):
        b = self.data.get_sections_of_type(BlocoVazoes)
        if isinstance(b, BlocoVazoes):
            b.data = valor
        else:
            raise ValueError("Campo não lido")
