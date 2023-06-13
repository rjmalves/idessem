from typing import Type, TypeVar, Optional, List, Union
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
import pandas as pd  # type: ignore
from idessem.dessem.modelos.polinjus import (
    HidreletricaCurvaJusante,
    HidreletricaCurvaJusantePolinomioPorPartes,
    HidreletricaCurvaJusantePolinomioPorPartesSegmento,
    HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
    HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Polinjus(RegisterFile):
    """ """

    T = TypeVar("T")

    REGISTERS = [
        HidreletricaCurvaJusantePolinomioPorPartesSegmento,
        HidreletricaCurvaJusantePolinomioPorPartes,
        HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
        HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
        HidreletricaCurvaJusante,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="polinjus.csv"
    ) -> "Polinjus":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="polinjus.csv"):
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

    def hidreletrica_curvajusante(
        self,
        codigo_usina: Optional[int] = None,
        indice_familia: Optional[int] = None,
        nivel_montante_referencia: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaCurvaJusante,
            List[HidreletricaCurvaJusante],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que cadastram uma família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param nivel_montante_referencia: nível de montante de usina de
            jusante para cálculo da queda
        :type nivel_montante_referencia: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaCurvaJusante` |
            List[`HidreletricaCurvaJusante`] | `None` | `DataFrame`
        """
        if df:
            return self._as_df(HidreletricaCurvaJusante)
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaCurvaJusante,
                codigo_usina=codigo_usina,
                indice_familia=indice_familia,
                nivel_montante_referencia=nivel_montante_referencia,
            )

    def hidreletrica_curvajusante_polinomio(
        self,
        codigo_usina: Optional[int] = None,
        indice_familia: Optional[int] = None,
        numero_polinomios: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaCurvaJusantePolinomioPorPartes,
            List[HidreletricaCurvaJusantePolinomioPorPartes],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que cadastram uma família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param numero_polinomios: número de polinômios da família
        :type numero_polinomios: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaCurvaJusantePolinomioPorPartes` |
            List[`HidreletricaCurvaJusantePolinomioPorPartes`] | `None` | `DataFrame`
        """
        if df:
            return self._as_df(HidreletricaCurvaJusantePolinomioPorPartes)
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaCurvaJusantePolinomioPorPartes,
                codigo_usina=codigo_usina,
                indice_familia=indice_familia,
                numero_polinomios=numero_polinomios,
            )

    def hidreletrica_curvajusante_polinomio_segmento(
        self,
        codigo_usina: Optional[int] = None,
        indice_familia: Optional[int] = None,
        indice_polinomio: Optional[int] = None,
        limite_inferior_vazao_jusante: Optional[float] = None,
        limite_superior_vazao_jusante: Optional[float] = None,
        coeficiente_a0: Optional[float] = None,
        coeficiente_a1: Optional[float] = None,
        coeficiente_a2: Optional[float] = None,
        coeficiente_a3: Optional[float] = None,
        coeficiente_a4: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaCurvaJusantePolinomioPorPartesSegmento,
            List[HidreletricaCurvaJusantePolinomioPorPartesSegmento],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que cadastram os polinômios para cada família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param indice_polinomio: índice do polinômio da família
        :type indice_polinomio: int | None
        :param limite_inferior_vazao_jusante: limite inferior de vazão de
            jusante para janela de validade do polinômio
        :type limite_inferior_vazao_jusante: float | None
        :param limite_superior_vazao_jusante: limite superior de vazão de
            jusante para janela de validade do polinômio
        :type limite_superior_vazao_jusante: float | None
        :param coeficiente_a0: coeficiente de grau 0 do polinômio
        :type coeficiente_a0: float | None
        :param coeficiente_a1: coeficiente de grau 1 do polinômio
        :type coeficiente_a1: float | None
        :param coeficiente_a2: coeficiente de grau 2 do polinômio
        :type coeficiente_a2: float | None
        :param coeficiente_a3: coeficiente de grau 3 do polinômio
        :type coeficiente_a3: float | None
        :param coeficiente_a4: coeficiente de grau 4 do polinômio
        :type coeficiente_a4: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HidreletricaCurvaJusantePolinomioPorPartesSegmento` |
            list[:class:`HidreletricaCurvaJusantePolinomioPorPartesSegmento`] |
            None
        """
        if df:
            return self._as_df(
                HidreletricaCurvaJusantePolinomioPorPartesSegmento
            )
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaCurvaJusantePolinomioPorPartesSegmento,
                codigo_usina=codigo_usina,
                indice_familia=indice_familia,
                indice_polinomio=indice_polinomio,
                limite_inferior_vazao_jusante=limite_inferior_vazao_jusante,
                limite_superior_vazao_jusante=limite_superior_vazao_jusante,
                coeficiente_a0=coeficiente_a0,
                coeficiente_a1=coeficiente_a1,
                coeficiente_a2=coeficiente_a2,
                coeficiente_a3=coeficiente_a3,
                coeficiente_a4=coeficiente_a4,
            )

    def hidreletrica_curvajusante_afogamentoexplicito_usina(
        self,
        codigo_usina: Optional[int] = None,
        considera_afogamento: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
            List[HidreletricaCurvaJusanteAfogamentoExplicitoUsina],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que habilitam ou desabilitam a consideração
        do tratamento do afogamento explícito por usina. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param considera_afogamento: habilitação do afogamento
        :type considera_afogamento: str | None
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaCurvaJusante` |
            List[`HidreletricaCurvaJusante`] | `None` | `DataFrame`
        """
        if df:
            return self._as_df(
                HidreletricaCurvaJusanteAfogamentoExplicitoUsina
            )
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
                codigo_usina=codigo_usina,
                considera_afogamento=considera_afogamento,
            )

    def hidreletrica_curvajusante_afogamentoexplicito_padrao(
        self,
        considera_afogamento: Optional[str] = None,
    ) -> Optional[
        Union[
            HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
            List[HidreletricaCurvaJusanteAfogamentoExplicitoPadrao],
        ]
    ]:
        """
        Obtém registros que habilitam ou desabilitam a consideração
        do tratamento do afogamento explícito padrão.

        :param considera_afogamento: habilitação do afogamento
        :type considera_afogamento: str | None
        """
        return self.__obtem_registros_com_filtros(
            HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
            considera_afogamento=considera_afogamento,
        )
