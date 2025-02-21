from idessem.dessem.modelos.renovaveis import (
    EOLICA,
    EOLICABARRA,
    EOLICASUBM,
    EOLICAGERACAO,
)
import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile
from typing import Type, List, Optional, TypeVar, Union
from cfinterface.components.register import Register


class Renovaveis(RegisterFile):
    """
    Armazena os dados de entrada do DESSEM associados a geração de renováveis
    e fontes não simuladas.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `renovaveis.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [EOLICAGERACAO, EOLICASUBM, EOLICABARRA, EOLICA]

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

    def eolica(
        self,
        codigo_usina: Optional[int] = None,
        nome_usina: Optional[str] = None,
        constrained_off: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[EOLICA, List[EOLICA], pd.DataFrame]]:
        """
        Obtém um registro que define as usinas não simuladas existentes
        no caso.

        :param codigo_usina: o código identificador da usina
        :type codigo_usina: int | None
        :param nome_usina: o nome da usina
        :type nome_usina: str | None
        :param constrained_off: a consideração de constrained-off na usina
        :type constrained_off: int | None
        :param df: retorna os registros em um `pd.DataFrame`
            (somente leitura)
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EOLICA` | list[:class:`EOLICA`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            EOLICA,
            codigo_usina=codigo_usina,
            nome_usina=nome_usina,
            constrained_off=constrained_off,
            df=df,
        )

    def eolicabarra(
        self,
        codigo_usina: Optional[int] = None,
        codigo_barra: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[EOLICABARRA, List[EOLICABARRA], pd.DataFrame]]:
        """
        Obtém um registro que define as relações entre usinas não simuladas
        e barras do sistema.

        :param codigo_usina: o código identificador da usina
        :type codigo_usina: int | None
        :param codigo_barra: o código identificador da barra
        :type codigo_barra: int | None
        :param df: retorna os registros em um `pd.DataFrame`
            (somente leitura)
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EOLICABARRA` | list[:class:`EOLICABARRA`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            EOLICABARRA,
            codigo_usina=codigo_usina,
            codigo_barra=codigo_barra,
            df=df,
        )

    def eolicasubm(
        self,
        codigo_usina: Optional[int] = None,
        submercado: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[EOLICASUBM, List[EOLICASUBM], pd.DataFrame]]:
        """
        Obtém um registro que define as relações entre usinas não simuladas
        e os submercados.

        :param codigo_usina: o código identificador da usina
        :type codigo_usina: int | None
        :param submercado: o nome do submercado a qual a usina pertence
        :type submercado: str | None
        :param df: retorna os registros em um `pd.DataFrame`
            (somente leitura)
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EOLICASUBM` | list[:class:`EOLICASUBM`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            EOLICASUBM, codigo_usina=codigo_usina, submercado=submercado, df=df
        )

    def eolica_geracao(
        self,
        codigo_usina: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[EOLICAGERACAO, List[EOLICAGERACAO], pd.DataFrame]]:
        """
        Obtém um registro que define a geração prevista das usinas não
        simuladas para o estudo.

        :param codigo_usina: o código identificador da usina
        :type codigo_usina: int | None
        :param df: retorna os registros em um `pd.DataFrame`
            (somente leitura)
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EOLICAGERACAO` | list[:class:`EOLICAGERACAO`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            EOLICAGERACAO, codigo_usina=codigo_usina, df=df
        )
