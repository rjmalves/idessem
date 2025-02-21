from idessem.dessem.modelos.termdat import CADUSIT, CADUNIDT, CADCONF, CADMIN
import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile
from typing import Type, List, Optional, TypeVar, Union
from cfinterface.components.register import Register


class Term(RegisterFile):
    """
    Armazena os dados com as características de cadastro das usinas
    termelétricas do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `termdat.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [CADUSIT, CADUNIDT, CADCONF, CADMIN]

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

    def cadusit(
        self,
        codigo_usina: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CADUSIT, List[CADUSIT], pd.DataFrame]]:
        """
        Obtém um registro que define as características de usinas termoelétricas
        no estudo descrito pelo :class:`Term`.

        :param codigo_usina: código da usina
        :type codigo_usina: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CADUSIT` | list[:class:`CADUSIT`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(CADUSIT, codigo_usina=codigo_usina, df=df)

    def cadunidt(
        self,
        codigo_usina: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CADUNIDT, List[CADUNIDT], pd.DataFrame]]:
        """
        Obtém um registro que define as características das unidades
        geradoras de usinas termoelétricas no estudo descrito
        pelo :class:`Term`.

        :param codigo_usina: código da usina
        :type codigo_usina: int | None
        :param codigo_unidade: código da unidade
        :type codigo_unidade: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CADUNIDT` | list[:class:`CADUNIDT`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            CADUNIDT,
            codigo_usina=codigo_usina,
            codigo_unidade=codigo_unidade,
            df=df,
        )

    def cadconf(
        self,
        codigo_usina: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        codigo_unidade_equivalente: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CADCONF, List[CADCONF], pd.DataFrame]]:
        """
        Obtém um registro que define as unidades equivalentes
        de usinas termoelétricas no estudo descrito pelo :class:`Term`.

        :param codigo_usina: código da usina
        :type codigo_usina: int | None
        :param codigo_unidade_equivalente: código da unidade equivalente
        :type codigo_unidade_equivalente: int | None
        :param codigo_unidade: código da unidade
        :type codigo_unidade: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CADCONF` | list[:class:`CADCONF`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            CADCONF,
            codigo_usina=codigo_usina,
            codigo_unidade_equivalente=codigo_unidade_equivalente,
            codigo_unidade=codigo_unidade,
            df=df,
        )

    def cadmin(
        self,
        codigo_usina: Optional[int] = None,
        codigo_unidade_equivalente: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CADMIN, List[CADMIN], pd.DataFrame]]:
        """
        Obtém um registro que define as quantidades de unidades reais disponíveis
        para acionamento das unidades equivalentes de usinas termoelétricas
        no estudo descrito pelo :class:`Term`.

        :param codigo_usina: código da usina
        :type codigo_usina: int | None
        :param codigo_unidade_equivalente: código da unidade equivalente
        :type codigo_unidade_equivalente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CADMIN` | list[:class:`CADMIN`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            CADMIN,
            codigo_usina=codigo_usina,
            codigo_unidade_equivalente=codigo_unidade_equivalente,
            df=df,
        )
