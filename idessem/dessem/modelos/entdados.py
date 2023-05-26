from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from typing import Optional, Union


class RD(Register):
    """
    Registro que contém opções de representação da rede elétrica.
    """

    IDENTIFIER = "RD  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(1, 4),
            IntegerField(3, 9),
            IntegerField(1, 14),
            IntegerField(1, 16),
            IntegerField(1, 18),
            IntegerField(1, 20),
            IntegerField(1, 22),
        ]
    )

    @property
    def variaveis_de_folga(self) -> Optional[int]:
        """
        O flag que define a inclusão de variáveis de folga nas restrições
        de rede elétrica.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[0]

    @variaveis_de_folga.setter
    def variaveis_de_folga(self, cod: int):
        self.data[0] = cod

    @property
    def maximo_circuitos_violados(self) -> Optional[int]:
        """
        O número máximo de circuitos que podem ser violados, por
        período.

        :return: O número máximo de circuitos.
        :rtype: int | None
        """
        return self.data[1]

    @maximo_circuitos_violados.setter
    def maximo_circuitos_violados(self, cod: int):
        self.data[1] = cod

    @property
    def carga_registro_dbar(self) -> Optional[int]:
        """
        O flag para executar um caso sem rede elétrica porém
        utilizando a carga declarada nos registros do bloco
        DBAR.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[2]

    @carga_registro_dbar.setter
    def carga_registro_dbar(self, cod: int):
        self.data[2] = cod

    @property
    def limites_circuitos_transformadores_elevadores(self) -> Optional[int]:
        """
        O flag para não considerar os limites de fluxo em
        circuitos transformadores elevadores.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[3]

    @limites_circuitos_transformadores_elevadores.setter
    def limites_circuitos_transformadores_elevadores(self, cod: int):
        self.data[3] = cod

    @property
    def limites_circuitos_e_drefs(self) -> Optional[int]:
        """
        O flag para não considerar restrições de limite de fluxo em circuitos
        e somatórios de fluxo independente dos níveis de tensão
        das barras.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[4]

    @limites_circuitos_e_drefs.setter
    def limites_circuitos_e_drefs(self, cod: int):
        self.data[4] = cod

    @property
    def consideracao_perdas(self) -> Optional[int]:
        """
        O flag para consideração das perdas nos circuitos
        da rede elétrica.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[5]

    @consideracao_perdas.setter
    def consideracao_perdas(self, cod: int):
        self.data[5] = cod

    @property
    def formato_arquivos_rede(self) -> Optional[int]:
        """
        O flag para indicar o tipo de formato dos arquivos
        da rede elétrica.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[6]

    @formato_arquivos_rede.setter
    def formato_arquivos_rede(self, cod: int):
        self.data[6] = cod


class RIVAR(Register):
    """
    Registro que contém configurações para consideração de restrições
    soft de variação para as variáveis do problema.
    """

    IDENTIFIER = "RIVAR  "
    IDENTIFIER_DIGITS = 7
    LINE = Line(
        [
            IntegerField(3, 7),
            IntegerField(3, 12),
            IntegerField(2, 15),
            FloatField(10, 19),
        ]
    )

    @property
    def codigo_entidade(self) -> Optional[int]:
        """
        O código da entidade (hidrelétrica, termelétrica, elevatória,
        intercâmbio).

        :return: O número.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_entidade.setter
    def codigo_entidade(self, cod: int):
        self.data[0] = cod

    @property
    def sistema_para(self) -> Optional[int]:
        """
        O código do sistema "para" no caso de restrição de intercâmbio.

        :return: O código do sistema para.
        :rtype: int | None
        """
        return self.data[1]

    @sistema_para.setter
    def sistema_para(self, cod: int):
        self.data[1] = cod

    @property
    def tipo_variavel(self) -> Optional[int]:
        """
        O código do tipo de variável.

        :return: O tipo de variável.
        :rtype: int | None
        """
        return self.data[2]

    @tipo_variavel.setter
    def tipo_variavel(self, cod: int):
        self.data[2] = cod

    @property
    def penalidade(self) -> Optional[float]:
        """
        A penalidade a ser utilizada nas restrições.

        :return: A penalidade.
        :rtype: float | None
        """
        return self.data[3]

    @penalidade.setter
    def penalidade(self, cod: float):
        self.data[3] = cod


class TM(Register):
    """
    Registro que contém a discretização temporal e representação
    da rede elétrica.
    """

    IDENTIFIER = "TM  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(2, 9),
            IntegerField(1, 14),
            FloatField(5, 19, 1),
            IntegerField(1, 29),
            LiteralField(6, 33),
        ]
    )

    @property
    def dia_inicial(self) -> Optional[int]:
        """
        O dia inicial do período.

        :return: O dia.
        :rtype: int | None
        """
        return self.data[0]

    @dia_inicial.setter
    def dia_inicial(self, cod: int):
        self.data[0] = cod

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial do período.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1]

    @hora_inicial.setter
    def hora_inicial(self, cod: int):
        self.data[1] = cod

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial do período.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, cod: int):
        self.data[2] = cod

    @property
    def duracao(self) -> Optional[float]:
        """
        A duração do período em horas.

        :return: A duração.
        :rtype: float | None
        """
        return self.data[3]

    @duracao.setter
    def duracao(self, cod: float):
        self.data[3] = cod

    @property
    def consideracao_rede_eletrica(self) -> Optional[int]:
        """
        O flag para indicar conisderação da rede elétrica no período.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[4]

    @consideracao_rede_eletrica.setter
    def consideracao_rede_eletrica(self, cod: int):
        self.data[4] = cod

    @property
    def patamar_de_carga(self) -> Optional[str]:
        """
        O nome do patamar de carga.

        :return: O patamar.
        :rtype: str | None
        """
        return self.data[5]

    @patamar_de_carga.setter
    def patamar_de_carga(self, n: str):
        self.data[5] = n


class SIST(Register):
    """
    Registro que contém o cadastro dos submercados.
    """

    IDENTIFIER = "SIST   "
    IDENTIFIER_DIGITS = 7
    LINE = Line(
        [
            IntegerField(2, 7),
            LiteralField(2, 10),
            IntegerField(2, 13),
            LiteralField(10, 16),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro do submercado.

        :return: O código.
        :rtype: int | None]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, cod: int):
        self.data[0] = cod

    @property
    def mnemonico(self) -> Optional[str]:
        """
        O mnemônico de cadastro do submercado.

        :return: O mnemônico.
        :rtype: str | None
        """
        return self.data[1]

    @mnemonico.setter
    def mnemonico(self, n: str):
        self.data[1] = n

    @property
    def ficticio(self) -> Optional[int]:
        """
        O código de cadastro do submercado.

        :return: O código.
        :rtype: int | None]
        """
        return self.data[2]

    @ficticio.setter
    def ficticio(self, cod: int):
        self.data[2] = cod

    @property
    def nome(self) -> Optional[str]:
        """
        O nome de cadastro do submercado.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[3]

    @nome.setter
    def nome(self, n: str):
        self.data[3] = n


class REE(Register):
    """
    Registro que contém o cadastro dos reservatórios equivalentes
    de energia.
    """

    IDENTIFIER = "REE   "
    IDENTIFIER_DIGITS = 6
    LINE = Line(
        [
            IntegerField(2, 6),
            IntegerField(2, 9),
            LiteralField(10, 12),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro do REE.

        :return: O código.
        :rtype: int | None]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, cod: int):
        self.data[0] = cod

    @property
    def submercado(self) -> Optional[int]:
        """
        O código do submercado que pertence o REE.

        :return: O código.
        :rtype: int | None]
        """
        return self.data[1]

    @submercado.setter
    def submercado(self, cod: int):
        self.data[1] = cod

    @property
    def nome(self) -> Optional[str]:
        """
        O nome de cadastro do REE.

        :return: O mnemônico.
        :rtype: str | None
        """
        return self.data[2]

    @nome.setter
    def nome(self, n: str):
        self.data[2] = n


class UH(Register):
    """
    Registro que contém o cadastro das UHEs, com os seus volumes
    iniciais no estudo.
    """

    IDENTIFIER = "UH  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            LiteralField(12, 9),
            IntegerField(2, 24),
            FloatField(10, 29, 2),
            IntegerField(1, 39),
            LiteralField(2, 41),
            IntegerField(2, 44),
            IntegerField(1, 47),
            FloatField(10, 49, 2),
            IntegerField(1, 64),
            IntegerField(1, 69),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro da UHE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, cod: int):
        self.data[0] = cod

    @property
    def nome(self) -> Optional[str]:
        """
        O nome da UHE.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[1]

    @nome.setter
    def nome(self, n: str):
        self.data[1] = n

    @property
    def ree(self) -> Optional[int]:
        """
        O REE de cadastro da UHE.

        :return: O REE.
        :rtype: int | None
        """
        return self.data[2]

    @ree.setter
    def ree(self, n: int):
        self.data[2] = n

    @property
    def volume_inicial(self) -> Optional[float]:
        """
        O volume inicial da UHE para o estudo.

        :return: O volume.
        :rtype: float | None
        """
        return self.data[3]

    @volume_inicial.setter
    def volume_inicial(self, v: float):
        self.data[3] = v

    @property
    def evaporacao(self) -> Optional[int]:
        """
        A consideração ou não de evaporação para a UHE.

        :return: A consideração.
        :rtype: int | None
        """
        return self.data[4]

    @evaporacao.setter
    def evaporacao(self, e: int):
        self.data[4] = e

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial de operação.

        :return: O dia.
        :rtype: str | int | None
        """

        dia = self.data[5]
        if (dia == "I") or (dia is None):
            return dia
        else:
            return int(dia)

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        if isinstance(n, int):
            self.data[5] = str(n)
        else:
            self.data[5] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial de operação.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[6]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[6] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial de operação.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[7]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[7] = n

    @property
    def volume_morto_inicial(self) -> Optional[float]:
        """
        Volume morto inicial da usina.

        :return: O volume em hm3.
        :rtype: float | None
        """
        return self.data[8]

    @volume_morto_inicial.setter
    def volume_morto_inicial(self, e: float):
        self.data[8] = e

    @property
    def produtividade(self) -> Optional[int]:
        """
        O tipo de produtividade considerada.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[9]

    @produtividade.setter
    def produtividade(self, n: int):
        self.data[9] = n

    @property
    def penaliza_restricao_geracao(self) -> Optional[int]:
        """
        O flag que indica penalização de restrições de geração.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[10]

    @penaliza_restricao_geracao.setter
    def penaliza_restricao_geracao(self, n: int):
        self.data[10] = n


# class CT(Register):
#     """
#     Registro que contém o cadastro das usinas termelétricas com
#     os seus custos e capacidades.

