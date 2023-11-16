from idessem.dessem.modelos.termdat import CADUSIT, CADUNIDT, CADCONF, CADMIN
import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile
from cfinterface.components.register import Register
from typing import Type, List, Optional, TypeVar, Union


# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Term(RegisterFile):
    """
    Armazena os dados com as características de cadastro das usinas
    termelétricas do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `termdat.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    REGISTERS = [CADUSIT, CADUNIDT, CADCONF, CADMIN]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="termdat.dat") -> "Term":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="termdat.dat"):
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
        if df:
            return self._as_df(CADUSIT)
        else:
            return self.__obtem_registros_com_filtros(
                CADUSIT,
                codigo_usina=codigo_usina,
            )

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
        if df:
            return self._as_df(CADUNIDT)
        else:
            return self.__obtem_registros_com_filtros(
                CADUSIT,
                codigo_usina=codigo_usina,
                codigo_unidade=codigo_unidade,
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
        if df:
            return self._as_df(CADCONF)
        else:
            return self.__obtem_registros_com_filtros(
                CADUSIT,
                codigo_usina=codigo_usina,
                codigo_unidade_equivalente=codigo_unidade_equivalente,
                codigo_unidade=codigo_unidade,
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
        if df:
            return self._as_df(CADMIN)
        else:
            return self.__obtem_registros_com_filtros(
                CADUSIT,
                codigo_usina=codigo_usina,
                codigo_unidade_equivalente=codigo_unidade_equivalente,
            )
