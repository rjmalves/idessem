from typing import Type, TypeVar, Optional, List, Union
from cfinterface.files.registerfile import RegisterFile
import pandas as pd  # type: ignore
from idessem.dessem.modelos.uch import (
    UchOpcaoPadrao,
    UchOpcaoUsina,
    UchOpcaoPadraoData,
    UchOpcaoUnidadeVazioPadrao,
    UchOpcaoConjuntoVazioPadrao,
    UchOpcaoUsinaVazioPadrao,
    UchTonToffUnidade,
    UchTonToffConjunto,
    UchTonToffUsina,
    UchGminGmaxUnidade,
    UchQturminQturmaxUnidade,
    UchCondicaoInicialUnidade,
    UchConsumoAguaVazioUnidade,
    UchConsumoAguaVazioConjunto,
    UchConsumoAguaVazioUsina,
    UchLimiteMudancaStatusVazioUnidade,
    UchLimiteMudancaStatusVazioConjunto,
    UchLimiteMudancaStatusVazioUsina,
    UchCustoPartidaVazioUnidade,
    UchCustoPartidaVazioConjunto,
    UchCustoPartidaVazioUsina,
    UchCustoPartidaUnidade,
    UchCustoPartidaConjunto,
    UchCustoPartidaUsina,
)
from cfinterface.components.register import Register