#     *OBS: Suporta apenas 3 patamares no momento*
#     """

#     IDENTIFIER = "CT  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             LiteralField(10, 14),
#             IntegerField(2, 24),
#             FloatField(5, 29, 2),
#             FloatField(5, 34, 2),
#             FloatField(10, 39, 2),
#             FloatField(5, 49, 2),
#             FloatField(5, 54, 2),
#             FloatField(10, 59, 2),
#             FloatField(5, 69, 2),
#             FloatField(5, 74, 2),
#             FloatField(10, 79, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código de cadastro da UTE.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, codigo: int):
#         self.data[0] = codigo

#     @property
#     def subsistema(self) -> Optional[int]:
#         """
#         O subsistema de cadastro da UTE.

#         :return: O subsistema.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @subsistema.setter
#     def subsistema(self, subsistema: int):
#         self.data[1] = subsistema

#     @property
#     def nome(self) -> Optional[str]:
#         """
#         O nome de cadastro da UTE.

#         :return: O nome como uma `str`.
#         :rtype: str | None
#         """
#         return self.data[2]

#     @nome.setter
#     def nome(self, nome: str):
#         self.data[2] = nome

#     @property
#     def estagio(self) -> Optional[str]:
#         """
#         O estágio associado às propriedades cadastradas.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[3]

#     @estagio.setter
#     def estagio(self, estagio: int):
#         self.data[3] = estagio

#     @property
#     def inflexibilidades(self) -> Optional[List[float]]:
#         """
#         As inflexibilidades da UTE por patamar.

#         :return: As inflexibilidades.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[4::3] if v is not None]

#     @inflexibilidades.setter
#     def inflexibilidades(self, inflex: List[float]):
#         self.__atualiza_dados_lista(inflex, 4, 3)

#     @property
#     def disponibilidades(self) -> Optional[List[float]]:
#         """
#         As disponibilidades da UTE por patamar.

#         :return: As disponibilidades.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[5::3] if v is not None]

#     @disponibilidades.setter
#     def disponibilidades(self, disp: List[float]):
#         self.__atualiza_dados_lista(disp, 5, 3)

#     @property
#     def cvus(self) -> Optional[List[float]]:
#         """
#         Os CVUs da UTE por patamar.

#         :return: Os CVUs.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[6::3] if v is not None]

#     @cvus.setter
#     def cvus(self, cvu: List[float]):
#         self.__atualiza_dados_lista(cvu, 6, 3)


# class UE(Register):
#     """
#     Registro que contém o cadastro das estações de bombeamento
#     (usinas elevatórias).
#     """

#     IDENTIFIER = "UE  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             LiteralField(12, 14),
#             IntegerField(3, 29),
#             IntegerField(3, 34),
#             FloatField(10, 39, 1),
#             FloatField(10, 49, 1),
#             FloatField(10, 59, 2),
#         ]
#     )

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código de cadastro da UE.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, cod: int):
#         self.data[0] = cod

#     @property
#     def subsistema(self) -> Optional[int]:
#         """
#         O subsistema de cadastro da UE, conforme registro SB.

#         :return: O subsistema.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @subsistema.setter
#     def subsistema(self, n: int):
#         self.data[1] = n

#     @property
#     def nome(self) -> Optional[str]:
#         """
#         O nome da estação de bombeamento.

#         :return: O nome.
#         :rtype: str | None
#         """
#         return self.data[2]

#     @nome.setter
#     def nome(self, v: str):
#         self.data[2] = v

#     @property
#     def uhe_montante(self) -> Optional[int]:
#         """
#         O código da UHE a montante, conforme registro UH.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[3]

#     @uhe_montante.setter
#     def uhe_montante(self, v: int):
#         self.data[3] = v

#     @property
#     def uhe_jusante(self) -> Optional[int]:
#         """
#         O código da UHE a jusante, conforme registro UH.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[4]

#     @uhe_jusante.setter
#     def uhe_jusante(self, e: int):
#         self.data[4] = e

#     @property
#     def vazao_minima_bombeavel(self) -> Optional[float]:
#         """
#         A vazão mínima bombeável.

#         :return: A vazão em m3/s
#         :rtype: float | None
#         """
#         return self.data[5]

#     @vazao_minima_bombeavel.setter
#     def vazao_minima_bombeavel(self, e: float):
#         self.data[5] = e

#     @property
#     def vazao_maxima_bombeavel(self) -> Optional[float]:
#         """
#         A vazão mínima bombeável.

#         :return: A vazão em m3/s
#         :rtype: float | None
#         """
#         return self.data[6]

#     @vazao_maxima_bombeavel.setter
#     def vazao_maxima_bombeavel(self, e: float):
#         self.data[6] = e

#     @property
#     def taxa_consumo(self) -> Optional[float]:
#         """
#         A taxa de consumo.

#         :return: A taxa em MWmed/m3/s.
#         :rtype: float | None
#         """
#         return self.data[7]

#     @taxa_consumo.setter
#     def taxa_consumo(self, e: float):
#         self.data[7] = e


# class DP(Register):
#     """
#     Registro que contém o cadastro das durações dos patamares.

#     *OBS: Suporta apenas 3 patamares no momento*
#     """

#     IDENTIFIER = "DP  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             IntegerField(2, 9),
#             IntegerField(1, 14),
#             FloatField(10, 19, 1),
#             FloatField(10, 29, 1),
#             FloatField(10, 39, 1),
#             FloatField(10, 49, 1),
#             FloatField(10, 59, 1),
#             FloatField(10, 69, 1),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado às durações especificadas.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[0] = e

#     @property
#     def subsistema(self) -> Optional[int]:
#         """
#         O subsistema associado às durações especificadas.

#         :return: O subsistema.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @subsistema.setter
#     def subsistema(self, sub: int):
#         self.data[1] = sub

#     @property
#     def num_patamares(self) -> Optional[int]:
#         """
#         O número de patamares.

#         :return: O número de patamares.
#         :rtype: int | None
#         """
#         return self.data[2]

#     @num_patamares.setter
#     def num_patamares(self, n: int):
#         self.data[2] = n

#     @property
#     def cargas(self) -> Optional[List[float]]:
#         """
#         As cargas em Mwmed pata cada patamar de carga

#         :return: As cargas.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[3::2] if v is not None]

#     @cargas.setter
#     def cargas(self, c: List[float]):
#         self.__atualiza_dados_lista(c, 3, 2)

#     @property
#     def duracoes(self) -> Optional[List[float]]:
#         """
#         As durações de cada patamar de carga em horas

#         :return: As durações em horas.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[4::2] if v is not None]

#     @duracoes.setter
#     def duracoes(self, d: List[float]):
#         self.__atualiza_dados_lista(d, 4, 2)


# class PQ(Register):
#     """
#     Registro que contém o cadastro da geração por pequenas usinas.

#     *OBS: Suporta apenas 3 patamares no momento*
#     """

#     IDENTIFIER = "PQ  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(10, 4),
#             IntegerField(2, 14),
#             IntegerField(2, 19),
#             FloatField(5, 24, 0),
#             FloatField(5, 29, 0),
#             FloatField(5, 34, 0),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def nome(self) -> Optional[str]:
#         """
#         O nome da geração.

#         :return: O nome.
#         :rtype: str | None
#         """
#         return self.data[0]

#     @nome.setter
#     def nome(self, nome: str):
#         self.data[0] = nome

#     @property
#     def subsistema(self) -> Optional[int]:
#         """
#         O subsistema associado à geração.

#         :return: O subsistema.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @subsistema.setter
#     def subsistema(self, sub: int):
#         self.data[1] = sub

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado à geração.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[2]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[2] = e

#     @property
#     def geracoes(self) -> Optional[List[float]]:
#         """
#         As gerações em Mwmed para cada patamar de carga.

#         :return: As gerações.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[3:6] if v is not None]

#     @geracoes.setter
#     def geracoes(self, c: List[float]):
#         self.__atualiza_dados_lista(c, 3, 1)


# class CD(Register):
#     """
#     Registro que contém o cadastro dos custos de déficit.

#     *OBS: Suporta apenas 3 patamares no momento*
#     """

#     IDENTIFIER = "CD  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             IntegerField(2, 9),
#             LiteralField(10, 14),
#             IntegerField(2, 24),
#             FloatField(5, 29, 1),
#             FloatField(10, 34, 2),
#             FloatField(5, 44, 1),
#             FloatField(10, 49, 2),
#             FloatField(5, 59, 1),
#             FloatField(10, 64, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def numero_curva(self) -> Optional[int]:
#         """
#         O número da curva de déficit.

#         :return: O índice da curva.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @numero_curva.setter
#     def numero_curva(self, n: int):
#         self.data[0] = n

#     @property
#     def subsistema(self) -> Optional[int]:
#         """
#         O índice do subsistema associado.

#         :return: O subsistema.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @subsistema.setter
#     def subsistema(self, s: int):
#         self.data[1] = s

#     @property
#     def nome_curva(self) -> Optional[str]:
#         """
#         O nome da curva de défitict

#         :return: O nome.
#         :rtype: str | None
#         """
#         return self.data[2]

#     @nome_curva.setter
#     def nome_curva(self, n: str):
#         self.data[2] = n

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio de vigência do custo de déficit

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[3]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[3] = e

#     @property
#     def limites_superiores(self) -> Optional[List[float]]:
#         """
#         Os limites superiores para consideração dos custos.

#         :return: Os limites.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[4::2] if v is not None]

#     @limites_superiores.setter
#     def limites_superiores(self, lim: List[float]):
#         self.__atualiza_dados_lista(lim, 4, 2)

#     @property
#     def custos(self) -> Optional[List[float]]:
#         """
#         Os custos de déficit.

#         :return: Os custos.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[5::2] if v is not None]

#     @custos.setter
#     def custos(self, cus: List[float]):
#         self.__atualiza_dados_lista(cus, 5, 2)


# class RI(Register):
#     """
#     Registro que contém as restrições de Itaipu.

#     *OBS: Suporta apenas 3 patamares no momento*
#     """

