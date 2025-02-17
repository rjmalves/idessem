from idessem.dessem.modelos.dadvaz import BlocoDataInicioEstudo, BlocoDadosHorizonte, BlocoVazoes

from cfinterface.files.sectionfile import SectionFile
from typing import TypeVar, Optional
import pandas as pd  # type: ignore


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
    def hora(self) -> Optional[int]:
        """
        A hora de referência para realização do estudo

        :return: A hora
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            return b.hora
        return None

    @hora.setter
    def hora(self, n: int):
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            b.data = n


    @property
    def dia(self) -> Optional[int]:
        """
        O dia de referência para realização do estudo

        :return: O dia
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            return b.dia
        return None

    @dia.setter
    def dia(self, n: int):
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            b.data = n

    @property
    def mes(self) -> Optional[int]:
        """
        O mês de referência para realização do estudo

        :return: O mês
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            return b.mes
        return None

    @mes.setter
    def mes(self, n: int):
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            b.data = n

    @property
    def ano(self) -> Optional[int]:
        """
        O ano de referência para realização do estudo

        :return: O ano
        :rtype: int | None
        """
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            return b.ano
        return None

    @ano.setter
    def ano(self, n: int):
        b = self.data.get_sections_of_type(BlocoDataInicioEstudo)
        if isinstance(b, BlocoDataInicioEstudo):
            b.data = n

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
            b.data = n

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
            b.data = n

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
            b.data = n

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
    def considera_periodo_simulacaonumero_semanas(self, n: int):
        b = self.data.get_sections_of_type(BlocoDadosHorizonte)
        if isinstance(b, BlocoDadosHorizonte):
            b.data = n


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