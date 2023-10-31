from typing import Type, TypeVar, Optional, List, Union
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
import pandas as pd  # type: ignore
from idessem.dessem.modelos.vazaolateral import (
    HidreletricaVazaoJusanteInfluenciaUsina,
    HidreletricaVazaoJusanteInfluenciaDefluencia,
    HidreletricaVazaoJusanteInfluenciaPosto,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class VazaoLateral(RegisterFile):
    """ """

    T = TypeVar("T")

    REGISTERS = [
        HidreletricaVazaoJusanteInfluenciaUsina,
        HidreletricaVazaoJusanteInfluenciaDefluencia,
        HidreletricaVazaoJusanteInfluenciaPosto,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="vazaolateral.csv"
    ) -> "VazaoLateral":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="vazaolateral.csv"):
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

    def vazao_jusante_influencia_defluencia(
        self,
        codigo_usina_influenciada: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaVazaoJusanteInfluenciaDefluencia,
            List[HidreletricaVazaoJusanteInfluenciaDefluencia],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que identificam a usina e fatores de influência do turbinamento e
        vertimento na vazão de jusante da própria usina. Opcionalmente, o retorno
        pode ser transformado em um `DataFrame`, apenas para leitura das informações.

        :param codigo_usina_influenciada: código da usina influenciada
        :type codigo_usina_influenciada: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaVazaoJusanteInfluenciaDefluencia` |
            List[`HidreletricaVazaoJusanteInfluenciaDefluencia`] | `None` | `DataFrame`
        """
        if df:
            return self._as_df(HidreletricaVazaoJusanteInfluenciaDefluencia)
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaVazaoJusanteInfluenciaDefluencia,
                codigo_usina_influenciada=codigo_usina_influenciada,
            )

    def vazao_jusante_influencia_posto(
        self,
        codigo_usina_influenciada: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaVazaoJusanteInfluenciaPosto,
            List[HidreletricaVazaoJusanteInfluenciaPosto],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que identificam a usina influenciada e a usina influenciadora e
        fator de influência da vazão incremental na vazão de jusante da usina influenciada.
        Opcionalmente, o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina_influenciada: código da usina influenciada
        :type codigo_usina_influenciada: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaVazaoJusanteInfluenciaDefluencia` |
            List[`HidreletricaVazaoJusanteInfluenciaDefluencia`] | `None` | `DataFrame`
        """
        if df:
            return self._as_df(HidreletricaVazaoJusanteInfluenciaPosto)
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaVazaoJusanteInfluenciaPosto,
                codigo_usina_influenciada=codigo_usina_influenciada,
            )

    def vazao_jusante_influencia_usina(
        self,
        codigo_usina_influenciada: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaVazaoJusanteInfluenciaUsina,
            List[HidreletricaVazaoJusanteInfluenciaUsina],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que identificam a usina influenciada e a usina influenciadora e
        fator de influência da vazão defluente na vazão de jusante da usina influenciada.
        Opcionalmente, o retorno pode ser transformado em um `DataFrame`, apenas para
        leitura das informações.

        :param codigo_usina_influenciada: código da usina influenciada
        :type codigo_usina_influenciada: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaVazaoJusanteInfluenciaUsina` |
            List[`HidreletricaVazaoJusanteInfluenciaUsina`] | `None` | `DataFrame`
        """
        if df:
            return self._as_df(HidreletricaVazaoJusanteInfluenciaUsina)
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaVazaoJusanteInfluenciaUsina,
                codigo_usina_influenciada=codigo_usina_influenciada,
            )