#     IDENTIFIER = "RI  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(3, 8),
#             IntegerField(3, 12),
#             FloatField(7, 16, 0),
#             FloatField(7, 23, 0),
#             FloatField(7, 30, 0),
#             FloatField(7, 37, 0),
#             FloatField(7, 44, 0),
#             FloatField(7, 51, 0),
#             FloatField(7, 58, 0),
#             FloatField(7, 65, 0),
#             FloatField(7, 72, 0),
#             FloatField(7, 79, 0),
#             FloatField(7, 86, 0),
#             FloatField(7, 93, 0),
#             FloatField(7, 100, 0),
#             FloatField(7, 107, 0),
#             FloatField(7, 114, 0),
#         ]
#     )


# class IA(Register):
#     """
#     Registro que contém os limites de intercâmbio entre os subsistemas.

#     *OBS: Suporta apenas 3 patamares no momento*
#     """

#     IDENTIFIER = "IA  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             LiteralField(2, 9),
#             LiteralField(2, 14),
#             IntegerField(1, 17),
#             FloatField(10, 19, 0),
#             FloatField(10, 29, 0),
#             FloatField(10, 39, 0),
#             FloatField(10, 49, 0),
#             FloatField(10, 59, 0),
#             FloatField(10, 69, 0),
#         ]
#     )


# class TX(Register):
#     """
#     Registro que contém a taxa de desconto anual do modelo.
#     """

#     IDENTIFIER = "TX  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             FloatField(5, 4, 0),
#         ]
#     )

#     @property
#     def taxa(self) -> Optional[float]:
#         """
#         A taxa de desconto em % utilizada no estudo.

#         :return: A taxa.
#         :rtype: float | None
#         """
#         return self.data[0]

#     @taxa.setter
#     def taxa(self, t: float):
#         self.data[0] = t


# class GP(Register):
#     """
#     Registro que contém o gap de tolerância para convergência.
#     """

#     IDENTIFIER = "GP  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             FloatField(10, 4, 6),
#         ]
#     )

#     @property
#     def gap(self) -> Optional[float]:
#         """
#         O gap considerado para convergência no estudo

#         :return: O gap.
#         :rtype: float | None
#         """
#         return self.data[0]

#     @gap.setter
#     def gap(self, g: float):
#         self.data[0] = g


# class NI(Register):
#     """
#     Registro que contém o número máximo de iterações do modelo.
#     """

#     IDENTIFIER = "NI  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line([IntegerField(3, 4), IntegerField(1, 8)])

#     @property
#     def iteracoes(self) -> Optional[int]:
#         """
#         O número máximo de iterações do modelo no estudo

#         :return: O número de iterações.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @iteracoes.setter
#     def iteracoes(self, i: int):
#         self.data[0] = i

#     @property
#     def tipo_limite(self) -> Optional[int]:
#         """
#         Se o número de interações fornecido é mínimo ou máximo.

#         :return: O tipo de limite de iterações
#         :rtype: int | None
#         """
#         return self.data[1]

#     @tipo_limite.setter
#     def tipo_limite(self, i: int):
#         self.data[1] = i


# class DT(Register):
#     """
#     Registro que contém a data de referência do estudo.
#     """

#     IDENTIFIER = "DT  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             IntegerField(2, 9),
#             IntegerField(4, 14),
#         ]
#     )

#     @property
#     def dia(self) -> Optional[int]:
#         """
#         O dia de referência para realização do estudo

#         :return: O dia
#         :rtype: int | None
#         """
#         return self.data[0]

#     @dia.setter
#     def dia(self, d: int):
#         self.data[0] = d

#     @property
#     def mes(self) -> Optional[int]:
#         """
#         O mês de referência para realização do estudo

#         :return: O mês
#         :rtype: int | None
#         """
#         return self.data[1]

#     @mes.setter
#     def mes(self, m: int):
#         self.data[1] = m

#     @property
#     def ano(self) -> Optional[int]:
#         """
#         O ano de referência para realização do estudo

#         :return: O ano
#         :rtype: int | None
#         """
#         return self.data[2]

#     @ano.setter
#     def ano(self, a: int):
#         self.data[2] = a


# class MP(Register):
#     """
#     Registro que contém as manutenções programadas das UHEs.

#     *OBS: Suporta apenas 12 estágios no momento*
#     """

#     IDENTIFIER = "MP  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 7),
#             FloatField(5, 9, 3),
#             FloatField(5, 14, 3),
#             FloatField(5, 19, 3),
#             FloatField(5, 24, 3),
#             FloatField(5, 29, 3),
#             FloatField(5, 34, 3),
#             FloatField(5, 39, 3),
#             FloatField(5, 44, 3),
#             FloatField(5, 49, 3),
#             FloatField(5, 54, 3),
#             FloatField(5, 59, 3),
#             FloatField(5, 64, 3),
#             FloatField(5, 69, 3),
#         ]
#     )


# class MT(Register):
#     """
#     Registro que contém as manutenções programadas das UTEs.

#     *OBS: Suporta apenas 12 estágios no momento*
#     """

#     IDENTIFIER = "MT  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             FloatField(5, 14, 3),
#             FloatField(5, 19, 3),
#             FloatField(5, 24, 3),
#             FloatField(5, 29, 3),
#             FloatField(5, 34, 3),
#             FloatField(5, 39, 3),
#             FloatField(5, 44, 3),
#             FloatField(5, 49, 3),
#             FloatField(5, 54, 3),
#             FloatField(5, 59, 3),
#             FloatField(5, 64, 3),
#             FloatField(5, 69, 3),
#             FloatField(5, 74, 3),
#         ]
#     )


# class FD(Register):
#     """
#     Registro que contém as manutenções programadas das UTEs.

#     *OBS: Suporta apenas 12 estágios no momento*
#     """

#     IDENTIFIER = "FD  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 7),
#             FloatField(5, 9, 3),
#             FloatField(5, 14, 3),
#             FloatField(5, 19, 3),
#             FloatField(5, 24, 3),
#             FloatField(5, 29, 3),
#             FloatField(5, 34, 3),
#             FloatField(5, 39, 3),
#             FloatField(5, 44, 3),
#             FloatField(5, 49, 3),
#             FloatField(5, 54, 3),
#             FloatField(5, 59, 3),
#             FloatField(5, 64, 3),
#             FloatField(5, 69, 3),
#         ]
#     )


# class VE(Register):
#     """
#     Registro que contém os volumes de espera das UHEs.

#     *OBS: Suporta apenas 12 estágios no momento*
#     """

#     IDENTIFIER = "VE  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(5, 9, 2),
#             FloatField(5, 14, 2),
#             FloatField(5, 19, 2),
#             FloatField(5, 24, 2),
#             FloatField(5, 29, 2),
#             FloatField(5, 34, 2),
#             FloatField(5, 39, 2),
#             FloatField(5, 44, 2),
#             FloatField(5, 49, 2),
#             FloatField(5, 54, 2),
#             FloatField(5, 59, 2),
#             FloatField(5, 64, 2),
#             FloatField(5, 69, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código do posto associado ao volume.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def volumes(self) -> Optional[List[float]]:
#         """
#         Os volumes de espera por estagio.

#         :return: Os volumes.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[1:] if v is not None]

#     @volumes.setter
#     def volumes(self, cus: List[float]):
#         self.__atualiza_dados_lista(cus, 1, 1)


# class RE(Register):
#     """
#     Registro que contém os cadastros de restrições elétricas.
#     """

#     IDENTIFIER = "RE  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             IntegerField(2, 14),
#         ]
#     )

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código de cadastro para a restrição

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio_inicial(self) -> Optional[int]:
#         """
#         O estágio inicial para consideração da restrição

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @estagio_inicial.setter
#     def estagio_inicial(self, e: int):
#         self.data[1] = e

#     @property
#     def estagio_final(self) -> Optional[int]:
#         """
#         O estágio final para consideração da restrição

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[2]

#     @estagio_final.setter
#     def estagio_final(self, e: int):
#         self.data[2] = e


# class LU(Register):
#     """
#     Registro que contém os cadastros de limites das restrições elétricas.

#     *OBS: Suporta apenas 3 patamares no momento*
#     """

#     IDENTIFIER = "LU  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             FloatField(10, 14, 1),
#             FloatField(10, 24, 1),
#             FloatField(10, 34, 1),
#             FloatField(10, 44, 1),
#             FloatField(10, 54, 1),
#             FloatField(10, 64, 1),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código da restrição RE associada aos limites

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio inicial para consideração dos limites, até
#         que sejam especificados novos limites.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[1] = e

#     @property
#     def limites_inferiores(self) -> Optional[List[float]]:
#         """
#         Os limites inferiores por patamar para a restrição elétrica

#         :return: Os limites
#         :rtype: list[float] | None
#         """
#         return self.data[2::2]

#     @limites_inferiores.setter
#     def limites_inferiores(self, lim: List[float]):
#         self.__atualiza_dados_lista(lim, 2, 2)

#     @property
#     def limites_superiores(self) -> Optional[List[float]]:
#         """
#         Os limites superiores por patamar para a restrição elétrica

#         :return: Os limites
#         :rtype: list[float] | None
#         """
#         return self.data[3::2]

#     @limites_superiores.setter
#     def limites_superiores(self, lim: List[float]):
#         self.__atualiza_dados_lista(lim, 3, 2)


# class FU(Register):
#     """
#     Registro que contém os coeficientes das usinas hidráulicas
#     nas restrições elétricas.
#     """

#     IDENTIFIER = "FU  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             IntegerField(3, 14),
#             FloatField(10, 19, 7),
#             IntegerField(2, 30),
#         ]
#     )

#     @property
#     def restricao(self) -> Optional[int]:
#         """
#         O código da restrição elétrica, segundo registro RE.

#         :return: O código como `int`.
#         """
#         return self.data[0]

#     @restricao.setter
#     def restricao(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado.

#         :return: O estágio como `int`.
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, c: int):
#         self.data[1] = c

#     @property
#     def uhe(self) -> Optional[int]:
#         """
#         O número da UHE conforme registro UH.

#         :return: O número da UHE como `int`.
#         """
#         return self.data[2]

#     @uhe.setter
#     def uhe(self, c: int):
#         self.data[2] = c

#     @property
#     def coeficiente(self) -> Optional[float]:
#         """
#         O coeficiente de participação da usina na restrição.

#         :return: O coeficiente como `float`
#         """
#         return self.data[3]

