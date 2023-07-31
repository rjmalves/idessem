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
from cfinterface.components.register import Register
from typing import Type, List, Optional, TypeVar, Union, Any


# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Entdados(RegisterFile):
    """
    Armazena os dados de entrada gerais do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `entdados.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="entdados.dat"
    ) -> "Entdados":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="entdados.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def __registros_por_tipo(self, registro: Type[T]) -> List[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.
        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
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

    def lista_registros(self, tipo: Type[T]) -> List[T]:
        """
        Lista todos os registros presentes no arquivo que tenham o tipo `T`.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        return [r for r in self.data.of_type(tipo)]

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
    def rd(self) -> Optional[RD]:
        """
        Obtém o (único) registro que define as opções de representação da
        rede elétrica no estudo descrito pelo :class:`Entdados`.

        :return: Um registro, se existir.
        :rtype: :class:`RD` | None
        """
        return self.__obtem_registro(RD)

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
        if df:
            return self._as_df(RIVAR)
        else:
            return self.__obtem_registros_com_filtros(
                RIVAR,
                codigo_entidade=codigo_entidade,
                tipo_variavel=tipo_variavel,
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
        :param patamar_de_carga: nome do patamar de carga
        :type patamar_de_carga: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TM` | list[:class:`TM`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(TM)
        else:
            return self.__obtem_registros_com_filtros(
                TM,
                dia_inicial=dia_inicial,
                hora_inicial=hora_inicial,
                meia_hora_inicial=meia_hora_inicial,
            )

    def sist(
        self,
        codigo: Optional[int] = None,
        nome: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[SIST, List[SIST], pd.DataFrame]]:
        """
        Obtém um registro que define os submercados existentes
        no estudo descrito pelo :class:`Entdados`.

        :param codigo: código que especifica o registro do submercado
        :type codigo: int | None
        :param mnemônico: mnemônico do submercado
        :type mnemônico: str | None
        :param ficticio: flag que identifica submercado fictício
        :type ficticio: int | None
        :param nome: nome do submercado
        :type nome: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`SIST` | list[:class:`SIST`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(SIST)
        else:
            return self.__obtem_registros_com_filtros(
                SIST, codigo=codigo, nome=nome
            )

    def ree(
        self,
        codigo: Optional[int] = None,
        submercado: Optional[int] = None,
        nome: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[REE, List[REE], pd.DataFrame]]:
        """
        Obtém um registro que define os reservatórios equivalentes
        de energia existentes no estudo descrito pelo :class:`Entdados`.

        :param codigo: código que especifica o registro do submercado
        :type codigo: int | None
        :param submercado: código do submercado correspondente
        :type submercado: str | None
        :param nome: nome do REE
        :type nome: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`REE` | list[:class:`REE`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(REE)
        else:
            return self.__obtem_registros_com_filtros(
                REE, codigo=codigo, submercado=submercado, nome=nome
            )

    def uh(
        self,
        codigo: Optional[int] = None,
        nome: Optional[str] = None,
        ree: Optional[int] = None,
        volume_inicial: Optional[float] = None,
        evaporacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[UH, List[UH], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina hidrelétrica existente
        no estudo descrito pelo :class:`Entdados`.

        :param codigo: índice do código que especifica o registro da UHE
        :type codigo: int | None
        :param nome: nome da UHE
        :type nome: str | None
        :param ree: índice do ree da UHE
        :type ree: int | None
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
        if df:
            return self._as_df(UH)
        else:
            return self.__obtem_registros_com_filtros(
                UH,
                codigo=codigo,
                nome=nome,
                ree=ree,
                volume_inicial=volume_inicial,
                evaporacao=evaporacao,
            )

    def tviag(
        self,
        uhe_montante: Optional[int] = None,
        elemento_jusante: Optional[int] = None,
        tipo_elemento_jusante: Optional[str] = None,
        duracao: Optional[int] = None,
        tipo_tempo_viagem: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[TVIAG, List[TVIAG], pd.DataFrame]]:
        """
        Obtém um registro que especifica os tempos de viagem da
        água entre uma UHE existente e um elemento a jusante
        no estudo descrito pelo :class:`Entdados`.

        :param uhe_montante: Índice da UHE a montante com tempo de viagem
        :type uhe_montante: int | None
        :param elemento_jusante: Índice do elemento a jusante
        :type elemento_jusante: int | None
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
        if df:
            return self._as_df(TVIAG)
        else:
            return self.__obtem_registros_com_filtros(
                TVIAG,
                uhe_montante=uhe_montante,
                elemento_jusante=elemento_jusante,
                tipo_elemento_jusante=tipo_elemento_jusante,
                duracao=duracao,
                tipo_tempo_viagem=tipo_tempo_viagem,
            )

    def ut(
        self,
        codigo: Optional[int] = None,
        nome: Optional[str] = None,
        submercado: Optional[int] = None,
        tipo_restricao: Optional[int] = None,
        geracao_minima: Optional[float] = None,
        geracao_maxima: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[UT, List[UT], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`Entdados`.

        :param codigo: índice do código que especifica o registro da UTE
        :type codigo: int | None
        :param nome: nome da UTE
        :type nome: str | None
        :param submercado: índice do submercado da UTE
        :type submercado: int | None
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
        if df:
            return self._as_df(UT)
        else:
            return self.__obtem_registros_com_filtros(
                UT,
                codigo=codigo,
                nome=nome,
                submercado=submercado,
                tipo_restricao=tipo_restricao,
                geracao_minima=geracao_minima,
                geracao_maxima=geracao_maxima,
            )

    def usie(
        self,
        codigo: Optional[int] = None,
        submercado: Optional[int] = None,
        nome: Optional[str] = None,
        uhe_montante: Optional[int] = None,
        uhe_jusante: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[USIE, List[USIE], pd.DataFrame]]:
        """
        Obtém um registro que define as usinas elevatórias da configuração
        e seus principais dados físicos no estudo descrito pelo :class:`Entdados`.

        :param codigo: código que especifica a usina elevatória
        :type codigo: int | None
        :param submercado: código do submercado correspondente
        :type submercado: str | None
        :param nome: nome da usina elevatória
        :type nome: int | None
        :param uhe_montante: código da usina a montante
        :type uhe_montante: int | None
        :param uhe_jusante: código da usina a jusante
        :type uhe_jusante: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`USIE` | list[:class:`USIE`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(USIE)
        else:
            return self.__obtem_registros_com_filtros(
                USIE,
                codigo=codigo,
                submercado=submercado,
                nome=nome,
                uhe_montante=uhe_montante,
                uhe_jusante=uhe_jusante,
            )

    def dp(
        self,
        submercado: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[DP, List[DP], pd.DataFrame]]:
        """
        Obtém um registro que define os dados de demanda para
        os submercados que serão consideradas para os períodos
        que não se considerada a rede elétrica no estudo descrito
        pelo :class:`Entdados`.

        :param submercado: subsistema para o qual
            valerão os patamares.
        :type submercado: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DP` | list[:class:`DP`] |
            :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(DP)
        else:
            return self.__obtem_registros_com_filtros(
                DP,
                submercado=submercado,
            )

    def de(
        self,
        codigo: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[DE, List[DE], pd.DataFrame]]:
        """
        Obtém um registro que define uma demanda especial para
        serem representadas em restrições elétricas no estudo descrito
        pelo :class:`Entdados`.

        :param codigo: código da demanda especial.
        :type codigo: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DE` | list[:class:`DE`] |
            :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(DE)
        else:
            return self.__obtem_registros_com_filtros(
                DE,
                codigo=codigo,
            )

    def cd(
        self,
        submercado: Optional[int] = None,
        numero_curva: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CD, List[CD], pd.DataFrame]]:
        """
        Obtém um registro que define as curvas de déficit
        no estudo descrito pelo :class:`Entdados`.

        :param submercado: submercado para o qual valerá a curva
        :type submercado: int | None
        :param numero_curva: índice da curva de déficit descrita
        :type numero_curva: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CD` | list[:class:`CD`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(CD)
        else:
            return self.__obtem_registros_com_filtros(
                CD,
                submercado=submercado,
                numero_curva=numero_curva,
            )

    def pq(
        self,
        codigo: Optional[int] = None,
        nome: Optional[str] = None,
        localizacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[PQ, List[PQ], pd.DataFrame]]:
        """
        Obtém um registro que define as gerações das pequenas usinas
        no estudo descrito pelo :class:`Entdados`.

        :param codigo: o código das gerações
        :type codigo: str | None
        :param nome: o nome das gerações
        :type nome: str | None
        :param localizacao: índice do subsistema ou barra
            associado à geração
        :type localizacao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PQ` | list[:class:`PQ`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(PQ)
        else:
            return self.__obtem_registros_com_filtros(
                PQ,
                codigo=codigo,
                nome=nome,
                localizacao=localizacao,
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
        return self.__obtem_registro(IT)

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
        if df:
            return self._as_df(RI)
        else:
            return self.__obtem_registros_com_filtros(
                RI,
            )

    def ia(
        self,
        submercado_de: Optional[str] = None,
        submercado_para: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[IA, List[IA], pd.DataFrame]]:
        """
        Obtém um registro que define as capacidades de intercâmbio
        no estudo descrito pelo :class:`Entdados`.

        :param submercado_de: mnemônico do submercado de origem (de).
        :type submercado_de: str | None
        :param submercado_para: mnemônico do submercado de destino (para).
        :type submercado_para: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`IA` | list[:class:`IA`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(IA)
        else:
            return self.__obtem_registros_com_filtros(
                IA,
                submercado_de=submercado_de,
                submercado_para=submercado_para,
            )

    @property
    def gp(self) -> Optional[GP]:
        """
        Obtém o (único) registro que define o gap de convergência
        no estudo definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`GP` | None.
        """
        return self.__obtem_registro(GP)

    def ac(
        self,
        uhe: int,
        modificacao: Any,
        df: bool = False,
        **kwargs,
    ) -> Optional[Union[AC, List[AC], pd.DataFrame]]:
        """
        Obtém um registro que define modificações nos parâmetros
        das UHE em um :class:`Entdados`.

        :param uhe: código da UHE modificada
        :type uhe: int
        :param modificacao: classe da modificação realizada
        :type modificacao: subtipos do tipo `AC`
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: `AC` | list[`AC`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(modificacao)
        else:
            return self.__obtem_registros_com_filtros(
                modificacao, **{"uhe": uhe, **kwargs}
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
        return self.__obtem_registro(NI)

    def ve(
        self, codigo: Optional[int] = None, df: bool = False
    ) -> Optional[Union[VE, List[VE], pd.DataFrame]]:
        """
        Obtém um registro que especifica o volume de espera
        por UHE existente no estudo especificado no :class:`Entdados`

        :param codigo: Código da usina
        :type codigo: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VE` | list[:class:`VE`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(VE)
        else:
            return self.__obtem_registros_com_filtros(VE, codigo=codigo)

    def fp(
        self,
        codigo: Optional[int] = None,
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

        :param codigo: Código da UHE associada ao registro
        :type codigo: int | None
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
        if df:
            return self._as_df(FP)
        else:
            return self.__obtem_registros_com_filtros(
                FP,
                codigo=codigo,
                tipo_tratamento_volume=tipo_tratamento_volume,
                numero_pontos_turbinamento=numero_pontos_turbinamento,
                numero_pontos_volume=numero_pontos_volume,
                verifica_concavidade=verifica_concavidade,
                ajuste_minimos_quadrados=ajuste_minimos_quadrados,
                comprimento_janela_volume=comprimento_janela_volume,
                tolerancia_desvio=tolerancia_desvio,
            )

    @property
    def tx(self) -> Optional[TX]:
        """
        Obtém o (único) registro que define a taxa de desconto
        aplicada no estudo definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`TX` | None.
        """
        return self.__obtem_registro(TX)

    def ez(
        self, uhe: Optional[int] = None, df: bool = False
    ) -> Optional[Union[EZ, List[EZ], pd.DataFrame]]:
        """
        Obtém um registro que especifica o percentual máximo do
        volume útil para acoplamento no estudo especificado
        no :class:`Entdados`

        :param uhe: Código da usina
        :type uhe: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EZ` | list[:class:`EZ`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(EZ)
        else:
            return self.__obtem_registros_com_filtros(EZ, uhe=uhe)

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
        if df:
            return self._as_df(R11)
        else:
            return self.__obtem_registros_com_filtros(R11)

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
        if df:
            return self._as_df(CR)
        else:
            return self.__obtem_registros_com_filtros(
                CR, codigo_secao=codigo_secao, nome_secao=nome_secao, grau=grau
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
        if df:
            return self._as_df(SECR)
        else:
            return self.__obtem_registros_com_filtros(
                SECR, codigo_secao=codigo_secao, nome_secao=nome_secao
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
        if df:
            return self._as_df(DA)
        else:
            return self.__obtem_registros_com_filtros(
                DA, codigo_usina=codigo_usina
            )

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
        if df:
            return self._as_df(RE)
        else:
            return self.__obtem_registros_com_filtros(
                RE,
                codigo_restricao=codigo_restricao,
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

        if df:
            return self._as_df(LU)
        else:
            return self.__obtem_registros_com_filtros(
                LU,
                codigo_restricao=codigo_restricao,
                dia_inicial=dia_inicial,
                hora_inicial=hora_inicial,
                meia_hora_inicial=meia_hora_inicial,
                dia_final=dia_final,
                hora_final=hora_final,
                meia_hora_final=meia_hora_final,
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
        conjunto: Optional[int] = None,
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
        :param conjunto: conjunto de máquinas da usina
        :type conjunto: int | None
        :param coeficiente: coeficiente de participação da usina na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FH` | list[:class:`FH`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(FH)
        else:
            return self.__obtem_registros_com_filtros(
                FH,
                codigo_restricao=codigo_restricao,
                dia_inicial=dia_inicial,
                hora_inicial=hora_inicial,
                meia_hora_inicial=meia_hora_inicial,
                dia_final=dia_final,
                hora_final=hora_final,
                meia_hora_final=meia_hora_final,
                codigo_usina=codigo_usina,
                conjunto=conjunto,
                coeficiente=coeficiente,
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
        if df:
            return self._as_df(FT)
        else:
            return self.__obtem_registros_com_filtros(
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
        submercado_de: Optional[int] = None,
        submercado_para: Optional[int] = None,
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
        :param submercado_de: mnemônico do submercado origem (de)
        :type submercado_de: str | None
        :param submercado_para: mnemônico do submercado destino (para)
        :type submercado_para: str | None
        :param coeficiente: coeficiente de participação do fluxo na restrição
        :type coeficiente: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FI` | list[:class:`FI`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(FI)
        else:
            return self.__obtem_registros_com_filtros(
                FI,
                codigo_restricao=codigo_restricao,
                dia_inicial=dia_inicial,
                hora_inicial=hora_inicial,
                meia_hora_inicial=meia_hora_inicial,
                dia_final=dia_final,
                hora_final=hora_final,
                meia_hora_final=meia_hora_final,
                submercado_de=submercado_de,
                submercado_para=submercado_para,
                coeficiente=coeficiente,
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
        if df:
            return self._as_df(FE)
        else:
            return self.__obtem_registros_com_filtros(
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
        if df:
            return self._as_df(FR)
        else:
            return self.__obtem_registros_com_filtros(
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
        if df:
            return self._as_df(FC)
        else:
            return self.__obtem_registros_com_filtros(
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
        if df:
            return self._as_df(MH)
        else:
            return self.__obtem_registros_com_filtros(
                MH,
                codigo_usina=codigo_usina,
                codigo_conjunto=codigo_conjunto,
                codigo_unidade=codigo_unidade,
                disponivel=disponivel,
            )

    @property
    def pe(self) -> Optional[PE]:
        """
        Obtém o (único) registro que contém penalidades no estudo
        definido no :class:`Entdados`

        :return: Um registro, se existir.
        :rtype: :class:`PE` | None.
        """
        return self.__obtem_registro(PE)
