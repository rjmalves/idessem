from idessem.dessem.modelos.entdados import (
    UH,
    SIST,
    REE,
    TM,
    RIVAR,
    RD,
    TVIAG,
    UT,
    USIE,
    DP,
    DE,
    CD,
    PQ,
    IT,
    RI,
    IA,
    GP,
    NI,
    VE,
    FP,
    TX,
    EZ,
    R11,
    CR,
    SECR,
    DA,
    RE,
    LU,
    FH,
    FT,
    FI,
    FE,
    FR,
    FC,
    CI,
    CE,
    MH,
    PE,
    ACVTFUGA,
    ACVOLMAX,
    ACVOLMIN,
    ACVSVERT,
    ACVMDESV,
    ACCOTVAZ,
    ACCOTVOL,
    ACCOTTAR,
    ACNUMCON,
    ACNUMJUS,
    ACNUMPOS,
    ACJUSENA,
    ACJUSMED,
    ACCOFEVA,
    ACNUMMAQ,
    ACDESVIO,
    ACPOTEFE,
)
import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile
from typing import Type, List, Optional, TypeVar, Union, Any
import numpy as np
from cfinterface.components.register import Register


class Entdados(RegisterFile):
    """
    Armazena os dados de entrada gerais do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `entdados.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    """

    T = TypeVar("T", bound=Register)

    AC = Union[
        ACVTFUGA,
        ACVOLMAX,
        ACVOLMIN,
        ACVSVERT,
        ACVMDESV,
        ACCOTVAZ,
        ACCOTVOL,
        ACCOTTAR,
        ACNUMCON,
        ACNUMJUS,
        ACNUMPOS,
        ACJUSENA,
        ACJUSMED,
        ACCOFEVA,
        ACNUMMAQ,
        ACDESVIO,
        ACPOTEFE,
    ]

    REGISTERS = [
        UH,
        SIST,
        REE,
        TM,
        RIVAR,
        RD,
        TVIAG,
        UT,
        USIE,
        DP,
        DE,
        CD,
        PQ,
        IT,
        RI,
        IA,
        GP,
        NI,
        VE,
        FP,
        TX,
        EZ,
        R11,
        CR,
        SECR,
        DA,
        RE,
        LU,
        FH,
        FT,
        FI,
        FE,
        FR,
        FC,
        CI,
        CE,
        MH,
        PE,
        ACVTFUGA,
        ACVOLMAX,
        ACVOLMIN,
        ACVSVERT,
        ACVMDESV,
        ACCOTVAZ,
        ACCOTVOL,
        ACCOTTAR,
        ACNUMCON,
        ACNUMJUS,
        ACNUMPOS,
        ACJUSENA,
        ACJUSMED,
        ACCOFEVA,
        ACNUMMAQ,
        ACPOTEFE,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    def __expande_colunas_df(self, df: pd.DataFrame) -> pd.DataFrame:
        colunas_com_listas = df.map(lambda linha: isinstance(linha, list)).all()
        nomes_colunas = [
            c for c in colunas_com_listas[colunas_com_listas].index
        ]
        for c in nomes_colunas:
            num_elementos = len(df.at[0, c])
            particoes_coluna = [f"{c}_{i}" for i in range(1, num_elementos + 1)]
            df[particoes_coluna] = df.apply(
                lambda linha: linha[c]
                + [np.nan] * max(0, num_elementos - len(linha[c])),
                axis=1,
                result_type="expand",
            )
            df.drop(columns=[c], inplace=True)
        return df

    def __registros_ou_df(
        self, t: Type[T], **kwargs
    ) -> Optional[Union[T, List[T], pd.DataFrame]]:
        if kwargs.get("df"):
            return self.__expande_colunas_df(self._as_df(t))
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    @property
    def rd(self) -> Optional[RD]:
        """
        Obtém o (único) registro que define as opções de representação da
        rede elétrica no estudo descrito pelo :class:`Entdados`.

        :return: Um registro, se existir.
        :rtype: :class:`RD` | None
        """
        r = self.data.get_registers_of_type(RD)
        if isinstance(r, RD):
            return r
        else:
            return None

    def rivar(
        self,
        codigo_entidade: Optional[int] = None,
        tipo_variavel: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[RIVAR, List[RIVAR], pd.DataFrame]]:
        """
        Obtém um registro que define a consideração de restrições internas
        do tipo "soft" de variação para variáveis do problema
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_entidade: código da entidade
        :type codigo_entidade: int | None
        :param sistema_para: sistema "para" quando aplicável
        :type sistema_para: int | None
        :param tipo_variavel: tipo de variável
        :type tipo_variavel: int | None
        :param penalidade: penalidade
        :type penalidade: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RIVAR` | list[:class:`RIVAR`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            RIVAR,
            codigo_entidade=codigo_entidade,
            tipo_variavel=tipo_variavel,
            df=df,
        )

    def tm(
        self,
        dia_inicial: Optional[int] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[TM, List[TM], pd.DataFrame]]:
        """
        Obtém um registro que define a discretização temporal e representação
        da rede elétrica no estudo descrito pelo :class:`Entdados`.

        :param dia_inicial: dia inicial do período
        :type dia_inicial: int | None
        :param hora_inicial: hora inicial do período
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial do período
        :type meia_hora_inicial: int | None
        :param duracao: duração do período
        :type duracao: float | None
        :param duracao: flag para consideração da rede elétrica
        :type duracao: int | None
        :param nome_patamar: nome do patamar de carga
        :type nome_patamar: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TM` | list[:class:`TM`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            TM,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            df=df,
        )

    def sist(
        self,
        codigo_submercado: Optional[int] = None,
        nome_submercado: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[SIST, List[SIST], pd.DataFrame]]:
        """
        Obtém um registro que define os submercados existentes
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_submercado: código que especifica o registro do submercado
        :type codigo_submercado: int | None
        :param nome_submercado: nome do submercado
        :type nome_submercado: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`SIST` | list[:class:`SIST`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            SIST,
            codigo_submercado=codigo_submercado,
            nome_submercado=nome_submercado,
            df=df,
        )

    def ree(
        self,
        codigo_ree: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        nome_ree: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[REE, List[REE], pd.DataFrame]]:
        """
        Obtém um registro que define os reservatórios equivalentes
        de energia existentes no estudo descrito pelo :class:`Entdados`.

        :param codigo_ree: código que especifica o registro do submercado
        :type codigo_ree: int | None
        :param codigo_submercado: código do submercado correspondente
        :type codigo_submercado: str | None
        :param nome_ree: nome do REE
        :type nome_ree: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`REE` | list[:class:`REE`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            REE,
            codigo_ree=codigo_ree,
            codigo_submercado=codigo_submercado,
            nome_ree=nome_ree,
            df=df,
        )

    def uh(
        self,
        codigo_usina: Optional[int] = None,
        nome_usina: Optional[str] = None,
        codigo_ree: Optional[int] = None,
        volume_inicial: Optional[float] = None,
        evaporacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[UH, List[UH], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina hidrelétrica existente
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_usina: índice do código que especifica o registro da UHE
        :type codigo_usina: int | None
        :param nome_usina: nome da UHE
        :type nome_usina: str | None
        :param codigo_ree: índice do ree da UHE
        :type codigo_ree: int | None
        :param volume_inicial: volume inicial da UHE
        :type volume_inicial: float | None
        :param evaporacao: consideração da evaporação na UHE
        :type evaporacao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`UH` | list[:class:`UH`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            UH,
            codigo_usina=codigo_usina,
            nome_usina=nome_usina,
            codigo_ree=codigo_ree,
            volume_inicial=volume_inicial,
            evaporacao=evaporacao,
            df=df,
        )

    def tviag(
        self,
        codigo_usina_montante: Optional[int] = None,
        codigo_elemento_jusante: Optional[int] = None,
        tipo_elemento_jusante: Optional[str] = None,
        duracao: Optional[int] = None,
        tipo_tempo_viagem: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[TVIAG, List[TVIAG], pd.DataFrame]]:
        """
        Obtém um registro que especifica os tempos de viagem da
        água entre uma UHE existente e um elemento a jusante
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_usina_montante: Índice da UHE a montante com tempo de viagem
        :type codigo_usina_montante: int | None
        :param codigo_elemento_jusante: Índice do elemento a jusante
        :type codigo_elemento_jusante: int | None
        :param tipo_elemento_jusante: Tipo do elemento a jusante (seção ou UHE)
        :type tipo_elemento_jusante: str | None
        :param duracao: duração, em horas, da viagem da água
        :type duracao: int | None
        :param tipo_tempo_viagem: ìndice do tipo do tempo de viagem (translação ou propagação)
        :type tipo_tempo_viagem: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TVIAG` | list[:class:`TVIAG`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            TVIAG,
            codigo_usina_montante=codigo_usina_montante,
            codigo_elemento_jusante=codigo_elemento_jusante,
            tipo_elemento_jusante=tipo_elemento_jusante,
            duracao=duracao,
            tipo_tempo_viagem=tipo_tempo_viagem,
            df=df,
        )

    def ut(
        self,
        codigo_usina: Optional[int] = None,
        nome_usina: Optional[str] = None,
        codigo_submercado: Optional[int] = None,
        tipo_restricao: Optional[int] = None,
        geracao_minima: Optional[float] = None,
        geracao_maxima: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[UT, List[UT], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_usina: índice do código que especifica o registro da UTE
        :type codigo_usina: int | None
        :param nome_usina: nome da UTE
        :type nome_usina: str | None
        :param codigo_submercado: índice do submercado da UTE
        :type codigo_submercado: int | None
        :param tipo_restricao: tipo de restrição
        :type tipo_restricao: int | None
        :param geracao_minima: limite de geração mínima (ou, caso restrição de rampa,
            valor da variação máxima para decréscimo de geração)
        :type geracao_minima: float | None
        :param geracao_maxima: limite de geração máxima (ou, caso restrição de rampa,
            valor da variação máxima para acréscimo de geração)
        :type geracao_maxima: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`UT` | list[:class:`UT`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            UT,
            codigo_usina=codigo_usina,
            nome_usina=nome_usina,
            codigo_submercado=codigo_submercado,
            tipo_restricao=tipo_restricao,
            geracao_minima=geracao_minima,
            geracao_maxima=geracao_maxima,
            df=df,
        )

    def usie(
        self,
        codigo_usina: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        nome_usina: Optional[str] = None,
        codigo_usina_montante: Optional[int] = None,
        codigo_usina_jusante: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[USIE, List[USIE], pd.DataFrame]]:
        """
        Obtém um registro que define as usinas elevatórias da configuração
        e seus principais dados físicos no estudo descrito pelo :class:`Entdados`.

        :param codigo_usina: código que especifica a usina elevatória
        :type codigo_usina: int | None
        :param codigo_submercado: código do submercado correspondente
        :type codigo_submercado: str | None
        :param nome_usina: nome da usina elevatória
        :type nome_usina: int | None
        :param codigo_usina_montante: código da usina a montante
        :type codigo_usina_montante: int | None
        :param codigo_usina_jusante: código da usina a jusante
        :type codigo_usina_jusante: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`USIE` | list[:class:`USIE`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            USIE,
            codigo_usina=codigo_usina,
            codigo_submercado=codigo_submercado,
            nome_usina=nome_usina,
            codigo_usina_montante=codigo_usina_montante,
            codigo_usina_jusante=codigo_usina_jusante,
            df=df,
        )

    def dp(
        self,
        codigo_submercado: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[DP, List[DP], pd.DataFrame]]:
        """
        Obtém um registro que define os dados de demanda para
        os submercados que serão consideradas para os períodos
        que não se considerada a rede elétrica no estudo descrito
        pelo :class:`Entdados`.

        :param codigo_submercado: subsistema para o qual
            valerão os patamares.
        :type codigo_submercado: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DP` | list[:class:`DP`] |
            :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            DP, codigo_submercado=codigo_submercado, df=df
        )

    def de(
        self,
        codigo_demanda_especial: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[DE, List[DE], pd.DataFrame]]:
        """
        Obtém um registro que define uma demanda especial para
        serem representadas em restrições elétricas no estudo descrito
        pelo :class:`Entdados`.

        :param codigo_demanda_especial: código da demanda especial.
        :type codigo_demanda_especial: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DE` | list[:class:`DE`] |
            :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            DE, codigo_demanda_especial=codigo_demanda_especial, df=df
        )

    def cd(
        self,
        codigo_submercado: Optional[int] = None,
        numero_curva: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CD, List[CD], pd.DataFrame]]:
        """
        Obtém um registro que define as curvas de déficit
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_submercado: submercado para o qual valerá a curva
        :type codigo_submercado: int | None
        :param numero_curva: índice da curva de déficit descrita
        :type numero_curva: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CD` | list[:class:`CD`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            CD,
            codigo_submercado=codigo_submercado,
            numero_curva=numero_curva,
            df=df,
        )

    def pq(
        self,
        codigo_usina: Optional[int] = None,
        nome_usina: Optional[str] = None,
        localizacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[PQ, List[PQ], pd.DataFrame]]:
        """
        Obtém um registro que define as gerações das pequenas usinas
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_usina: o código das gerações
        :type codigo_usina: str | None
        :param nome_usina: o nome das gerações
        :type nome_usina: str | None
        :param localizacao: índice do subsistema ou barra
            associado à geração
        :type localizacao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PQ` | list[:class:`PQ`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            PQ,
            codigo_usina=codigo_usina,
            nome_usina=nome_usina,
            localizacao=localizacao,
            df=df,
        )

    @property
    def it(self) -> Optional[IT]:
        """
        Obtém o (único) registro que contém os coeficientes
        do polinômio do canal de fuga de Itaipu em função
        da vazão na Régua 11, para casos sem FPHA Libs
        no estudo definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`IT` | None.
        """
        r = self.data.get_registers_of_type(IT)
        if isinstance(r, IT):
            return r
        else:
            return None

    def ri(
        self,
        df: bool = False,
    ) -> Optional[Union[RI, List[RI], pd.DataFrame]]:
        """
        Obtém um registro que define restrições de Itaipu
        no estudo descrito pelo :class:`Entdados`.

        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RI` | list[:class:`RI`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(RI, df=df)

    def ia(
        self,
        nome_submercado_de: Optional[str] = None,
        nome_submercado_para: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[IA, List[IA], pd.DataFrame]]:
        """
        Obtém um registro que define as capacidades de intercâmbio
        no estudo descrito pelo :class:`Entdados`.

        :param nome_submercado_de: mnemônico do submercado de origem (de).
        :type nome_submercado_de: str | None
        :param nome_submercado_para: mnemônico do submercado de destino (para).
        :type nome_submercado_para: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`IA` | list[:class:`IA`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            IA,
            nome_submercado_de=nome_submercado_de,
            nome_submercado_para=nome_submercado_para,
            df=df,
        )

    @property
    def gp(self) -> Optional[GP]:
        """
        Obtém o (único) registro que define o gap de convergência
        no estudo definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`GP` | None.
        """
        r = self.data.get_registers_of_type(GP)
        if isinstance(r, GP):
            return r
        else:
            return None

    def ac(
        self,
        codigo_usina: int,
        modificacao: Any,
        df: bool = False,
        **kwargs,
    ) -> Optional[Union[AC, List[AC], pd.DataFrame]]:
        """
        Obtém um registro que define modificações nos parâmetros
        das UHE em um :class:`Entdados`.

        :param codigo_usina: código da UHE modificada
        :type codigo_usina: int
        :param modificacao: classe da modificação realizada
        :type modificacao: subtipos do tipo `AC`
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: `AC` | list[`AC`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            modificacao, **{"codigo_usina": codigo_usina, **kwargs, "df": df}
        )

    @property
    def ni(self) -> Optional[NI]:
        """
        Obtém o (único) registro que define o número de iterações
        caso considere PDD no DESSEM no estudo
        definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`NI` | None.
        """
        r = self.data.get_registers_of_type(NI)
        if isinstance(r, NI):
            return r
        else:
            return None

    def ve(
        self, codigo_usina: Optional[int] = None, df: bool = False
    ) -> Optional[Union[VE, List[VE], pd.DataFrame]]:
        """
        Obtém um registro que especifica o volume de espera
        por UHE existente no estudo especificado no :class:`Entdados`

        :param codigo_usina: Código da usina
        :type codigo_usina: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VE` | list[:class:`VE`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(VE, codigo_usina=codigo_usina, df=df)

    def fp(
        self,
        codigo_usina: Optional[int] = None,
        tipo_tratamento_volume: Optional[int] = None,
        numero_pontos_turbinamento: Optional[int] = None,
        numero_pontos_volume: Optional[int] = None,
        verifica_concavidade: Optional[int] = None,
        ajuste_minimos_quadrados: Optional[int] = None,
        comprimento_janela_volume: Optional[float] = None,
        tolerancia_desvio: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FP, List[FP], pd.DataFrame]]:
        """
        Obtém um registro que que contém alteração de parâmetros para
        a construção da função de produção aproximada (FPHA)
        das usinas existente no estudo especificado no :class:`Entdados`

        :param codigo_usina: Código da UHE associada ao registro
        :type codigo_usina: int | None
        :param tipo_tratamento_volume: Tipo de tratamento para o eixo de
            volume
        :type tipo_tratamento_volume: int | None
        :param numero_pontos_turbinamento: número de pontos para
            discretização da janela
        :type numero_pontos_turbinamento: int | None
        :param numero_pontos_volume: número de pontos para
            discretização da janela
        :type numero_pontos_volume: int | None
        :param verifica_concavidade: Verificação da concavidade
        :type verifica_concavidade: int | None
        :param ajuste_minimos_quadrados: Ajuste de mínimos quadrados
        :type ajuste_minimos_quadrados: int | None
        :param comprimento_janela_volume: Comprimento da janela para
            discretização do volume
        :type comprimento_janela_volume: float | None
        :param tolerancia_desvio: Tolerância para desvio para na função
        :type tolerancia_desvio: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`FP` | list[:class:`FP`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            FP,
            codigo_usina=codigo_usina,
            tipo_tratamento_volume=tipo_tratamento_volume,
            numero_pontos_turbinamento=numero_pontos_turbinamento,
            numero_pontos_volume=numero_pontos_volume,
            verifica_concavidade=verifica_concavidade,
            ajuste_minimos_quadrados=ajuste_minimos_quadrados,
            comprimento_janela_volume=comprimento_janela_volume,
            tolerancia_desvio=tolerancia_desvio,
            df=df,
        )

    @property
    def tx(self) -> Optional[TX]:
        """
        Obtém o (único) registro que define a taxa de desconto
        aplicada no estudo definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`TX` | None.
        """
        r = self.data.get_registers_of_type(TX)
        if isinstance(r, TX):
            return r
        else:
            return None

    def ez(
        self, codigo_usina: Optional[int] = None, df: bool = False
    ) -> Optional[Union[EZ, List[EZ], pd.DataFrame]]:
        """
        Obtém um registro que especifica o percentual máximo do
        volume útil para acoplamento no estudo especificado
        no :class:`Entdados`

        :param codigo_usina: Código da usina
        :type codigo_usina: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EZ` | list[:class:`EZ`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(EZ, codigo_usina=codigo_usina, df=df)

    def r11(
        self, df: bool = False
    ) -> Optional[Union[R11, List[R11], pd.DataFrame]]:
        """
        Obtém um registro que contém as restrições de variação
        horária e diária no nível da Régua 11 existente no estudo
        especificado no :class:`Entdados`

        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`R11` | list[:class:`R11`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(R11, df=df)

    def cr(
        self,
        codigo_secao: Optional[int] = None,
        nome_secao: Optional[str] = None,
        grau: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CR, List[CR], pd.DataFrame]]:
        """
        Obtém um registro que especifica o polinômio cota x vazão para seções
        de rio no estudo especificado no :class:`Entdados`

        :param codigo_secao: Código da seção
        :type codigo_secao: int | None
        :param nome_secao: Nome da seção
        :type nome_secao: str | None
        :param grau: Grau do polinômio
        :type grau: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CR` | list[:class:`CR`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            CR,
            codigo_secao=codigo_secao,
            nome_secao=nome_secao,
            grau=grau,
            df=df,
        )

    def secr(
        self,
        codigo_secao: Optional[int] = None,
        nome_secao: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[SECR, List[SECR], pd.DataFrame]]:
        """
        Obtém um registro que define as seções de rio
        no estudo especificado no :class:`Entdados`

        :param codigo_secao: Código da seção
        :type codigo_secao: int | None
        :param nome_secao: Nome da seção
        :type nome_secao: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`SECR` | list[:class:`SECR`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            SECR, codigo_secao=codigo_secao, nome_secao=nome_secao, df=df
        )

    def da(
        self, codigo_usina: Optional[int] = None, df: bool = False
    ) -> Optional[Union[DA, List[DA], pd.DataFrame]]:
        """
        Obtém um registro que especifica a taxa de retirada de água
        para uma usina existente no estudo especificado no :class:`Entdados`

        :param codigo_usina: Código da usina
        :type codigo_usina: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DA` | list[:class:`DA`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(DA, codigo_usina=codigo_usina, df=df)

    def re(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[RE, List[RE], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição elétrica existente
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_restricao: código que especifica o registro
            da restrição elétrica
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
        :rtype: :class:`RE` | list[:class:`RE`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            RE,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            df=df,
        )

    def lu(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LU, List[LU], pd.DataFrame]]:
        """
        Obtém um registro que especifica o limite inferior e
        superior de uma restrição elétrica existente
        no estudo descrito pelo :class:`Entdados`.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
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
        :rtype: :class:`LU` | list[:class:`LU`] | :class:`pd.DataFrame` | None

        """

        return self.__registros_ou_df(
            LU,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            df=df,
        )

    def fh(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FH, List[FH], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas para usinas hidráulicas.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param codigo_usina: código da usina hidráulica
        :type codigo_usina: int | None
        :param codigo_conjunto: conjunto de máquinas da usina
        :type codigo_conjunto: int | None
        :param coeficiente: coeficiente de participação da usina na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FH` | list[:class:`FH`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            FH,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            coeficiente=coeficiente,
            df=df,
        )

    def ft(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FT, List[FT], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas para usinas térmicas.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param codigo_usina: código da usina hidráulica
        :type codigo_usina: int | None
        :param coeficiente: coeficiente de participação da usina na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FT` | list[:class:`FT`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            FT,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            codigo_usina=codigo_usina,
            coeficiente=coeficiente,
            df=df,
        )

    def fi(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        nome_submercado_de: Optional[int] = None,
        nome_submercado_para: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FI, List[FI], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas para intercâmbios.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param nome_submercado_de: mnemônico do submercado origem (de)
        :type nome_submercado_de: str | None
        :param nome_submercado_para: mnemônico do submercado destino (para)
        :type nome_submercado_para: str | None
        :param coeficiente: coeficiente de participação do fluxo na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FI` | list[:class:`FI`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            FI,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            nome_submercado_de=nome_submercado_de,
            nome_submercado_para=nome_submercado_para,
            coeficiente=coeficiente,
            df=df,
        )

    def fe(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        codigo_contrato: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FE, List[FE], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas para contratos de importação/exportação de energia.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param codigo_contrato: código do contrato
        :type codigo_contrato: int | None
        :param coeficiente: coeficiente de participação do contrato na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FE` | list[:class:`FE`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            FE,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            codigo_contrato=codigo_contrato,
            coeficiente=coeficiente,
            df=df,
        )

    def fr(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FR, List[FR], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas para usinas de fontes renováveis.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param codigo_usina: código da usina renovável
        :type codigo_usina: int | None
        :param coeficiente: coeficiente de participação da usina na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FR` | list[:class:`FR`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            FR,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            codigo_usina=codigo_usina,
            coeficiente=coeficiente,
            df=df,
        )

    def fc(
        self,
        codigo_restricao: Optional[int] = None,
        dia_inicial: Optional[Union[str, int]] = None,
        hora_inicial: Optional[int] = None,
        meia_hora_inicial: Optional[int] = None,
        dia_final: Optional[Union[str, int]] = None,
        hora_final: Optional[int] = None,
        meia_hora_final: Optional[int] = None,
        codigo_demanda: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FC, List[FC], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas para demandas especiais.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param dia_inicial: dia inicial
        :type dia_inicial: int | None
        :param hora_inicial: hora inicial
        :type hora_inicial: int | None
        :param meia_hora_inicial: meia-hora inicial
        :param dia_final: dia final
        :type dia_final: int | None
        :param hora_final: hora final
        :type hora_final: int | None
        :param meia_hora_final: meia-hora final
        :type meia_hora_final: int | None
        :param codigo_demanda: código da demanda especial
        :type codigo_demanda: int | None
        :param coeficiente: coeficiente de participação da usina na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FR` | list[:class:`FR`] | :class:`pd.DataFrame` | None
        """

        return self.__registros_ou_df(
            FC,
            codigo_restricao=codigo_restricao,
            dia_inicial=dia_inicial,
            hora_inicial=hora_inicial,
            meia_hora_inicial=meia_hora_inicial,
            dia_final=dia_final,
            hora_final=hora_final,
            meia_hora_final=meia_hora_final,
            codigo_demanda=codigo_demanda,
            coeficiente=coeficiente,
            df=df,
        )

    def mh(
        self,
        codigo_usina: Optional[int] = None,
        codigo_conjunto: Optional[int] = None,
        codigo_unidade: Optional[int] = None,
        disponivel: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[MH, List[MH], pd.DataFrame]]:
        """
        Obtém um registro que especifica a taxa de retirada de água
        para uma usina existente no estudo especificado no :class:`Entdados`

        :param codigo_usina: Código da usina
        :type codigo_usina: int | None
        :param codigo_conjunto: Código do conjunto
        :type codigo_conjunto: int | None
        :param codigo_unidade: Código da unidade
        :type codigo_unidade: int | None
        :param disponivel: Flag disponibilidade
        :type disponivel: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`MH` | list[:class:`MH`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            MH,
            codigo_usina=codigo_usina,
            codigo_conjunto=codigo_conjunto,
            codigo_unidade=codigo_unidade,
            disponivel=disponivel,
            df=df,
        )

    @property
    def pe(self) -> Optional[PE]:
        """
        Obtém o (único) registro que contém penalidades no estudo
        definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`PE` | None.
        """
        r = self.data.get_registers_of_type(PE)
        if isinstance(r, PE):
            return r
        else:
            return None