#     @coeficiente.setter
#     def coeficiente(self, f: float):
#         self.data[3] = f

#     @property
#     def frequencia(self) -> Optional[int]:
#         """
#         A frequência para restrição elétrica, valendo 50 ou 60
#         para Itaipu e 0 para as demais.

#         :return: O número da frequencia como `int`.
#         """
#         return self.data[4]

#     @frequencia.setter
#     def frequencia(self, c: int):
#         self.data[4] = c


# class FT(Register):
#     """
#     Registro que contém os coeficientes das usinas térmicas
#     nas restrições elétricas.
#     """

#     IDENTIFIER = "FT  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             IntegerField(3, 14),
#             IntegerField(2, 19),
#             FloatField(10, 24, 7),
#         ]
#     )

#     @property
#     def restricao(self) -> Optional[int]:
#         """
#         O código da restrição elétrica, segundo registro RE.

#         :return: O código como `int`.
#         """
#         return self.data[0]

#     @restricao.setter
#     def restricao(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado.

#         :return: O estágio como `int`.
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, c: int):
#         self.data[1] = c

#     @property
#     def ute(self) -> Optional[int]:
#         """
#         O número da UTE conforme registro CT.

#         :return: O número da UTE como `int`.
#         """
#         return self.data[2]

#     @ute.setter
#     def ute(self, c: int):
#         self.data[2] = c

#     @property
#     def subsistema(self) -> Optional[int]:
#         """
#         O número do subsistema conforme registros CT ou TG.

#         :return: O número do subsistema como `int`.
#         """
#         return self.data[3]

#     @subsistema.setter
#     def subsistema(self, s: int):
#         self.data[3] = s

#     @property
#     def coeficiente(self) -> Optional[float]:
#         """
#         O coeficiente de participação da usina na restrição.

#         :return: O coeficiente como `float`
#         """
#         return self.data[4]

#     @coeficiente.setter
#     def coeficiente(self, f: float):
#         self.data[4] = f


# class FI(Register):
#     """
#     Registro que contém o sentido do fluxo da interligação
#     entre os subsistemas associados à restrição elétrica.
#     """

#     IDENTIFIER = "FI  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             LiteralField(2, 14),
#             LiteralField(2, 19),
#             FloatField(10, 24, 7),
#         ]
#     )

#     @property
#     def restricao(self) -> Optional[int]:
#         """
#         O código da restrição elétrica, segundo registro RE.

#         :return: O código como `int`.
#         """
#         return self.data[0]

#     @restricao.setter
#     def restricao(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado.

#         :return: O estágio como `int`.
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, c: int):
#         self.data[1] = c

#     @property
#     def de(self) -> Optional[str]:
#         """
#         O subsistema "DE" conforme registros SB.

#         :return: O subsistema como `str`.
#         """
#         return self.data[2]

#     @de.setter
#     def de(self, s: str):
#         self.data[2] = s

#     @property
#     def para(self) -> Optional[str]:
#         """
#         O subsistema "PARA" conforme registros SB.

#         :return: O  subsistema como `str`.
#         """
#         return self.data[3]

#     @para.setter
#     def para(self, s: str):
#         self.data[3] = s

#     @property
#     def coeficiente(self) -> Optional[float]:
#         """
#         O coeficiente de participação da interligação.

#         :return: O coeficiente como `float`
#         """
#         return self.data[4]

#     @coeficiente.setter
#     def coeficiente(self, f: float):
#         self.data[4] = f


# class VI(Register):
#     """
#     Registro que contém os tempos de viagem da água entre usinas.
#     """

#     IDENTIFIER = "VI  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(3, 9),
#             FloatField(5, 14, 0),
#             FloatField(5, 19, 0),
#             FloatField(5, 24, 0),
#             FloatField(5, 29, 0),
#             FloatField(5, 34, 0),
#             FloatField(5, 39, 0),
#             FloatField(5, 44, 0),
#             FloatField(5, 49, 0),
#             FloatField(5, 54, 0),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def uhe(self) -> Optional[int]:
#         """
#         O código da UHE a partir do qual é contabilizado
#         o tempo de viagem.

#         :return: O código
#         :rtype: int | None
#         """
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def duracao(self) -> Optional[int]:
#         """
#         A duração da viagem da água (em horas) entre a UHE do
#         código informado e sua usina à jusante segundo o hidr.

#         :return: A duração
#         :rtype: int | None
#         """
#         return self.data[1]

#     @duracao.setter
#     def duracao(self, d: int):
#         self.data[1] = d

#     @property
#     def vazoes(self) -> Optional[List[float]]:
#         """
#         As vazões defluentes das semanas passadas para a usina
#         do código informado. A posição da vazão na lista indica
#         a qual semana passada se refere [s-1, s-2, s-3, ...].

#         :return: As vazões
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[2::] if v is not None]

#     @vazoes.setter
#     def vazoes(self, v: List[float]):
#         self.__atualiza_dados_lista(v, 2, 1)


# class IR(Register):
#     """
#     Registro que contém as configurações de
#     geração de relatórios de saída.
#     """

#     IDENTIFIER = "IR  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(7, 4),
#             IntegerField(2, 14),
#             IntegerField(2, 19),
#             IntegerField(5, 24),
#         ]
#     )

#     @property
#     def tipo(self) -> Optional[str]:
#         """
#         Mnemônico que contém o tipo de relatório de
#         saída escolhido.

#         :return: O mnemônico.
#         :rtype: str | None
#         """
#         return self.data[0]

#     @tipo.setter
#     def tipo(self, t: str):
#         self.data[0] = t


# class CI(Register):
#     """
#     Registro que define contratos de importação de energia.
#     """

#     IDENTIFIER = "CI  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 8),
#             LiteralField(10, 11),
#             IntegerField(2, 24),
#             FloatField(5, 29, 0),
#             FloatField(5, 34, 0),
#             FloatField(10, 39, 2),
#             FloatField(5, 49, 0),
#             FloatField(5, 54, 0),
#             FloatField(10, 59, 2),
#             FloatField(5, 69, 0),
#             FloatField(5, 74, 0),
#             FloatField(10, 79, 2),
#             FloatField(5, 89, 3),
#         ]
#     )


# class CE(Register):
#     """
#     Registro que define contratos de exportação de energia.
#     """

#     IDENTIFIER = "CE  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 8),
#             LiteralField(10, 11),
#             IntegerField(2, 24),
#             FloatField(5, 29, 0),
#             FloatField(5, 34, 0),
#             FloatField(10, 39, 2),
#             FloatField(5, 49, 0),
#             FloatField(5, 54, 0),
#             FloatField(10, 59, 2),
#             FloatField(5, 69, 0),
#             FloatField(5, 74, 0),
#             FloatField(10, 79, 2),
#             FloatField(5, 89, 3),
#         ]
#     )


# class FC(Register):
#     """
#     Registro que contém informações para acessar a FCF fornecida
#     pelo NEWAVE.
#     """

#     IDENTIFIER = "FC  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(6, 4),
#             LiteralField(200, 14),
#         ]
#     )

#     @property
#     def tipo(self) -> Optional[str]:
#         """
#         O tipo de arquivo da FCF na forma dos mnemônicos
#         aceitos pelo DECOMP.

#         :return: O mnemônico.
#         :rtype: str | None
#         """
#         return self.data[0]

#     @property
#     def caminho(self) -> Optional[str]:
#         """
#         O caminho relativo ou completo para o arquivo da
#         FCF.

#         :return: O caminho.
#         :rtype: str | None
#         """
#         return self.data[1]

#     @caminho.setter
#     def caminho(self, c: str):
#         self.data[1] = c


# class EA(Register):
#     """
#     Registro que a ENA dos meses que antecedem o estudo.
#     """

#     IDENTIFIER = "EA  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             FloatField(10, 11, 2),
#             FloatField(10, 21, 2),
#             FloatField(10, 31, 2),
#             FloatField(10, 41, 2),
#             FloatField(10, 51, 2),
#             FloatField(10, 61, 2),
#             FloatField(10, 71, 2),
#             FloatField(10, 81, 2),
#             FloatField(10, 91, 2),
#             FloatField(10, 101, 2),
#             FloatField(10, 111, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def ree(self) -> Optional[int]:
#         """
#         O índice do REE

#         :return: O índice.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @ree.setter
#     def ree(self, c: int):
#         self.data[0] = c

#     @property
#     def ena(self) -> Optional[List[float]]:
#         """
#         A ENA passada para o REE.

#         :return: O ena.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[1::] if v is not None]

#     @ena.setter
#     def ena(self, c: List[float]):
#         self.__atualiza_dados_lista(c, 1, 1)
#         self.data[1:] = c


# class ES(Register):
#     """
#     Registro que define a ENA das semanas que antecedem o estudo.
#     """

#     IDENTIFIER = "ES  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             IntegerField(1, 9),
#             FloatField(10, 14, 2),
#             FloatField(10, 24, 2),
#             FloatField(10, 34, 2),
#             FloatField(10, 44, 2),
#             FloatField(10, 54, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def ree(self) -> Optional[int]:
#         """
#         O índice do REE

#         :return: O índice.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @ree.setter
#     def ree(self, c: int):
#         self.data[0] = c

#     @property
#     def numero_semanas(self) -> Optional[int]:
#         """
#         O número de semanas do mês anterior

#         :return: O número de semanas.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @numero_semanas.setter
#     def numero_semanas(self, c: int):
#         self.data[1] = c

#     @property
#     def ena(self) -> Optional[List[float]]:
#         """
#         A ENA passada para o REE.

#         :return: O ena.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[2::] if v is not None]

#     @ena.setter
#     def ena(self, c: List[float]):
#         self.__atualiza_dados_lista(c, 1, 1)
#         self.data[2:] = c


# class QI(Register):
#     """
#     Registro que define o tempo de viagem para o cálculo da ENA.
#     """

#     IDENTIFIER = "QI  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(5, 9, 1),
#             FloatField(5, 14, 1),
#             FloatField(5, 19, 1),
#             FloatField(5, 24, 1),
#             FloatField(5, 29, 1),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def uhe(self) -> Optional[int]:
#         """
#         O índice da UHE

#         :return: O índice.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, c: int):
#         self.data[0] = c

#     @property
#     def vazoes(self) -> Optional[List[float]]:
#         """
#         As vazões incrementais cálculo da ENA.

#         :return: As incrementais para cálculo do tempo de viagem.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[1::] if v is not None]

