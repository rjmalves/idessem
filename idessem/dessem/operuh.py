from idessem.dessem.modelos.operuh import REST, ELEM, LIM, VAR
import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile
from cfinterface.components.register import Register
from typing import Type, List, Optional, TypeVar, Union


# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Operuh(RegisterFile):
    """
    Armazena os dados com as restrições operativas para as
    usinas hidrelétricas do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `operuh.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    REGISTERS = [
        REST,
        ELEM,
        LIM,
        VAR,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="operuh.dat") -> "Operuh":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="operuh.dat"):
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

    def rest(
        self,
        codigo_restricao: Optional[int] = None,
        tipo: Optional[str] = None,
        intervalo_aplicacao: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[REST, List[REST], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição hidráulica existente
        no estudo descrito pelo :class:`Operuh`.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param tipo: tipo da restrição (L,V)
        :type tipo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`REST` | list[:class:`REST`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(REST)
        else:
            return self.__obtem_registros_com_filtros(
                REST,
                codigo_restricao=codigo_restricao,
                tipo=tipo,
                intervalo_aplicacao=intervalo_aplicacao,
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
        if df:
            return self._as_df(ELEM)
        else:
            return self.__obtem_registros_com_filtros(
                ELEM,
                codigo_restricao=codigo_restricao,
                codigo_usina=codigo_usina,
                coeficiente=coeficiente,
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

        if df:
            return self._as_df(LIM)
        else:
            return self.__obtem_registros_com_filtros(
                LIM,
                codigo_restricao=codigo_restricao,
                dia_inicial=dia_inicial,
                hora_inicial=hora_inicial,
                meia_hora_inicial=meia_hora_inicial,
                dia_final=dia_final,
                hora_final=hora_final,
                meia_hora_final=meia_hora_final,
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

        if df:
            return self._as_df(VAR)
        else:
            return self.__obtem_registros_com_filtros(
                VAR,
                codigo_restricao=codigo_restricao,
                dia_inicial=dia_inicial,
                hora_inicial=hora_inicial,
                meia_hora_inicial=meia_hora_inicial,
                dia_final=dia_final,
                hora_final=hora_final,
                meia_hora_final=meia_hora_final,
            )