class Uch(RegisterFile):
    """Armazena os dados de entrada do DESSEM referentes aos dados
    de unit commitment hidráulico (UCH) do problema."""

    T = TypeVar("T", bound=Register)

    REGISTERS = [
        UchCustoPartidaVazioUnidade,
        UchCustoPartidaVazioConjunto,
        UchCustoPartidaVazioUsina,
        UchCustoPartidaUnidade,
        UchCustoPartidaConjunto,
        UchCustoPartidaUsina,
        UchLimiteMudancaStatusVazioUnidade,
        UchLimiteMudancaStatusVazioConjunto,
        UchLimiteMudancaStatusVazioUsina,
        UchConsumoAguaVazioUnidade,
        UchConsumoAguaVazioConjunto,
        UchConsumoAguaVazioUsina,
        UchCondicaoInicialUnidade,
        UchQturminQturmaxUnidade,
        UchGminGmaxUnidade,
        UchTonToffUsina,
        UchTonToffConjunto,
        UchTonToffUnidade,
        UchOpcaoPadraoData,
        UchOpcaoPadrao,
        UchOpcaoUsinaVazioPadrao,
        UchOpcaoConjuntoVazioPadrao,
        UchOpcaoUnidadeVazioPadrao,
        UchOpcaoUsina,
    ]

    def __registros_ou_df(
        self, t: Type[T], **kwargs
    ) -> Optional[Union[T, List[T], pd.DataFrame]]:
        if kwargs.get("df"):
            return self._as_df(t)
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    @property
    def opcao_padrao(
        self,
    ) -> Optional[UchOpcaoPadrao]:
        """
        Obtém o (único) registro de identificação de consideração
        de UCH na execução.

        :return: Um registro, se existir.
        :rtype: `UchOpcaoPadrao` | `None`
        """

        r = self.data.get_registers_of_type(UchOpcaoPadrao)
        if isinstance(r, UchOpcaoPadrao):
            return r
        else:
            return None

    def opcao_usina(
        self,
        codigo_usina: Optional[int] = None,
        considera_uch_usina: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[UchOpcaoUsina, List[UchOpcaoUsina], pd.DataFrame]]:
        """
        Obtém registros que identificam a consideração de UCH
        para cada usina. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param considera_uch_usina: flag se considera UCH para a usina
        :type considera_uch_usina: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchOpcaoUsina` |
            List[`UchOpcaoUsina`] | `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            UchOpcaoUsina,
            codigo_usina=codigo_usina,
            considera_uch_usina=considera_uch_usina,
            df=df,
        )

    @property
    def opcao_padrao_data(
        self,
    ) -> Optional[UchOpcaoPadraoData]:
        """
        Obtém o (único) registro que determina o período de consideração
        das restrições de UCH.

        :return: Um registro, se existir.
        :rtype: `UchOpcaoPadrao` | `None`
        """

        r = self.data.get_registers_of_type(UchOpcaoPadraoData)
        if isinstance(r, UchOpcaoPadraoData):
            return r
        else:
            return None

    def opcao_unidade_vazio_padrao(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        considera_operacao_vazio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchOpcaoUnidadeVazioPadrao,
            List[UchOpcaoUnidadeVazioPadrao],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam se a unidade geradora de um determinado
        conjunto de uma usina hidrelétrica poderá operar em vazio. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param considera_operacao_vazio: flag se considera operação a vazio
        :type considera_operacao_vazio: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchOpcaoUnidadeVazioPadrao` |
            List[`UchOpcaoUnidadeVazioPadrao`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchOpcaoUnidadeVazioPadrao,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            considera_operacao_vazio=considera_operacao_vazio,
            df=df,
        )

    def opcao_conjunto_vazio_padrao(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        considera_operacao_vazio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchOpcaoConjuntoVazioPadrao,
            List[UchOpcaoConjuntoVazioPadrao],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam se um conjunto de uma usina
        hidrelétrica poderá operar em vazio. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`,
        apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param considera_operacao_vazio: flag se considera operação a vazio
        :type considera_operacao_vazio: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchOpcaoConjuntoVazioPadrao` |
            List[`UchOpcaoConjuntoVazioPadrao`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchOpcaoConjuntoVazioPadrao,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            considera_operacao_vazio=considera_operacao_vazio,
            df=df,
        )

    def opcao_usina_vazio_padrao(
        self,
        codigo_usina: Optional[int] = None,
        considera_operacao_vazio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchOpcaoUsinaVazioPadrao,
            List[UchOpcaoUsinaVazioPadrao],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam se uma usina hidrelétrica
        poderá operar em vazio. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param considera_operacao_vazio: flag se considera operação a vazio
        :type considera_operacao_vazio: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchOpcaoUsinaVazioPadrao` |
            List[`UchOpcaoUsinaVazioPadrao`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchOpcaoUsinaVazioPadrao,
            codigo_usina=codigo_usina,
            considera_operacao_vazio=considera_operacao_vazio,
            df=df,
        )

    def ton_toff_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        tempo_minimo_ligada: Optional[int] = None,
        tempo_maximo_ligada: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchTonToffUnidade,
            List[UchTonToffUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o tempo mínimo ligada e desligada
        (Ton e Toff) da unidade geradora de um determinado conjunto de uma
        usina hidrelétrica. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param tempo_minimo_ligada: tempo mínimo ligada em horas
        :type tempo_minimo_ligada: int | None
        :param tempo_maximo_ligada: tempo máximo ligada em horas
        :type tempo_maximo_ligada: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchTonToffUnidade` |
            List[`UchTonToffUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchTonToffUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            tempo_minimo_ligada=tempo_minimo_ligada,
            tempo_maximo_ligada=tempo_maximo_ligada,
            df=df,
        )

    def ton_toff_conjunto(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        tempo_minimo_ligada: Optional[int] = None,
        tempo_maximo_ligada: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchTonToffConjunto,
            List[UchTonToffConjunto],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o tempo mínimo ligada e desligada
        (Ton e Toff) do conjunto de uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas para
        leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param tempo_minimo_ligada: tempo mínimo ligada em horas
        :type tempo_minimo_ligada: int | None
        :param tempo_maximo_ligada: tempo máximo ligada em horas
        :type tempo_maximo_ligada: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchTonToffConjunto` |
            List[`UchTonToffConjunto`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchTonToffConjunto,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            tempo_minimo_ligada=tempo_minimo_ligada,
            tempo_maximo_ligada=tempo_maximo_ligada,
            df=df,
        )

    def ton_toff_usina(
        self,
        codigo_usina: Optional[int] = None,
        tempo_minimo_ligada: Optional[int] = None,
        tempo_maximo_ligada: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchTonToffUsina,
            List[UchTonToffUsina],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o tempo mínimo ligada e desligada
        (Ton e Toff) de uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas para
        leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param tempo_minimo_ligada: tempo mínimo ligada em horas
        :type tempo_minimo_ligada: int | None
        :param tempo_maximo_ligada: tempo máximo ligada em horas
        :type tempo_maximo_ligada: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchTonToffUsina` |
            List[`UchTonToffUsina`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchTonToffUsina,
            codigo_usina=codigo_usina,
            tempo_minimo_ligada=tempo_minimo_ligada,
            tempo_maximo_ligada=tempo_maximo_ligada,
            df=df,
        )

    def gmin_gmax_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        geracao_minima_unidade: Optional[float] = None,
        geracao_maxima_unidade: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchGminGmaxUnidade,
            List[UchGminGmaxUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam a geração mínima e máxima
        da unidade geradora de um determinado conjunto de uma
        usina hidrelétrica. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param geracao_minima_unidade: geração mínima
        :type geracao_minima_unidade: float | None
        :param geracao_maxima_unidade: geração máxima
        :type geracao_maxima_unidade: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchGminGmaxUnidade` |
            List[`UchGminGmaxUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchGminGmaxUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            geracao_minima_unidade=geracao_minima_unidade,
            geracao_maxima_unidade=geracao_maxima_unidade,
            df=df,
        )

    def qturmin_qturmax_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        turbinamento_minimo_unidade: Optional[float] = None,
        turbinamento_maximo_unidade: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchQturminQturmaxUnidade,
            List[UchQturminQturmaxUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o turbinamento mínimo e máximo
        da unidade geradora de um determinado conjunto de uma
        usina hidrelétrica. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param turbinamento_minimo_unidade: turbinamento mínimo
        :type turbinamento_minimo_unidade: float | None
        :param turbinamento_maximo_unidade: turbinamento máximo
        :type turbinamento_maximo_unidade: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchQturminQturmaxUnidade` |
            List[`UchQturminQturmaxUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchQturminQturmaxUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            turbinamento_minimo_unidade=turbinamento_minimo_unidade,
            turbinamento_maximo_unidade=turbinamento_maximo_unidade,
            df=df,
        )

    def condicao_inicial_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        status_inicial: Optional[int] = None,
        tempo_permanencia_unidade: Optional[int] = None,
        geracao_inicial_unidade: Optional[float] = None,
        turbinamento_inicial_unidade: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchCondicaoInicialUnidade,
            List[UchCondicaoInicialUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam a condição inicial
        da unidade geradora de um determinado conjunto de uma
        usina hidrelétrica. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param status_inicial: o status inicial
        :type status_inicial: int | None
        :param tempo_permanencia_unidade: tempo de permanência da unidade
        :type tempo_permanencia_unidade: int | None
        :param geracao_inicial_unidade: geração inicial da unidade
        :type geracao_inicial_unidade: float | None
        :param turbinamento_inicial_unidade: turbinamento inicial da undiade
        :type turbinamento_inicial_unidade: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchCondicaoInicialUnidade` |
            List[`UchCondicaoInicialUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchCondicaoInicialUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            status_inicial=status_inicial,
            tempo_permanencia_unidade=tempo_permanencia_unidade,
            geracao_inicial_unidade=geracao_inicial_unidade,
            turbinamento_inicial_unidade=turbinamento_inicial_unidade,
            df=df,
        )

    def consumo_agua_vazio_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        consumo_agua: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchConsumoAguaVazioUnidade,
            List[UchConsumoAguaVazioUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o consumo de água incorrido de
        forma contínua enquanto a unidade geradora de um determinado
        conjunto de uma usina hidrelétrica está operando em vazio. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param consumo_agua: consumo de água
        :type consumo_agua: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchConsumoAguaVazioUnidade` |
            List[`UchConsumoAguaVazioUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchConsumoAguaVazioUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            consumo_agua=consumo_agua,
            df=df,
        )

    def consumo_agua_vazio_conjunto(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        consumo_agua: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchConsumoAguaVazioConjunto,
            List[UchConsumoAguaVazioConjunto],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o consumo de água incorrido de
        forma contínua enquanto as unidades do conjunto de uma usina hidrelétrica
        estão operando em vazio. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param consumo_agua: consumo de água
        :type consumo_agua: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchConsumoAguaVazioConjunto` |
            List[`UchConsumoAguaVazioConjunto`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchConsumoAguaVazioConjunto,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            consumo_agua=consumo_agua,
            df=df,
        )

    def consumo_agua_vazio_usina(
        self,
        codigo_usina: Optional[int] = None,
        consumo_agua: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchConsumoAguaVazioUsina,
            List[UchConsumoAguaVazioUsina],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o consumo de água incorrido de
        forma contínua enquanto a usina hidrelétrica
        estão operando em vazio. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param consumo_agua: consumo de água
        :type consumo_agua: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchConsumoAguaVazioUsina` |
            List[`UchConsumoAguaVazioUsina`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchConsumoAguaVazioUsina,
            codigo_usina=codigo_usina,
            consumo_agua=consumo_agua,
            df=df,
        )

    def limite_mudanca_status_vazio_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        limite_maximo_mudancas: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchLimiteMudancaStatusVazioUnidade,
            List[UchLimiteMudancaStatusVazioUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o limite máximo de mudança de status
        para operar em vazio para a unidade geradora de um determinado
        conjunto de uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param limite_maximo_mudancas: limite máximo de mudança de status para operar vazio
        :type limite_maximo_mudancas: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchLimiteMudancaStatusVazioUnidade` |
            List[`UchLimiteMudancaStatusVazioUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchLimiteMudancaStatusVazioUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            limite_maximo_mudancas=limite_maximo_mudancas,
            df=df,
        )

    def limite_mudanca_status_vazio_conjunto(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        limite_maximo_mudancas: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchLimiteMudancaStatusVazioConjunto,
            List[UchLimiteMudancaStatusVazioConjunto],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o limite máximo de mudança de status
        para operar em vazio por conjunto de uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param limite_maximo_mudancas: limite máximo de mudança de status para operar vazio
        :type limite_maximo_mudancas: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchLimiteMudancaStatusVazioConjunto` |
            List[`UchLimiteMudancaStatusVazioConjunto`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchLimiteMudancaStatusVazioConjunto,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            limite_maximo_mudancas=limite_maximo_mudancas,
            df=df,
        )

    def limite_mudanca_status_vazio_usina(
        self,
        codigo_usina: Optional[int] = None,
        limite_maximo_mudancas: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchLimiteMudancaStatusVazioUsina,
            List[UchLimiteMudancaStatusVazioUsina],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o limite máximo de mudança de status
        para operar em vazio para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param limite_maximo_mudancas: limite máximo de mudança de status para operar vazio
        :type limite_maximo_mudancas: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchLimiteMudancaStatusVazioUsina` |
            List[`UchLimiteMudancaStatusVazioUsina`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchLimiteMudancaStatusVazioUsina,
            codigo_usina=codigo_usina,
            limite_maximo_mudancas=limite_maximo_mudancas,
            df=df,
        )

    def custo_partida_vazio_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        custo_partida: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchCustoPartidaVazioUnidade,
            List[UchCustoPartidaVazioUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o custo de partida
        para operar em vazio (transição de desligado para vazio)
        para uma unidade geradora de um determinado conjunto de uma usina
        hidrelétrica. Opcionalmente, o retorno pode ser transformado em
        um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param custo_partida: custo de partida
        :type custo_partida: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchCustoPartidaVazioUnidade` |
            List[`UchCustoPartidaVazioUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchCustoPartidaVazioUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            custo_partida=custo_partida,
            df=df,
        )

    def custo_partida_vazio_conjunto(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        custo_partida: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchCustoPartidaVazioConjunto,
            List[UchCustoPartidaVazioConjunto],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o custo de partida
        para operar em vazio (transição de desligado para vazio)
        para as unidades geradoras de um determinado conjunto de uma usina
        hidrelétrica. Opcionalmente, o retorno pode ser transformado em
        um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param custo_partida: custo de partida
        :type custo_partida: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchCustoPartidaVazioConjunto` |
            List[`UchCustoPartidaVazioConjunto`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchCustoPartidaVazioConjunto,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            custo_partida=custo_partida,
            df=df,
        )

    def custo_partida_vazio_usina(
        self,
        codigo_usina: Optional[int] = None,
        custo_partida: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchCustoPartidaVazioUsina,
            List[UchCustoPartidaVazioUsina],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o custo de partida
        para operar em vazio (transição de desligado para vazio)
        para as unidades geradoras de uma usina
        hidrelétrica. Opcionalmente, o retorno pode ser transformado em
        um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param custo_partida: custo de partida
        :type custo_partida: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchCustoPartidaVazioUsina` |
            List[`UchCustoPartidaVazioUsina`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchCustoPartidaVazioUsina,
            codigo_usina=codigo_usina,
            custo_partida=custo_partida,
            df=df,
        )

    def custo_partida_unidade(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        custo_partida: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchCustoPartidaUnidade,
            List[UchCustoPartidaUnidade],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o custo de partida
        para acionamento de uma unidade geradora de um determinado conjunto de uma usina
        hidrelétrica. Opcionalmente, o retorno pode ser transformado em
        um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param codigo_unidade: código da unidade geradora do conjunto
        :type codigo_unidade: int | None
        :param custo_partida: custo de partida
        :type custo_partida: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchCustoPartidaUnidade` |
            List[`UchCustoPartidaUnidade`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchCustoPartidaUnidade,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            custo_partida=custo_partida,
            df=df,
        )

    def custo_partida_conjunto(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        custo_partida: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchCustoPartidaConjunto,
            List[UchCustoPartidaConjunto],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o custo de partida
        para acionamento das unidades geradoras de um determinado conjunto de uma usina
        hidrelétrica. Opcionalmente, o retorno pode ser transformado em
        um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param codigo_conjunto: código do conjunto da usina
        :type codigo_conjunto: int | None
        :param custo_partida: custo de partida
        :type custo_partida: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchCustoPartidaConjunto` |
            List[`UchCustoPartidaConjunto`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchCustoPartidaConjunto,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            custo_partida=custo_partida,
            df=df,
        )

    def custo_partida_usina(
        self,
        codigo_usina: Optional[int] = None,
        custo_partida: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            UchCustoPartidaUsina,
            List[UchCustoPartidaUsina],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que determinam o custo de partida
        para acionamento das unidades geradoras de uma usina
        hidrelétrica. Opcionalmente, o retorno pode ser transformado em
        um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param custo_partida: custo de partida
        :type custo_partida: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: `UchCustoPartidaUsina` |
            List[`UchCustoPartidaUsina`] | `None` | `DataFrame`
        """

        return self.__registros_ou_df(
            UchCustoPartidaUsina,
            codigo_usina=codigo_usina,
            custo_partida=custo_partida,
            df=df,
        )