#     @vazoes.setter
#     def vazoes(self, c: List[float]):
#         self.__atualiza_dados_lista(c, 1, 1)
#         self.data[1:] = c


# class RT(Register):
#     """
#     Registro utilizado para retirada de restrições de soleira de
#     vertedouro e de canais de desvio.
#     """

#     IDENTIFIER = "RT  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(6, 4),
#         ]
#     )

#     @property
#     def restricao(self) -> Optional[str]:
#         """
#         O mnemônico da restrição removida.

#         :return: O mnemônico
#         :rtype: str | None
#         """
#         return self.data[0]

#     @restricao.setter
#     def restricao(self, m: str):
#         self.data[0] = m


# class TI(Register):
#     """
#     Registro que contém as taxas de irrigação por UHE.
#     """

#     IDENTIFIER = "TI  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(5, 9, 2),
#             FloatField(5, 14, 2),
#             FloatField(5, 19, 2),
#             FloatField(5, 24, 2),
#             FloatField(5, 29, 2),
#             FloatField(5, 34, 2),
#             FloatField(5, 39, 2),
#             FloatField(5, 44, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código da UHE associada às taxas de irrigação

#         :return: O código como `int`.
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def taxas(self) -> Optional[List[float]]:
#         """
#         As taxas de irrigação por estágio do estudo. A
#         posição da taxa na lista indica a qual estágio
#         ela está associada [e1, e2, e3, ...].

#         :return: As taxas.
#         :type: list[float] | None
#         """
#         return [v for v in self.data[1::] if v is not None]

#     @taxas.setter
#     def taxas(self, tx: List[float]):
#         self.__atualiza_dados_lista(tx, 1, 1)


# class FP(Register):
#     """
#     Registro que contém os cadastros de restrições de alteração na
#     função de produção das usinas.
#     """

#     IDENTIFIER = "FP  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(3, 9),
#             IntegerField(1, 14),
#             IntegerField(4, 16),
#             FloatField(5, 21, 0),
#             FloatField(5, 27, 0),
#             IntegerField(1, 34),
#             IntegerField(4, 36),
#             FloatField(5, 41, 0),
#             FloatField(5, 47, 0),
#             FloatField(5, 54, 0),
#             FloatField(5, 60, 0),
#             FloatField(5, 66, 0),
#         ]
#     )

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código da UHE associada à restrição FP.

#         :return: O código
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado à restrição FP.

#         :return: O estágio
#         :rtype: int | None
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[1] = e

#     @property
#     def tipo_entrada_janela_turbinamento(self) -> Optional[int]:
#         """
#         O tipo de entrada da janela de turbinamento fornecido
#         na restrição FP. 0 para limites em percentual da vazão turbinada
#         máxima das usinas, 1 para limites em m3/s.

#         :return: O tipo de entrada
#         :rtype: int | None
#         """
#         return self.data[2]

#     @tipo_entrada_janela_turbinamento.setter
#     def tipo_entrada_janela_turbinamento(self, t: int):
#         self.data[2] = t

#     @property
#     def numero_pontos_turbinamento(self) -> Optional[int]:
#         """
#         O número de pontos para discretização da janela de
#         turbinamento. Máximo permitido de 1000 pontos.

#         :return: O número de pontos
#         :rtype: int | None
#         """
#         return self.data[3]

#     @numero_pontos_turbinamento.setter
#     def numero_pontos_turbinamento(self, n: int):
#         self.data[3] = n

#     @property
#     def limite_inferior_janela_turbinamento(self) -> Optional[float]:
#         """
#         O limite inferior da janela de turbinamento.

#         :return: O limite.
#         :rtype: float | None
#         """
#         return self.data[4]

#     @limite_inferior_janela_turbinamento.setter
#     def limite_inferior_janela_turbinamento(self, lim: float):
#         self.data[4] = lim

#     @property
#     def limite_superior_janela_turbinamento(self) -> Optional[float]:
#         """
#         O limite superior da janela de turbinamento.

#         :return: O limite.
#         :rtype: float | None
#         """
#         return self.data[5]

#     @limite_superior_janela_turbinamento.setter
#     def limite_superior_janela_turbinamento(self, lim: float):
#         self.data[5] = lim

#     @property
#     def tipo_entrada_janela_volume(self) -> Optional[int]:
#         """
#         O tipo de entrada da janela de volume fornecido
#         na restrição FP. 0 para limites em percentual do volume útil
#         das usinas, 1 para limites em hm3.

#         :return: O tipo de entrada.
#         :rtype: int | None
#         """
#         return self.data[6]

#     @tipo_entrada_janela_volume.setter
#     def tipo_entrada_janela_volume(self, t: int):
#         self.data[6] = t

#     @property
#     def numero_pontos_volume(self) -> Optional[int]:
#         """
#         O número de pontos para discretização da janela de
#         volume. Máximo permitido de 1000 pontos.

#         :return: O número de pontos.
#         :rtype: int | None
#         """
#         return self.data[7]

#     @numero_pontos_volume.setter
#     def numero_pontos_volume(self, n: int):
#         self.data[7] = n

#     @property
#     def limite_inferior_janela_volume(self) -> Optional[float]:
#         """
#         A redução aplicada ao volume útil da usina, para ser utilizado
#         como limite inferior da janela de volume.

#         :return: O limite.
#         :rtype: float | None
#         """
#         return self.data[8]

#     @limite_inferior_janela_volume.setter
#     def limite_inferior_janela_volume(self, lim: float):
#         self.data[8] = lim

#     @property
#     def limite_superior_janela_volume(self) -> Optional[float]:
#         """
#         O acréscimo aplicado ao volume útil da usina, para ser utilizado
#         como limite superior da janela de volume.

#         :return: O limite.
#         :rtype: float | None
#         """
#         return self.data[9]

#     @limite_superior_janela_volume.setter
#     def limite_superior_janela_volume(self, lim: float):
#         self.data[9] = lim


# class RQ(Register):
#     """
#     Registro que contém os percentuais de vazão defluente
#     mínima histórica para cada REE.
#     """

#     IDENTIFIER = "RQ  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             FloatField(5, 9, 2),
#             FloatField(5, 14, 2),
#             FloatField(5, 19, 2),
#             FloatField(5, 24, 2),
#             FloatField(5, 29, 2),
#             FloatField(5, 34, 2),
#             FloatField(5, 39, 2),
#             FloatField(5, 44, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def ree(self) -> Optional[int]:
#         """
#         O código do REE associado às vazões mínimas.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @ree.setter
#     def ree(self, r: int):
#         self.data[0] = r

#     @property
#     def vazoes(self) -> Optional[List[float]]:
#         """
#         As vazões defluentes mínimas (percentuais)
#         para o REE, por estágio [e1, e2, e3, ...].

#         :return: As vazoes.
#         :rtype: list[float] | None
#         """
#         return [v for v in self.data[1:] if v is not None]

#     @vazoes.setter
#     def vazoes(self, v: List[float]):
#         self.__atualiza_dados_lista(v, 1, 1)
#         self.data[1:] = v


# class EZ(Register):
#     """
#     Registro que contém o percentual máximo do
#     volume útil para acoplamento.
#     """

#     IDENTIFIER = "EZ  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(5, 9, 2),
#         ]
#     )

#     @property
#     def uhe(self) -> Optional[int]:
#         """
#         Código da UHE associada, conforme registro UH.

#         :return: O código da UHE.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def volume(self) -> Optional[float]:
#         """
#         O volume útil considerado para cálculo.

#         :return: O volume útil em % do volume máximo.
#         :rtype: float | None
#         """
#         return self.data[1]

#     @volume.setter
#     def volume(self, u: float):
#         self.data[1] = u


# class HV(Register):
#     """
#     Registro que contém os cadastros de restrições de volume armazenado.
#     """

#     IDENTIFIER = "HV  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             IntegerField(2, 14),
#         ]
#     )

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código da UHE associada à restrição HV.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio_inicial(self) -> Optional[int]:
#         """
#         O estágio inicial de consideração da restrição HV.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @estagio_inicial.setter
#     def estagio_inicial(self, e: int):
#         self.data[1] = e

#     @property
#     def estagio_final(self) -> Optional[int]:
#         """
#         O estágio final de consideração da restrição HV.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[2]

#     @estagio_final.setter
#     def estagio_final(self, e: int):
#         self.data[2] = e


# class LV(Register):
#     """
#     Registro que contém os cadastros dos limites das
#     restrições de volume armazenado.
#     """

#     IDENTIFIER = "LV  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             FloatField(10, 14, 2),
#             FloatField(10, 24, 2),
#         ]
#     )

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código da restrição HV associada aos limites

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio de consideração dos limites.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[1] = e

#     @property
#     def limite_inferior(self) -> Optional[float]:
#         """
#         O limite inferior para o armazenamento.

#         :return: O limite.
#         :rtype: float | None
#         """
#         return self.data[2]

#     @limite_inferior.setter
#     def limite_inferior(self, lim: float):
#         self.data[2] = lim

#     @property
#     def limite_superior(self) -> Optional[float]:
#         """
#         O limite superior para o armazenamento.

#         :return: O limite.
#         :rtype: float | None
#         """
#         return self.data[3]

#     @limite_superior.setter
#     def limite_superior(self, lim: float):
#         self.data[3] = lim


# class CV(Register):
#     """
#     Registro que contém os coeficientes das usinas hidráulicas
#     nas restrições de volume armazenado.
#     """

#     IDENTIFIER = "CV  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             IntegerField(3, 14),
#             FloatField(10, 19, 7),
#             LiteralField(4, 34),
#         ]
#     )

#     @property
#     def restricao(self) -> Optional[int]:
#         """
#         O código da restrição de volume, segundo registro HV.

#         :return: O código como `int`.
#         """
#         return self.data[0]

#     @restricao.setter
#     def restricao(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado.

#         :return: O estágio como `int`.
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, c: int):
#         self.data[1] = c

#     @property
#     def uhe(self) -> Optional[int]:
#         """
#         O número da UHE ou estação de bombeamento conforme registros UH ou UE.

#         :return: O número da UHE como `int`.
#         """
#         return self.data[2]

#     @uhe.setter
#     def uhe(self, c: int):
#         self.data[2] = c

#     @property
#     def coeficiente(self) -> Optional[float]:
#         """
#         O coeficiente da variável na restrição.

