from idessem.dessem.modelos.renovaveis import (
    EOLICA,
    EOLICABARRA,
    EOLICASUBM,
    EOLICAGERACAO,
)
import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile
from cfinterface.components.register import Register
from typing import Type, List, Optional, TypeVar, Union

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Renovaveis(RegisterFile):
    """
    Armazena os dados de entrada do DESSEM associados a geração de renováveis
    e fontes não simuladas.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `renovaveis.dat`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    REGISTERS = [EOLICAGERACAO, EOLICASUBM, EOLICABARRA, EOLICA]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="renovaveis.dat"
    ) -> "Renovaveis":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="renovaveis.dat"):
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
        if df:
            return self._as_df(EOLICA)
        else:
            return self.__obtem_registros_com_filtros(
                EOLICA,
                codigo_usina=codigo_usina,
                nome_usina=nome_usina,
                constrained_off=constrained_off,
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
        if df:
            return self._as_df(EOLICABARRA)
        else:
            return self.__obtem_registros_com_filtros(
                EOLICABARRA,
                codigo_usina=codigo_usina,
                codigo_barra=codigo_barra,
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
        if df:
            return self._as_df(EOLICASUBM)
        else:
            return self.__obtem_registros_com_filtros(
                EOLICASUBM,
                codigo_usina=codigo_usina,
                submercado=submercado,
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
        if df:
            return self._as_df(EOLICAGERACAO)
        else:
            return self.__obtem_registros_com_filtros(
                EOLICAGERACAO,
                codigo_usina=codigo_usina,
            )
