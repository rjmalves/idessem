from typing import List, Optional, Type, TypeVar, Union

import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile

from idessem.dessem.modelos.operuh import ELEM, LIM, REST, VAR
from cfinterface.components.register import Register


class Operuh(RegisterFile):
    """
    Armazena os dados com as restrições operativas para as
    usinas hidrelétricas do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `operuh.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [
        REST,
        ELEM,
        LIM,
        VAR,
    ]

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

    def rest(
        self,
        codigo_restricao: Optional[int] = None,
        tipo_restricao: Optional[str] = None,
        intervalo_aplicacao: Optional[str] = None,
        valor_inicial: Optional[float] = None,
        tipo_restricao_variacao: Optional[int] = None,
        duracao_janela: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[REST, List[REST], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição hidráulica existente
        no estudo descrito pelo :class:`Operuh`.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param tipo_restricao: tipo da restrição (L,V)
        :type tipo_restricao: str | None
        :param intervalo_aplicacao: intervalo de aplicação
        :type intervalo_aplicacao: str | None
        :param valor_inicial: valor inicial da variável
        :type valor_inicial: float | None
        :param tipo_restricao_variacao: tipo da restrição de variação
        :type tipo_restricao_variacao: int | None
        :param duracao_janela: duração da janela da restrição de variação
        :type duracao_janela: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`REST` | list[:class:`REST`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            REST,
            codigo_restricao=codigo_restricao,
            tipo_restricao=tipo_restricao,
            intervalo_aplicacao=intervalo_aplicacao,
            valor_inicial=valor_inicial,
            tipo_restricao_variacao=tipo_restricao_variacao,
            duracao_janela=duracao_janela,
            df=df,
        )

    def elem(
        self,
        codigo_restricao: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[ELEM, List[ELEM], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes de participação
        das usinas hidráulicas de uma restrição hidráulica existente
        no estudo descrito pelo :class:`Operuh`.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param codigo_usina: código da usina hidráulica
        :type codigo_usina: int | None
        :param coeficiente: coeficiente de participação da usina na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`ELEM` | list[:class:`ELEM`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            ELEM,
            codigo_restricao=codigo_restricao,
            codigo_usina=codigo_usina,
            coeficiente=coeficiente,
            df=df,
        )

    def lim(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LIM, List[LIM], pd.DataFrame]]:
        """
        Obtém um registro que especifica o limite inferior e
        superior de uma restrição hidráulica existente
        no estudo descrito pelo :class:`Operuh`.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | str | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | str | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LIM` | list[:class:`LIM`] | :class:`pd.DataFrame` | None

        """

        return self.__registros_ou_df(
            LIM,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            df=df,
        )

    def var(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[VAR, List[VAR], pd.DataFrame]]:
        """
        Obtém um registro que especifica rampas de variação de
        acréscimo e descréscimo de uma restrição hidráulica existente
        no estudo descrito pelo :class:`Operuh`.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | str | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | str | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VAR` | list[:class:`VAR`] | :class:`pd.DataFrame` | None

        """

        return self.__registros_ou_df(
            VAR,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            df=df,
        )