#         :return: O coeficiente como `float`
#         """
#         return self.data[3]

#     @coeficiente.setter
#     def coeficiente(self, f: float):
#         self.data[3] = f

#     @property
#     def tipo(self) -> Optional[str]:
#         """
#         O mnemônico de tipo da restrição.

#         :return: O tipo como `str`.
#         """
#         return self.data[4]

#     @tipo.setter
#     def tipo(self, t: str):
#         self.data[4] = t


# class HQ(Register):
#     """
#     Registro que contém os cadastros de restrições de vazões.
#     """

#     IDENTIFIER = "HQ  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             IntegerField(2, 14),
#         ]
#     )

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código da UHE associada à restrição HQ.

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio_inicial(self) -> Optional[int]:
#         """
#         O estágio inicial de consideração da restrição HQ.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @estagio_inicial.setter
#     def estagio_inicial(self, e: int):
#         self.data[1] = e

#     @property
#     def estagio_final(self) -> Optional[int]:
#         """
#         O estágio final de consideração da restrição HQ.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[2]

#     @estagio_final.setter
#     def estagio_final(self, e: int):
#         self.data[2] = e


# class LQ(Register):
#     """
#     Registro que contém os cadastros dos limites das
#     restrições de vazão.
#     """

#     IDENTIFIER = "LQ  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             FloatField(10, 14, 2),
#             FloatField(10, 24, 2),
#             FloatField(10, 34, 2),
#             FloatField(10, 44, 2),
#             FloatField(10, 54, 2),
#             FloatField(10, 64, 2),
#         ]
#     )

#     def __atualiza_dados_lista(
#         self,
#         novos_dados: list,
#         indice_inicial: int,
#         espacamento: int,
#     ):
#         atuais = len(self.data)
#         ultimo_indice = indice_inicial + espacamento * len(novos_dados)
#         diferenca = (ultimo_indice - atuais) // espacamento
#         if diferenca > 0:
#             self.data += [None] * (ultimo_indice - atuais)
#             diferenca -= 1
#         novos_dados += [None] * abs(diferenca)
#         self.data[indice_inicial::espacamento] = novos_dados

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código da restrição HQ associada aos limites

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio de consideração dos limites.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[1] = e

#     @property
#     def limites_inferiores(self) -> Optional[List[float]]:
#         """
#         Os limites inferiores por patamar para a vazão.

#         :return: Os limites.
#         :rtype: list[float] | None
#         """
#         return self.data[2::2]

#     @limites_inferiores.setter
#     def limites_inferiores(self, lim: List[float]):
#         self.__atualiza_dados_lista(lim, 2, 2)

#     @property
#     def limites_superiores(self) -> Optional[List[float]]:
#         """
#         Os limites superiores por patamar para a vazão.

#         :return: Os limites.
#         :rtype: list[float] | None
#         """
#         return self.data[3::2]

#     @limites_superiores.setter
#     def limites_superiores(self, lim: List[float]):
#         self.__atualiza_dados_lista(lim, 3, 2)


# class CQ(Register):
#     """
#     Registro que contém os coeficientes das usinas hidráulicas
#     nas restrições de vazão.
#     """

#     IDENTIFIER = "CQ  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(2, 9),
#             IntegerField(3, 14),
#             FloatField(10, 19, 7),
#             LiteralField(4, 34),
#         ]
#     )

#     @property
#     def restricao(self) -> Optional[int]:
#         """
#         O código da restrição de vazão, segundo registro HQ.

#         :return: O código como `int`.
#         """
#         return self.data[0]

#     @restricao.setter
#     def restricao(self, c: int):
#         self.data[0] = c

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio associado.

#         :return: O estágio como `int`.
#         """
#         return self.data[1]

#     @estagio.setter
#     def estagio(self, c: int):
#         self.data[1] = c

#     @property
#     def uhe(self) -> Optional[int]:
#         """
#         O número da UHE conforme registro UH.

#         :return: O número da UHE como `int`.
#         """
#         return self.data[2]

#     @uhe.setter
#     def uhe(self, c: int):
#         self.data[2] = c

#     @property
#     def coeficiente(self) -> Optional[float]:
#         """
#         O coeficiente da variável na restrição.

#         :return: O coeficiente como `float`
#         """
#         return self.data[3]

#     @coeficiente.setter
#     def coeficiente(self, f: float):
#         self.data[3] = f

#     @property
#     def tipo(self) -> Optional[str]:
#         """
#         O mnemônico de tipo da restrição.

#         :return: O tipo como `str`.
#         """
#         return self.data[4]

#     @tipo.setter
#     def tipo(self, t: str):
#         self.data[4] = t


# class AR(Register):
#     """
#     Registro que contém as configurações de aversão a risco.
#     """

#     IDENTIFIER = "AR  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [IntegerField(3, 5), FloatField(5, 11, 0), FloatField(5, 17, 0)]
#     )

#     @property
#     def periodo(self) -> Optional[int]:
#         """
#         O período inicial de aplicação do CVaR.

#         :return: O índice do período inicial.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @periodo.setter
#     def periodo(self, p: int):
#         self.data[0] = p

#     @property
#     def lamb(self) -> Optional[float]:
#         """
#         O valor de lambda utilizado no CVaR.

#         :return: O valor de lambda
#         :rtype: float | None
#         """
#         return self.data[1]

#     @lamb.setter
#     def lamb(self, v: float):
#         self.data[1] = v

#     @property
#     def alfa(self) -> Optional[float]:
#         """
#         O valor de alfa utilizado no CVaR.

#         :return: O valor de alfa
#         :rtype: float | None
#         """
#         return self.data[2]

#     @alfa.setter
#     def alfa(self, v: float):
#         self.data[2] = v


# class EV(Register):
#     """
#     Registro que contém as configurações de consideração
#     da evaporação.
#     """

#     IDENTIFIER = "EV  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(1, 4),
#             LiteralField(3, 9),
#         ]
#     )

#     @property
#     def modelo(self) -> Optional[int]:
#         """
#         O modelo de evaporação considerado

#         :return: O modelo.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @modelo.setter
#     def modelo(self, m: int):
#         self.data[0] = m

#     @property
#     def volume_referencia(self) -> Optional[str]:
#         """
#         O mnemônico para o volume considerado

#         :return: O mnemônico.
#         :rtype: str | None
#         """
#         return self.data[1]

#     @volume_referencia.setter
#     def volume_referencia(self, v: str):
#         self.data[1] = v


# class FJ(Register):
#     """
#     Registro que contém o arquivo de polinômios de jusante.
#     """

#     IDENTIFIER = "FJ  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(12, 4),
#         ]
#     )

#     @property
#     def arquivo(self) -> str:
#         """
#         O nome do arquivo.

#         :return: O nome
#         :rtype: str | None
#         """
#         return self.data[0]

#     @arquivo.setter
#     def arquivo(self, a: str):
#         self.data[0] = a


# class HE(Register):
#     """
#     Registro que contém o cadastro de uma restrição de energia
#     armazenada.
#     """

#     IDENTIFIER = "HE  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(1, 9),
#             FloatField(10, 14, 2),
#             IntegerField(2, 25),
#             FloatField(10, 28, 2),
#             IntegerField(1, 39),
#             IntegerField(1, 41),
#             IntegerField(1, 43),
#             LiteralField(12, 45),
#         ]
#     )

#     @property
#     def codigo(self) -> Optional[int]:
#         """
#         O código de cadastro da restrição HE

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def tipo_limite(self) -> Optional[int]:
#         """
#         O tipo de limite especificado na restrição HE,
#         em valor absoluto ou percentual.

#         :return: O tipo.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @tipo_limite.setter
#     def tipo_limite(self, t: int):
#         self.data[1] = t

#     @property
#     def limite(self) -> Optional[float]:
#         """
#         O limite para a energia armazenada associada
#         ao registro HE.

#         :return: O limite.
#         :rtype: float | None
#         """
#         return self.data[2]

#     @limite.setter
#     def limite(self, lim: float):
#         self.data[2] = lim

#     @property
#     def estagio(self) -> Optional[int]:
#         """
#         O estágio para consideração da restrição.

#         :return: O estágio.
#         :rtype: int | None
#         """
#         return self.data[3]

#     @estagio.setter
#     def estagio(self, e: int):
#         self.data[3] = e

#     @property
#     def penalidade(self) -> Optional[float]:
#         """
#         O valor da penalidade para a violação da restrição.

#         :return: O valor.
#         :rtype: float | None
#         """
#         return self.data[4]

#     @penalidade.setter
#     def penalidade(self, p: float):
#         self.data[4] = p

#     @property
#     def forma_calculo_produtibilidades(self) -> Optional[int]:
#         """
#         Flag para indicar a forma de cálculo das produtividades
#         das usinas usadas nas restrição.

#         :return: A flag.
#         :rtype: int | None
#         """
#         return self.data[5]

#     @forma_calculo_produtibilidades.setter
#     def forma_calculo_produtibilidades(self, t: int):
#         self.data[5] = t

#     @property
#     def tipo_valores_produtibilidades(self) -> Optional[int]:
#         """
#         Flag para indicar o tipo dos valores das produtividades
#         das usinas usadas nas restrição.

#         :return: O tipo.
#         :rtype: int | None
#         """
#         return self.data[6]

#     @tipo_valores_produtibilidades.setter
#     def tipo_valores_produtibilidades(self, t: int):
#         self.data[6] = t

#     @property
#     def tipo_penalidade(self) -> Optional[int]:
#         """
#         O tipo de penalidade a ser considerada ao violar a
#         restrição (inviabilidade ou penalização).

#         :return: O tipo.
#         :rtype: int | None
#         """
#         return self.data[7]

#     @tipo_penalidade.setter
#     def tipo_penalidade(self, t: int):
#         self.data[7] = t

#     @property
#     def arquivo_produtibilidades(self) -> Optional[str]:
#         """
#         O arquivo com as definições das produtibilidades usadas
#         para o cálculo da restrição RHE.

#         :return: O arquivo externo com as produbitibilidades.
#         :rtype: str | None
#         """
#         return self.data[8]

#     @arquivo_produtibilidades.setter
#     def arquivo_produtibilidades(self, t: str):
#         self.data[8] = t


# class CM(Register):
#     """
#     Registro que contém os coeficientes de uma restrição RHE.
#     """

#     IDENTIFIER = "CM  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [IntegerField(3, 4), IntegerField(3, 9), FloatField(10, 14, 2)]
#     )

