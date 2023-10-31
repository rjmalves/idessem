from typing import Type, TypeVar, Optional, List, Union
from cfinterface.components.register import Register
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

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Uch(RegisterFile):
    """ """

    T = TypeVar("T")

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

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="uch.csv") -> "Uch":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="uch.csv"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def __registros_por_tipo(self, registro: Type[T]) -> List[T]:
        """
        Obtém os registro de um tipo, se houver algum no arquivo.

        :param registro: Um tipo de registro para ser lido
        :type registro: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int

        """
        return [b for b in self.data.of_type(registro)]

    def __obtem_registro(self, tipo: Type[T]) -> Optional[T]:
        """ """
        r = self.__obtem_registros(tipo)
        return r[0] if len(r) > 0 else None

    def __obtem_registros(self, tipo: Type[T]) -> List[T]:
        return self.__registros_por_tipo(tipo)

    def __obtem_registros_com_filtros(
        self, tipo_registro: Type[T], **kwargs
    ) -> Optional[Union[T, List[T]]]:
        def __atende(r) -> bool:
            condicoes: List[bool] = []
            for k, v in kwargs.items():
                if v is not None:
                    condicoes.append(getattr(r, k) == v)
            return all(condicoes)

        regs_filtro = [
            r for r in self.__obtem_registros(tipo_registro) if __atende(r)
        ]
        if len(regs_filtro) == 0:
            return None
        elif len(regs_filtro) == 1:
            return regs_filtro[0]
        else:
            return regs_filtro

    def cria_registro(self, anterior: Register, registro: Register):
        """
        Adiciona um registro ao arquivo após um outro registro previamente
        existente.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.add_after(anterior, registro)

    def deleta_registro(self, registro: Register):
        """
        Remove um registro existente no arquivo.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.remove(registro)

    def append_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na última posição.
        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.append(registro)

    def preppend_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na primeira posição.
        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.preppend(registro)

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

        return self.__obtem_registro(UchOpcaoPadrao)

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
        if df:
            return self._as_df(UchOpcaoUsina)
        else:
            return self.__obtem_registros_com_filtros(
                UchOpcaoUsina,
                codigo_usina=codigo_usina,
                considera_uch_usina=considera_uch_usina,
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

        return self.__obtem_registro(UchOpcaoPadraoData)

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
        if df:
            return self._as_df(UchOpcaoUnidadeVazioPadrao)
        else:
            return self.__obtem_registros_com_filtros(
                UchOpcaoUnidadeVazioPadrao,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                considera_operacao_vazio=considera_operacao_vazio,
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
        if df:
            return self._as_df(UchOpcaoConjuntoVazioPadrao)
        else:
            return self.__obtem_registros_com_filtros(
                UchOpcaoConjuntoVazioPadrao,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                considera_operacao_vazio=considera_operacao_vazio,
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
        if df:
            return self._as_df(UchOpcaoUsinaVazioPadrao)
        else:
            return self.__obtem_registros_com_filtros(
                UchOpcaoUsinaVazioPadrao,
                codigo_usina=codigo_usina,
                considera_operacao_vazio=considera_operacao_vazio,
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
        if df:
            return self._as_df(UchTonToffUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchTonToffUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                tempo_minimo_ligada=tempo_minimo_ligada,
                tempo_maximo_ligada=tempo_maximo_ligada,
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
        if df:
            return self._as_df(UchTonToffConjunto)
        else:
            return self.__obtem_registros_com_filtros(
                UchTonToffConjunto,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                tempo_minimo_ligada=tempo_minimo_ligada,
                tempo_maximo_ligada=tempo_maximo_ligada,
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
        if df:
            return self._as_df(UchTonToffUsina)
        else:
            return self.__obtem_registros_com_filtros(
                UchTonToffUsina,
                codigo_usina=codigo_usina,
                tempo_minimo_ligada=tempo_minimo_ligada,
                tempo_maximo_ligada=tempo_maximo_ligada,
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
        if df:
            return self._as_df(UchGminGmaxUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchGminGmaxUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                geracao_minima_unidade=geracao_minima_unidade,
                geracao_maxima_unidade=geracao_maxima_unidade,
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
        if df:
            return self._as_df(UchQturminQturmaxUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchQturminQturmaxUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                turbinamento_minimo_unidade=turbinamento_minimo_unidade,
                turbinamento_maximo_unidade=turbinamento_maximo_unidade,
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
        if df:
            return self._as_df(UchCondicaoInicialUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchCondicaoInicialUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                status_inicial=status_inicial,
                tempo_permanencia_unidade=tempo_permanencia_unidade,
                geracao_inicial_unidade=geracao_inicial_unidade,
                turbinamento_inicial_unidade=turbinamento_inicial_unidade,
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
        if df:
            return self._as_df(UchConsumoAguaVazioUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchConsumoAguaVazioUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                consumo_agua=consumo_agua,
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
        if df:
            return self._as_df(UchConsumoAguaVazioConjunto)
        else:
            return self.__obtem_registros_com_filtros(
                UchConsumoAguaVazioConjunto,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                consumo_agua=consumo_agua,
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
        if df:
            return self._as_df(UchConsumoAguaVazioUsina)
        else:
            return self.__obtem_registros_com_filtros(
                UchConsumoAguaVazioUsina,
                codigo_usina=codigo_usina,
                consumo_agua=consumo_agua,
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
        if df:
            return self._as_df(UchLimiteMudancaStatusVazioUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchLimiteMudancaStatusVazioUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                limite_maximo_mudancas=limite_maximo_mudancas,
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
        if df:
            return self._as_df(UchLimiteMudancaStatusVazioConjunto)
        else:
            return self.__obtem_registros_com_filtros(
                UchLimiteMudancaStatusVazioConjunto,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                limite_maximo_mudancas=limite_maximo_mudancas,
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
        if df:
            return self._as_df(UchLimiteMudancaStatusVazioUsina)
        else:
            return self.__obtem_registros_com_filtros(
                UchLimiteMudancaStatusVazioUsina,
                codigo_usina=codigo_usina,
                limite_maximo_mudancas=limite_maximo_mudancas,
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
        if df:
            return self._as_df(UchCustoPartidaVazioUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchCustoPartidaVazioUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                custo_partida=custo_partida,
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
        if df:
            return self._as_df(UchCustoPartidaVazioConjunto)
        else:
            return self.__obtem_registros_com_filtros(
                UchCustoPartidaVazioConjunto,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                custo_partida=custo_partida,
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
        if df:
            return self._as_df(UchCustoPartidaVazioUsina)
        else:
            return self.__obtem_registros_com_filtros(
                UchCustoPartidaVazioUsina,
                codigo_usina=codigo_usina,
                custo_partida=custo_partida,
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
        if df:
            return self._as_df(UchCustoPartidaUnidade)
        else:
            return self.__obtem_registros_com_filtros(
                UchCustoPartidaUnidade,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                custo_partida=custo_partida,
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
        if df:
            return self._as_df(UchCustoPartidaConjunto)
        else:
            return self.__obtem_registros_com_filtros(
                UchCustoPartidaConjunto,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                custo_partida=custo_partida,
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
        if df:
            return self._as_df(UchCustoPartidaUsina)
        else:
            return self.__obtem_registros_com_filtros(
                UchCustoPartidaUsina,
                codigo_usina=codigo_usina,
                custo_partida=custo_partida,
            )
