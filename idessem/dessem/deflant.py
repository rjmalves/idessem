from typing import List, Optional, Type, TypeVar, Union

import pandas as pd  # type: ignore
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile

from idessem.dessem.modelos.deflant import DEFANT


class Deflant(RegisterFile):
    """
    Armazena os dados de defluências da usinas hidrelétricas anteriores
    ao início do estudo, para consideração do tempo de viagem, no DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `deflant.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [DEFANT]

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

    def defant(
        self,
        codigo_usina_montante: Optional[int] = None,
        codigo_elemento_jusante: Optional[int] = None,
        tipo_elemento_jusante: Optional[str] = None,
        defluencia: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[DEFANT, List[DEFANT], pd.DataFrame]]:
        """
        Obtém um registro que especifica as defluências anteriores
         ao início do estudo para consideração dos tempos de viagem
          descritas pelo :class:`Deflant`.

        :param codigo_usina_montante: Índice da UHE a montante com tempo de viagem
        :type codigo_usina_montante: int | None
        :param codigo_elemento_jusante: Índice do elemento a jusante
        :type codigo_elemento_jusante: int | None
        :param tipo_elemento_jusante: Tipo do elemento a jusante (seção ou UHE)
        :type tipo_elemento_jusante: str |
        :param defluencia: Defluência
        :type defluencia: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DEFANT` | list[:class:`DEFANT`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            DEFANT,
            codigo_usina_montante=codigo_usina_montante,
            codigo_elemento_jusante=codigo_elemento_jusante,
            tipo_elemento_jusante=tipo_elemento_jusante,
            defluencia=defluencia,
            df=df,
        )
