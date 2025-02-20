from typing import List, Optional, Type, TypeVar, Union

import pandas as pd  # type: ignore
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile

from idessem.dessem.modelos.respot import LM, RP


class Respot(RegisterFile):
    """
    Armazena os dados de requisitos de reserva de potência mínima por área de
    controle no DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `respot.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [RP, LM]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    def __registros_ou_df(
        self, t: Type[T], **kwargs
    ) -> Optional[Union[T, List[T], pd.DataFrame]]:
        if kwargs.get("df"):
            return self._as_df(t)
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    def rp(
        self,
        codigo_area: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[RP, List[RP], pd.DataFrame]]:
        """
        Obtém um registro que especifica a janela de tempo da área
        de controle de reserva de potência descritas pelo :class:`Respot`.

        :param codigo_area: Índice da área de controle
        :type codigo_area: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RP` | list[:class:`RP`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RP,
            codigo_area=codigo_area,
            df=df,
        )

    def lm(
        self,
        codigo_area: Optional[int] = None,
        limite_inferior: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[RP, List[RP], pd.DataFrame]]:
        """
        Obtém um registro que especifica o requisito de reserva de potência
        mínimo para a área de controle descritas pelo :class:`Respot`.

        :param codigo_area: Índice da área de controle
        :type codigo_area: int | None
        :param limite_inferior: Reserva de potência mínima
        :type limite_inferior: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LM` | list[:class:`LM`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            LM,
            codigo_area=codigo_area,
            limite_inferior=limite_inferior,
            df=df,
        )