#     @property
#     def codigo(self) -> int:
#         """
#         O código de cadastro da restrição CM

#         :return: O código.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo.setter
#     def codigo(self, c: int):
#         self.data[0] = c

#     @property
#     def ree(self) -> int:
#         """
#         O REE do coeficiente

#         :return: O REE.
#         :rtype: int | None
#         """
#         return self.data[1]

#     @ree.setter
#     def ree(self, e: int):
#         self.data[1] = e

#     @property
#     def coeficiente(self) -> float:
#         """
#         O coeficiente de energia considerado

#         :return: O coeficiente.
#         :rtype: float | None
#         """
#         return self.data[2]

#     @coeficiente.setter
#     def coeficiente(self, c: float):
#         self.data[2] = c


# class PD(Register):
#     """
#     Registro que contém a escolha do algoritmo para
#     resolução do PL.
#     """

#     IDENTIFIER = "PD  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(6, 4),
#         ]
#     )

#     @property
#     def algoritmo(self) -> Optional[str]:
#         """
#         O algoritmo considerado.

#         :return: O identificador do algoritmo.
#         :rtype: str | None
#         """
#         return self.data[0]

#     @algoritmo.setter
#     def algoritmo(self, m: str):
#         self.data[0] = m


# class PU(Register):
#     """
#     Registro que habilita a solução do problema
#     via PL único.
#     """

#     IDENTIFIER = "PU  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(1, 4),
#         ]
#     )

#     @property
#     def pl(self) -> Optional[int]:
#         """
#         O tipo de pl considerado.

#         :return: O identificador do pl.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @pl.setter
#     def pl(self, m: int):
#         self.data[0] = m


# class RC(Register):
#     """
#     Registro que inclui restrições do tipo escada.
#     """

#     IDENTIFIER = "RC  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(6, 4),
#         ]
#     )

#     @property
#     def mnemonico(self) -> Optional[str]:
#         """
#         O tipo de mnemonico considerado.

#         :return: O identificador do mnemonico.
#         :rtype: str | None
#         """
#         return self.data[0]

#     @mnemonico.setter
#     def mnemonico(self, m: str):
#         self.data[0] = m


# class PE(Register):
#     """
#     Registro que altera as penalidades de vertimento,
#     intercâmbio e desvios.
#     """

#     IDENTIFIER = "PE  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(2, 4),
#             IntegerField(1, 7),
#             FloatField(10, 9, 6),
#         ]
#     )

#     @property
#     def subsistema(self) -> Optional[int]:
#         """
#         O índice do subsistema considerado

#         :return: O índice do subsistema.
#         :rtype: int | None
#         """
#         return self.data[0]

#     @subsistema.setter
#     def subsistema(self, m: int):
#         self.data[0] = m

#     @property
#     def tipo(self) -> Optional[int]:
#         """
#         O tipo de penalidade a ser modificado

#         :return: O indice do tipo de penalidade
#         :rtype: int | None
#         """
#         return self.data[1]

#     @tipo.setter
#     def tipo(self, m: int):
#         self.data[1] = m

#     @property
#     def penalidade(self) -> Optional[float]:
#         """
#         O novo valor de penalidade

#         :return: O valor da penalidade
#         :rtype: float | None
#         """
#         return self.data[2]

#     @penalidade.setter
#     def penalidade(self, m: float):
#         self.data[2] = m


# class TS(Register):
#     """
#     Registro que altera as tolerâncias do solver.
#     """

#     IDENTIFIER = "TS  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             FloatField(17, 4, 15),
#             FloatField(17, 22, 15),
#             IntegerField(1, 42),
#             FloatField(17, 22, 15),
#         ]
#     )

#     @property
#     def tolerancia_primaria(self) -> Optional[float]:
#         """
#         A nova tolerância primária do solver.

#         :return: A tolerância
#         :rtype: float | None
#         """
#         return self.data[0]

#     @tolerancia_primaria.setter
#     def tolerancia_primaria(self, m: float):
#         self.data[0] = m

#     @property
#     def tolerancia_secundaria(self) -> Optional[float]:
#         """
#         A nova tolerância secundária do solver.

#         :return: A tolerância
#         :rtype: float | None
#         """
#         return self.data[1]

#     @tolerancia_secundaria.setter
#     def tolerancia_secundaria(self, m: float):
#         self.data[1] = m

#     @property
#     def zera_coeficientes(self) -> Optional[int]:
#         """
#         Habilita ou não a funcionalidade de zerar coeficientes
#         em casos de cortes não ótimos.

#         :return: O valor do flag
#         :rtype: int | None
#         """
#         return self.data[2]

#     @zera_coeficientes.setter
#     def zera_coeficientes(self, m: int):
#         self.data[2] = m

#     @property
#     def tolerancia_teste_otimalidade(self) -> Optional[float]:
#         """
#         A nova tolerância usada no teste de otimalidade da
#         solução do PL.

#         :return: A tolerância
#         :rtype: float | None
#         """
#         return self.data[3]

#     @tolerancia_teste_otimalidade.setter
#     def tolerancia_teste_otimalidade(self, m: float):
#         self.data[3] = m


# class PV(Register):
#     """
#     Registro que altera as penalidades das variáveis de folga
#     do problema e as tolerâncias para a viabilidade das restrições.
#     """

#     IDENTIFIER = "PV  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             FloatField(20, 5, 5),
#             FloatField(20, 28, 5),
#             IntegerField(3, 51),
#             FloatField(3, 57, 1),
#             FloatField(20, 63, 5),
#             FloatField(20, 86, 5),
#         ]
#     )

#     @property
#     def penalidade_variaveis_folga(self) -> Optional[float]:
#         """
#         A nova penalidade para as variáveis de folga (R$/MWh).

#         :return: A tolerância
#         :rtype: float | None
#         """
#         return self.data[0]

#     @penalidade_variaveis_folga.setter
#     def penalidade_variaveis_folga(self, m: float):
#         self.data[0] = m

#     @property
#     def tolerancia_viabilidade_restricoes(self) -> Optional[float]:
#         """
#         A nova tolerância para a viabilidade das restrições.

#         :return: A tolerância
#         :rtype: float | None
#         """
#         return self.data[1]

#     @tolerancia_viabilidade_restricoes.setter
#     def tolerancia_viabilidade_restricoes(self, m: float):
#         self.data[1] = m

#     @property
#     def iteracoes_atualizacao_penalidade(self) -> Optional[int]:
#         """
#         O número de iterações para atualização da penalidade variável
#         iterativa para as folgas.

#         :return: O número de iterações
#         :rtype: int | None
#         """
#         return self.data[2]

#     @iteracoes_atualizacao_penalidade.setter
#     def iteracoes_atualizacao_penalidade(self, m: int):
#         self.data[2] = m

#     @property
#     def fator_multiplicacao_folga(self) -> Optional[float]:
#         """
#         O fator para multiplicação da folga ao longo das restrições.

#         :return: A tolerância
#         :rtype: float | None
#         """
#         return self.data[3]

#     @fator_multiplicacao_folga.setter
#     def fator_multiplicacao_folga(self, m: float):
#         self.data[3] = m

#     @property
#     def valor_inicial_variaveis_folga(self) -> Optional[float]:
#         """
#         O valor inicial ou mínimo para as variáveis de folga.

#         :return: O valor mínimo
#         :rtype: float | None
#         """
#         return self.data[4]

#     @valor_inicial_variaveis_folga.setter
#     def valor_inicial_variaveis_folga(self, m: float):
#         self.data[4] = m

#     @property
#     def valor_final_variaveis_folga(self) -> Optional[float]:
#         """
#         O valor final ou máximo para as variáveis de folga.

#         :return: O valor máximo
#         :rtype: float | None
#         """
#         return self.data[5]

#     @valor_final_variaveis_folga.setter
#     def valor_final_variaveis_folga(self, m: float):
#         self.data[5] = m


# class CX(Register):
#     """
#     Registro que mapeia o acoplamento de usinas que representam
#     complexos no NEWAVE com o DECOMP.
#     """

#     IDENTIFIER = "CX  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(4, 4),
#             IntegerField(4, 9),
#         ]
#     )

#     @property
#     def codigo_newave(self) -> Optional[int]:
#         """
#         O código da usina no NEWAVE

#         :return: O código
#         :rtype: int | None
#         """
#         return self.data[0]

#     @codigo_newave.setter
#     def codigo_newave(self, m: int):
#         self.data[0] = m

#     @property
#     def codigo_decomp(self) -> Optional[int]:
#         """
#         O código da usina no DECOMP

#         :return: O código
#         :rtype: int | None
#         """
#         return self.data[1]

#     @codigo_decomp.setter
#     def codigo_decomp(self, m: int):
#         self.data[1] = m


# class FA(Register):
#     """
#     Registro que indica o nome do arquivo índice CSV.
#     """

#     IDENTIFIER = "FA  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(50, 4),
#         ]
#     )

#     @property
#     def arquivo(self) -> Optional[str]:
#         """
#         O nome do arquivo índice CSV.

#         :return: O nome do arquivo
#         :rtype: str | None
#         """
#         return self.data[0]

#     @arquivo.setter
#     def arquivo(self, m: str):
#         self.data[0] = m


# class VT(Register):
#     """
#     Registro que indica o nome do arquivo com cenários de vento.
#     """

#     IDENTIFIER = "VT  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             LiteralField(50, 4),
#         ]
#     )

#     @property
#     def arquivo(self) -> Optional[str]:
#         """
#         O nome do arquivo com cenários de vento.

#         :return: O nome do arquivo
#         :rtype: str | None
#         """
#         return self.data[0]

#     @arquivo.setter
#     def arquivo(self, m: str):
#         self.data[0] = m


# class CS(Register):
#     """
#     Registro que habilita a consistência de dados.
#     """

#     IDENTIFIER = "CS  "
#     IDENTIFIER_DIGITS = 4
#     LINE = Line(
#         [
#             IntegerField(1, 4),
#         ]
#     )

#     @property
#     def consistencia(self) -> Optional[int]:
#         """
#         Habilita ou não a consistência de dados.

#         :return: O nvalor do flag
#         :rtype: int | None
#         """
#         return self.data[0]

#     @consistencia.setter
#     def consistencia(self, m: int):
#         self.data[0] = m


# class ACNUMPOS(Register):
#     """
#     Registro AC específico para alteração no número do posto.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  NUMPOS"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def posto(self) -> Optional[int]:
#         return self.data[1]

#     @posto.setter
#     def posto(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACNUMJUS(Register):
#     """
#     Registro AC específico para alteração na usina de jusante.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  NUMJUS"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def jusante(self) -> Optional[int]:
#         return self.data[1]

#     @jusante.setter
#     def jusante(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACDESVIO(Register):
#     """
#     Registro AC específico para alteração na usina de jusante
#     para canal de desvio e limite da vazão no canal.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  DESVIO"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             FloatField(10, 24, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def jusante(self) -> Optional[int]:
#         return self.data[1]

#     @jusante.setter
#     def jusante(self, u: int):
#         self.data[1] = u

#     @property
#     def limite_vazao(self) -> Optional[float]:
#         return self.data[2]

#     @limite_vazao.setter
#     def limite_vazao(self, u: float):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACVOLMIN(Register):
#     """
#     Registro AC específico para alteração de volume mínimo.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMIN"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(10, 19, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def volume(self) -> Optional[float]:
#         return self.data[1]

#     @volume.setter
#     def volume(self, u: float):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACVOLMAX(Register):
#     """
#     Registro AC específico para alteração de volume máximo.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMAX"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(10, 19, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def volume(self) -> Optional[float]:
#         return self.data[1]

#     @volume.setter
#     def volume(self, u: float):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACCOTVOL(Register):
#     """
#     Registro AC específico para alteração de um coeficiente do
#     polinômio cota-volume.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  COTVOL"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             FloatField(15, 24, 3),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def ordem(self) -> Optional[int]:
#         return self.data[1]

#     @ordem.setter
#     def ordem(self, u: int):
#         self.data[1] = u

#     @property
#     def coeficiente(self) -> Optional[float]:
#         return self.data[2]

#     @coeficiente.setter
#     def coeficiente(self, u: float):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACCOTARE(Register):
#     """
#     Registro AC específico para alteração de um coeficiente do
#     polinômio cota-área.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  COTARE"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             FloatField(15, 24, 3),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def ordem(self) -> Optional[int]:
#         return self.data[1]

#     @ordem.setter
#     def ordem(self, u: int):
#         self.data[1] = u

#     @property
#     def coeficiente(self) -> Optional[float]:
#         return self.data[2]

#     @coeficiente.setter
#     def coeficiente(self, u: float):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACPROESP(Register):
#     """
#     Registro AC específico para alteração do coeficiente de perdas
#     hidráulicas em função da queda bruta (%,m,k).
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  PROESP"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(10, 19, 3),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def produtibilidade(self) -> Optional[float]:
#         return self.data[1]

#     @produtibilidade.setter
#     def produtibilidade(self, u: float):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACPERHID(Register):
#     """
#     Registro AC específico para alteração do coeficiente de perdas
#     hidráulicas em função da queda bruta (%,m,k).
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  PERHID"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(10, 19, 3),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def coeficiente(self) -> Optional[float]:
#         return self.data[1]

#     @coeficiente.setter
#     def coeficiente(self, u: float):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACNCHAVE(Register):
#     """
#     Registro AC específico para alteração do número da curva-chave
#     (cota-vazão) e nível de jusante da faixa associada (m).
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  NCHAVE"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             FloatField(10, 24, 3),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def numero_curva(self) -> Optional[int]:
#         return self.data[1]

#     @numero_curva.setter
#     def numero_curva(self, u: int):
#         self.data[1] = u

#     @property
#     def nivel(self) -> Optional[float]:
#         return self.data[2]

#     @nivel.setter
#     def nivel(self, u: float):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACCOTVAZ(Register):
#     """
#     Registro AC específico para alteração de um coeficiente do
#     polinômio cota-vazão.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  COTVAZ"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             IntegerField(5, 24),
#             FloatField(15, 29, 3),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def polimonio(self) -> Optional[int]:
#         return self.data[1]

#     @polimonio.setter
#     def polimonio(self, u: int):
#         self.data[1] = u

#     @property
#     def ordem(self) -> Optional[int]:
#         return self.data[2]

#     @ordem.setter
#     def ordem(self, u: int):
#         self.data[2] = u

#     @property
#     def coeficiente(self) -> Optional[float]:
#         return self.data[3]

#     @coeficiente.setter
#     def coeficiente(self, u: float):
#         self.data[3] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACCOFEVA(Register):
#     """
#     Registro AC específico para alteração do coeficiente de evaporação
#     mensal para cada mês.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  COFEVA"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             IntegerField(5, 24),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def mes_coeficiente(self) -> Optional[int]:
#         return self.data[1]

#     @mes_coeficiente.setter
#     def mes_coeficiente(self, u: int):
#         self.data[1] = u

#     @property
#     def coeficiente(self) -> Optional[int]:
#         return self.data[2]

#     @coeficiente.setter
#     def coeficiente(self, u: int):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACNUMCON(Register):
#     """
#     Registro AC específico para alteração no número de conjuntos
#     de máquinas.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  NUMCON"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def conjunto(self) -> Optional[int]:
#         return self.data[1]

#     @conjunto.setter
#     def conjunto(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACNUMMAQ(Register):
#     """
#     Registro AC específico para alteração do número de máquinas
#     em cada conjunto de máquinas.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  NUMMAQ"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             IntegerField(5, 24),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def conjunto(self) -> Optional[int]:
#         return self.data[1]

#     @conjunto.setter
#     def conjunto(self, u: int):
#         self.data[1] = u

#     @property
#     def maquinas(self) -> Optional[int]:
#         return self.data[2]

#     @maquinas.setter
#     def maquinas(self, u: int):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACPOTEFE(Register):
#     """
#     Registro AC específico para alteração da potência efetiva
#     por unidade geradora em um conjunto de máquinas.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  POTEFE"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             FloatField(10, 24, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def conjunto(self) -> Optional[int]:
#         return self.data[1]

#     @conjunto.setter
#     def conjunto(self, u: int):
#         self.data[1] = u

#     @property
#     def potencia(self) -> Optional[float]:
#         return self.data[2]

#     @potencia.setter
#     def potencia(self, u: float):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACALTEFE(Register):
#     """
#     Registro AC específico para alteração da altura efetiva
#     de queda para um conjunto de máquinas.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  ALTEFE"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             FloatField(10, 24, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACVAZEFE(Register):
#     """
#     Registro AC específico para alteração da vazão efetiva
#     para um conjunto de máquinas.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  VAZEFE"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             IntegerField(5, 24),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def conjunto(self) -> Optional[int]:
#         return self.data[1]

#     @conjunto.setter
#     def conjunto(self, u: int):
#         self.data[1] = u

#     @property
#     def vazao(self) -> Optional[int]:
#         return self.data[2]

#     @vazao.setter
#     def vazao(self, u: int):
#         self.data[2] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACJUSMED(Register):
#     """
#     Registro AC específico para alteração da cota média do canal
#     de fuga em metros.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  JUSMED"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(10, 19, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def cota(self) -> Optional[float]:
#         return self.data[1]

#     @cota.setter
#     def cota(self, u: float):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACVERTJU(Register):
#     """
#     Registro AC específico para consideração da influência do vertimento
#     no canal de fuga.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  VERTJU"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def influi(self) -> Optional[int]:
#         return self.data[1]

#     @influi.setter
#     def influi(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACVAZMIN(Register):
#     """
#     Registro AC específico para alteração da vazão mínima.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  VAZMIN"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def vazao(self) -> Optional[int]:
#         return self.data[1]

#     @vazao.setter
#     def vazao(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACTIPERH(Register):
#     """
#     Registro AC específico para alteração do tipo de perdas hidráulicas.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  TIPERH"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def tipo_perda(self) -> Optional[int]:
#         return self.data[1]

#     @tipo_perda.setter
#     def tipo_perda(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACJUSENA(Register):
#     """
#     Registro AC específico para alteração do índice de
#     aproveitamento de jusante para cálculo das energias
#     armazenada e afluente.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  JUSENA"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def aproveitamento(self) -> Optional[int]:
#         return self.data[1]

#     @aproveitamento.setter
#     def aproveitamento(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACVSVERT(Register):
#     """
#     Registro AC específico para alteração do volume mínimo para operação
#     do vertedor.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  VSVERT"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(10, 19, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def volume(self) -> Optional[float]:
#         return self.data[1]

#     @volume.setter
#     def volume(self, u: float):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACVMDESV(Register):
#     """
#     Registro AC específico para alteração do volume mínimo para operação
#     do canal de desvio.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  VMDESV"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             FloatField(10, 19, 2),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def volume(self) -> Optional[float]:
#         return self.data[1]

#     @volume.setter
#     def volume(self, u: float):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m


# class ACNPOSNW(Register):
#     """
#     Registro AC específico para alteração do posto de acoplamento
#     com o NEWAVE.
#     """

#     IDENTIFIER = r"AC  ([\d ]{1,3})  NPOSNW"
#     IDENTIFIER_DIGITS = 15
#     LINE = Line(
#         [
#             IntegerField(3, 4),
#             IntegerField(5, 19),
#             LiteralField(3, 69),
#             IntegerField(2, 73),
#             IntegerField(4, 76),
#         ]
#     )

#     # Override
#     def write(self, file: IO, storage: str = "") -> bool:
#         line = self.__class__.LINE.write(self.data)
#         line = (
#             self.__class__.IDENTIFIER[:2]  # type: ignore
#             + line[2:9]
#             + self.__class__.IDENTIFIER[18:]
#             + line[15:]
#         )
#         file.write(line)
#         return True

#     @property
#     def uhe(self) -> Optional[int]:
#         return self.data[0]

#     @uhe.setter
#     def uhe(self, u: int):
#         self.data[0] = u

#     @property
#     def posto(self) -> Optional[int]:
#         return self.data[1]

#     @posto.setter
#     def posto(self, u: int):
#         self.data[1] = u

#     @property
#     def mes(self) -> Optional[str]:
#         return self.data[-3]

#     @mes.setter
#     def mes(self, m: str):
#         self.data[-3] = m

#     @property
#     def semana(self) -> Optional[int]:
#         return self.data[-2]

#     @semana.setter
#     def semana(self, s: int):
#         self.data[-2] = s

#     @property
#     def ano(self) -> Optional[int]:
#         return self.data[-1]

#     @ano.setter
#     def ano(self, m: int):
#         self.data[-1] = m
