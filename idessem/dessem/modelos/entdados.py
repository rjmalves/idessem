from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from idessem.dessem.modelos.componentes.stagedatefield import StageDateField
from typing import Optional, Union, IO


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
            StageDateField(starting_position=41, special_day_character="I"),
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
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[5][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[5][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[5][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[5][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[5][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[5][2] = n

    @property
    def volume_morto_inicial(self) -> Optional[float]:
        """
        Volume morto inicial da usina.

        :return: O volume em hm3.
        :rtype: float | None
        """
        return self.data[6]

    @volume_morto_inicial.setter
    def volume_morto_inicial(self, e: float):
        self.data[6] = e

    @property
    def produtividade(self) -> Optional[int]:
        """
        O tipo de produtividade considerada.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[7]

    @produtividade.setter
    def produtividade(self, n: int):
        self.data[7] = n

    @property
    def penaliza_restricao_geracao(self) -> Optional[int]:
        """
        O flag que indica penalização de restrições de geração.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[8]

    @penaliza_restricao_geracao.setter
    def penaliza_restricao_geracao(self, n: int):
        self.data[8] = n


class TVIAG(Register):
    """
    Registro que contém os tempos de viagem da água entre usinas.
    """

    IDENTIFIER = "TVIAG "
    IDENTIFIER_DIGITS = 6
    LINE = Line(
        [
            IntegerField(3, 6),
            IntegerField(3, 10),
            LiteralField(1, 14),
            IntegerField(3, 19),
            IntegerField(1, 24),
        ]
    )

    @property
    def uhe_montante(self) -> Optional[int]:
        """
        O código da UHE a montante a partir do qual é contabilizado
        o tempo de viagem.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @uhe_montante.setter
    def uhe_montante(self, u: int):
        self.data[0] = u

    @property
    def elemento_jusante(self) -> Optional[int]:
        """
        O código do elemento a jusante do qual é contabilizado
        o tempo de viagem.

        :return: O código
        :rtype: int | None
        """
        return self.data[1]

    @elemento_jusante.setter
    def elemento_jusante(self, u: int):
        self.data[1] = u

    @property
    def tipo_elemento_jusante(self) -> Optional[str]:
        """
        O tipo de elemento de jusante (S=seção de rio, H=usina).

        :return: O código
        :rtype: str | None
        """
        return self.data[2]

    @tipo_elemento_jusante.setter
    def tipo_elemento_jusante(self, u: str):
        self.data[2] = u

    @property
    def duracao(self) -> Optional[int]:
        """
        A duração da viagem da água (em horas) entre a UHE a montante e
        o elemento à jusante.

        :return: A duração
        :rtype: int | None
        """
        return self.data[3]

    @duracao.setter
    def duracao(self, d: int):
        self.data[3] = d

    @property
    def tipo_tempo_viagem(self) -> Optional[int]:
        """
        O código referente ao tipo de tempo de viagem considerado
        (1=translação; 2=propagação).

        :return: O código do tipo.
        :rtype: int | None
        """
        return self.data[4]

    @tipo_tempo_viagem.setter
    def tipo_tempo_viagem(self, d: int):
        self.data[4] = d


class UT(Register):
    """
    Registro que contém as usinas termelétricas e suas restrições
    de geração.

    """

    IDENTIFIER = "UT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            LiteralField(12, 9),
            IntegerField(2, 22),
            IntegerField(1, 25),
            StageDateField(starting_position=27, special_day_character="I"),
            StageDateField(starting_position=35, special_day_character="F"),
            IntegerField(1, 46),
            FloatField(10, 47, 3),
            FloatField(10, 57, 3),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro da UTE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, codigo: int):
        self.data[0] = codigo

    @property
    def nome(self) -> Optional[str]:
        """
        O nome de cadastro da UTE.

        :return: O nome como uma `str`.
        :rtype: str | None
        """
        return self.data[1]

    @nome.setter
    def nome(self, nome: str):
        self.data[1] = nome

    @property
    def submercado(self) -> Optional[int]:
        """
        O submercado de cadastro da UTE.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[2]

    @submercado.setter
    def submercado(self, submercado: int):
        self.data[2] = submercado

    @property
    def tipo_restricao(self) -> Optional[int]:
        """
        O flag para indicar tipo de restrição.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[3]

    @tipo_restricao.setter
    def tipo_restricao(self, tipo_restricao: int):
        self.data[3] = tipo_restricao

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[4][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[4][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[4][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[4][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[4][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[4][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[5][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[5][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[5][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[5][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[5][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[5][2] = n

    @property
    def unidade_restricao(self) -> Optional[int]:
        """
        O flag para indicar a unidade da restrição de rampa.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[6]

    @unidade_restricao.setter
    def unidade_restricao(self, unidade_restricao: int):
        self.data[6] = unidade_restricao

    @property
    def geracao_minima(self) -> Optional[float]:
        """
        O valor do limite de geracao minima
        (caso restrição de rampa, é o valor da variação
        máxima para decréscimo de geração).

        :return: O valor.
        :rtype: float | None
        """
        return self.data[7]

    @geracao_minima.setter
    def geracao_minima(self, geracao_minima: float):
        self.data[7] = geracao_minima

    @property
    def geracao_maxima(self) -> Optional[float]:
        """
        O valor do limite de geracao máxima
        (caso restrição de rampa, é o valor da variação
        máxima para acréscimo de geração).

        :return: O valor.
        :rtype: float | None
        """
        return self.data[8]

    @geracao_maxima.setter
    def geracao_maxima(self, geracao_maxima: float):
        self.data[8] = geracao_maxima


class USIE(Register):
    """
    Registro que contém o cadastro das usinas elevatórias.
    """

    IDENTIFIER = "USIE "
    IDENTIFIER_DIGITS = 5
    LINE = Line(
        [
            IntegerField(3, 5),
            IntegerField(2, 9),
            LiteralField(12, 14),
            IntegerField(3, 29),
            IntegerField(3, 34),
            FloatField(10, 39, 3),
            FloatField(10, 49, 3),
            FloatField(10, 59, 3),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro da UE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, cod: int):
        self.data[0] = cod

    @property
    def submercado(self) -> Optional[int]:
        """
        O submercado de cadastro da UE.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[1]

    @submercado.setter
    def submercado(self, n: int):
        self.data[1] = n

    @property
    def nome(self) -> Optional[str]:
        """
        O nome da usina elevatória.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[2]

    @nome.setter
    def nome(self, v: str):
        self.data[2] = v

    @property
    def uhe_montante(self) -> Optional[int]:
        """
        O código da UHE a montante, conforme registro UH.

        :return: O código.
        :rtype: int | None
        """
        return self.data[3]

    @uhe_montante.setter
    def uhe_montante(self, v: int):
        self.data[3] = v

    @property
    def uhe_jusante(self) -> Optional[int]:
        """
        O código da UHE a jusante, conforme registro UH.

        :return: O código.
        :rtype: int | None
        """
        return self.data[4]

    @uhe_jusante.setter
    def uhe_jusante(self, e: int):
        self.data[4] = e

    @property
    def vazao_minima_bombeavel(self) -> Optional[float]:
        """
        A vazão mínima bombeável.

        :return: A vazão em m3/s
        :rtype: float | None
        """
        return self.data[5]

    @vazao_minima_bombeavel.setter
    def vazao_minima_bombeavel(self, e: float):
        self.data[5] = e

    @property
    def vazao_maxima_bombeavel(self) -> Optional[float]:
        """
        A vazão mínima bombeável.

        :return: A vazão em m3/s
        :rtype: float | None
        """
        return self.data[6]

    @vazao_maxima_bombeavel.setter
    def vazao_maxima_bombeavel(self, e: float):
        self.data[6] = e

    @property
    def taxa_consumo(self) -> Optional[float]:
        """
        A taxa de consumo.

        :return: A taxa em MWmed/m3/s.
        :rtype: float | None
        """
        return self.data[7]

    @taxa_consumo.setter
    def taxa_consumo(self, e: float):
        self.data[7] = e


class DP(Register):
    """
    Registro que as demandas para os submercados que serão consideradas
    para os períodos em que não se considerada a rede elétrica.

    """

    IDENTIFIER = "DP  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            FloatField(10, 24, 1),
        ]
    )

    @property
    def submercado(self) -> Optional[int]:
        """
        O submercado associado à demanada especificada.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[0]

    @submercado.setter
    def submercado(self, sub: int):
        self.data[0] = sub

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def demanda(self) -> Optional[float]:
        """
        A demanda em Mwmed para o período especificado

        :return: A demanda.
        :rtype: float | None
        """
        return self.data[3]

    @demanda.setter
    def demanda(self, demanda: float):
        self.data[3] = demanda


class DE(Register):
    """
    Registro que as demandas especiais para serem representadas em
    restrições elétricas do tipo RE.

    """

    IDENTIFIER = "DE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            FloatField(10, 24, 1),
            LiteralField(10, 35),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código da demanda especial.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, sub: int):
        self.data[0] = sub

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """
        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """
        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def demanda(self) -> Optional[float]:
        """
        A demanda em Mwmed para o período especificado

        :return: A demanda.
        :rtype: float | None
        """
        return self.data[3]

    @demanda.setter
    def demanda(self, demanda: float):
        self.data[3] = demanda

    @property
    def justificativa(self) -> Optional[str]:
        """
        A descrição ou justificativa.

        :return: A justificativa.
        :rtype: str | None
        """
        return self.data[4]

    @justificativa.setter
    def justificativa(self, justificativa: str):
        self.data[4] = justificativa


class CD(Register):
    """
    Registro que contém o cadastro dos custos de déficit.

    """

    IDENTIFIER = "CD "
    IDENTIFIER_DIGITS = 3
    LINE = Line(
        [
            IntegerField(2, 3),
            IntegerField(2, 6),
            StageDateField(starting_position=9, special_day_character="I"),
            StageDateField(starting_position=17, special_day_character="F"),
            FloatField(10, 25, 2),
            FloatField(10, 35, 2),
        ]
    )

    @property
    def submercado(self) -> Optional[int]:
        """
        O índice do submercado associado.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[0]

    @submercado.setter
    def submercado(self, s: int):
        self.data[0] = s

    @property
    def numero_curva(self) -> Optional[int]:
        """
        O número da curva de déficit.

        :return: O índice da curva.
        :rtype: int | None
        """
        return self.data[1]

    @numero_curva.setter
    def numero_curva(self, n: int):
        self.data[1] = n

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[2][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[3][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[3][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[3][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[3][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[3][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[3][2] = n

    @property
    def custo(self) -> Optional[float]:
        """
        O custo de déficit.

        :return: O custo.
        :rtype: float | None
        """
        return self.data[4]

    @custo.setter
    def custo(self, cus: float):
        self.data[4] = cus

    @property
    def limite_superior(self) -> Optional[float]:
        """
        O limite superior para consideração dos custos.

        :return: O limite.
        :rtype: float | None
        """
        return self.data[5]

    @limite_superior.setter
    def limite_superior(self, lim: float):
        self.data[5] = lim


class PQ(Register):
    """
    Registro que contém o cadastro da geração por pequenas usinas.

    """

    IDENTIFIER = "PQ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            LiteralField(10, 9),
            IntegerField(5, 19),
            StageDateField(starting_position=24, special_day_character="I"),
            StageDateField(starting_position=32, special_day_character="F"),
            FloatField(10, 40, 1),
        ]
    )

    @property
    def codigo(self) -> Optional[str]:
        """
        O código da pequena usina.

        :return: O código.
        :rtype: str | None
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, nome: str):
        self.data[0] = nome

    @property
    def nome(self) -> Optional[str]:
        """
        O nome da pequena usina.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[1]

    @nome.setter
    def nome(self, nome: str):
        self.data[1] = nome

    @property
    def localizacao(self) -> Optional[int]:
        """
        O indice do subsistema  ou barra associado à geração.

        :return: O índice da localização.
        :rtype: int | None
        """
        return self.data[2]

    @localizacao.setter
    def localizacao(self, sub: int):
        self.data[2] = sub

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[3][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[3][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[3][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[3][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[3][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[3][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[4][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[4][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[4][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[4][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[4][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[4][2] = n

    @property
    def geracao(self) -> Optional[float]:
        """
        A geração da pequena usina.

        :return: A geração.
        :rtype: float | None
        """
        return self.data[5]

    @geracao.setter
    def geracao(self, ger: float):
        self.data[5] = ger


class IT(Register):
    """
    Registro que contém os coeficientes do polinômio do canal de fuga
    de Itaipu em função da vazão na Régua 11, para casos sem FPHA Libs.
    """

    IDENTIFIER = "IT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            FloatField(15, 9, 7, format="E"),
            FloatField(15, 24, 7, format="E"),
            FloatField(15, 39, 7, format="E"),
            FloatField(15, 54, 7, format="E"),
            FloatField(15, 69, 7, format="E"),
        ]
    )

    @property
    def ree(self) -> Optional[int]:
        """
        O código do REE em que se encontra a usina
        de Itaipu.

        :return: O ree.
        :rtype: int | None
        """

        return self.data[0]

    @ree.setter
    def ree(self, n: int):
        self.data[0] = n

    @property
    def coeficiente_a0(self) -> Optional[float]:
        """
        O coeficiente de grau 0 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[1]

    @coeficiente_a0.setter
    def coeficiente_a0(self, c: float):
        self.data[1] = c

    @property
    def coeficiente_a1(self) -> Optional[float]:
        """
        O coeficiente de grau 1 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[2]

    @coeficiente_a1.setter
    def coeficiente_a1(self, c: float):
        self.data[2] = c

    @property
    def coeficiente_a2(self) -> Optional[float]:
        """
        O coeficiente de grau 2 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[3]

    @coeficiente_a2.setter
    def coeficiente_a2(self, c: float):
        self.data[3] = c

    @property
    def coeficiente_a3(self) -> Optional[float]:
        """
        O coeficiente de grau 3 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[4]

    @coeficiente_a3.setter
    def coeficiente_a3(self, c: float):
        self.data[4] = c

    @property
    def coeficiente_a4(self) -> Optional[float]:
        """
        O coeficiente de grau 4 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[5]

    @coeficiente_a4.setter
    def coeficiente_a4(self, c: float):
        self.data[5] = c


class RI(Register):
    """
    Registro que contém as restrições de Itaipu.

    """

    IDENTIFIER = "RI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            FloatField(10, 26, 2),
            FloatField(10, 36, 2),
            FloatField(10, 46, 2),
            FloatField(10, 56, 2),
            FloatField(10, 66, 2),
        ]
    )

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[0][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[0][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[0][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[0][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[0][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[0][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[1][2] = n

    @property
    def geracao_minima_50hz(self) -> Optional[float]:
        """
        O limite inferior para a geração 50 Hz de Itaipu.

        :return: O limite.
        :rtype: float | None
        """
        return self.data[2]

    @geracao_minima_50hz.setter
    def geracao_minima_50hz(self, n: float):
        self.data[2] = n

    @property
    def geracao_maxima_50hz(self) -> Optional[float]:
        """
        O limite superior para a geração 50 Hz de Itaipu.

        :return: O limite.
        :rtype: float | None
        """
        return self.data[3]

    @geracao_maxima_50hz.setter
    def geracao_maxima_50hz(self, n: float):
        self.data[3] = n

    @property
    def geracao_minima_60hz(self) -> Optional[float]:
        """
        O limite inferior para a geração 60 Hz de Itaipu.

        :return: O limite.
        :rtype: float | None
        """
        return self.data[4]

    @geracao_minima_60hz.setter
    def geracao_minima_60hz(self, n: float):
        self.data[4] = n

    @property
    def geracao_maxima_60hz(self) -> Optional[float]:
        """
        O limite superior para a geração 60 Hz de Itaipu.

        :return: O limite.
        :rtype: float | None
        """
        return self.data[5]

    @geracao_maxima_60hz.setter
    def geracao_maxima_60hz(self, n: float):
        self.data[5] = n

    @property
    def carga_ande(self) -> Optional[float]:
        """
        A carga da ANDE.

        :return: A carga.
        :rtype: float | None
        """
        return self.data[6]

    @carga_ande.setter
    def carga_ande(self, n: float):
        self.data[6] = n


class IA(Register):
    """
    Registro que contém os limites de intercâmbio entre os subsistemas.

    """

    IDENTIFIER = "IA  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(2, 4),
            LiteralField(2, 9),
            StageDateField(starting_position=13, special_day_character="I"),
            StageDateField(starting_position=21, special_day_character="F"),
            FloatField(10, 29, 1),
            FloatField(10, 39, 1),
        ]
    )

    @property
    def submercado_de(self) -> Optional[str]:
        """
        O submercado de origem (de).

        :return: O submercado.
        :rtype: str | None
        """

        return self.data[0]

    @submercado_de.setter
    def submercado_de(self, n: str):
        self.data[0] = n

    @property
    def submercado_para(self) -> Optional[str]:
        """
        O submercado de destino (para).

        :return: O submercado.
        :rtype: str | None
        """

        return self.data[1]

    @submercado_para.setter
    def submercado_para(self, n: str):
        self.data[1] = n

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[2][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[3][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[3][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[3][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[3][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[3][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[3][2] = n

    @property
    def capacidade_de(self) -> Optional[float]:
        """
        A capacidade do intercâmbio do submercado de ao submercado para.

        :return: A capacidade.
        :rtype: float | None
        """
        return self.data[4]

    @capacidade_de.setter
    def capacidade_de(self, n: float):
        self.data[4] = n

    @property
    def capacidade_para(self) -> Optional[float]:
        """
        A capacidade do intercâmbio do submercado para ao submercado de.

        :return: A capacidade.
        :rtype: float | None
        """
        return self.data[5]

    @capacidade_para.setter
    def capacidade_para(self, n: float):
        self.data[5] = n


class GP(Register):
    """
    Registro que contém os gaps de tolerância para convergência
    para os métodos PDD ou MILP.
    """

    IDENTIFIER = "GP  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([FloatField(10, 4, 8), FloatField(10, 15, 8)])

    @property
    def gap_pdd(self) -> Optional[float]:
        """
        O gap de convergência do processo iterativo de
        programação dinâmica dual (PDD).

        :return: O gap.
        :rtype: float | None
        """

        return self.data[0]

    @gap_pdd.setter
    def gap_pdd(self, n: float):
        self.data[0] = n

    @property
    def gap_milp(self) -> Optional[float]:
        """
        O gap de convergência do problema por programação
        linear inteira mista (MILP).

        :return: O gap.
        :rtype: float | None
        """

        return self.data[1]

    @gap_milp.setter
    def gap_milp(self, n: float):
        self.data[1] = n


class ACVTFUGA(Register):
    """
    Registro AC específico para consideração da influência do vertimento
    no canal de fuga.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VTFUGA"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def influi(self) -> Optional[int]:
        return self.data[1]

    @influi.setter
    def influi(self, u: int):
        self.data[1] = u


class ACVOLMAX(Register):
    """
    Registro AC específico para alteração de volume máximo.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMAX"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 3),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u


class ACVOLMIN(Register):
    """
    Registro AC específico para alteração de volume mínimo.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMIN"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 3),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u


class ACVSVERT(Register):
    """
    Registro AC específico para alteração do volume mínimo para operação
    do vertedor.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VSVERT"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 3),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u


class ACVMDESV(Register):
    """
    Registro AC específico para alteração do volume mínimo para operação
    do canal de desvio.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VMDESV"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 3),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u


class ACCOTVAZ(Register):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-vazão.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COTVAZ"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(15, 24, 8, format="E"),
            IntegerField(5, 39),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def ordem(self) -> Optional[int]:
        return self.data[1]

    @ordem.setter
    def ordem(self, u: int):
        self.data[1] = u

    @property
    def coeficiente(self) -> Optional[float]:
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, u: float):
        self.data[2] = u

    @property
    def polimonio(self) -> Optional[int]:
        return self.data[3]

    @polimonio.setter
    def polimonio(self, u: int):
        self.data[3] = u


class ACCOTVOL(Register):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-volume.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COTVOL"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(15, 24, 8, format="E"),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def ordem(self) -> Optional[int]:
        return self.data[1]

    @ordem.setter
    def ordem(self, u: int):
        self.data[1] = u

    @property
    def coeficiente(self) -> Optional[float]:
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, u: float):
        self.data[2] = u


class ACCOTTAR(Register):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-área.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COTTAR"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(15, 24, 8, format="E"),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def ordem(self) -> Optional[int]:
        return self.data[1]

    @ordem.setter
    def ordem(self, u: int):
        self.data[1] = u

    @property
    def coeficiente(self) -> Optional[float]:
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, u: float):
        self.data[2] = u


class ACNUMCON(Register):
    """
    Registro AC específico para número de conjuntos de máquinas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMCON"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def numero_conjuntos(self) -> Optional[int]:
        return self.data[1]

    @numero_conjuntos.setter
    def numero_conjuntos(self, u: int):
        self.data[1] = u


class ACNUMJUS(Register):
    """
    Registro AC específico para número da usina de jusante
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMJUS"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def jusante(self) -> Optional[int]:
        return self.data[1]

    @jusante.setter
    def jusante(self, u: int):
        self.data[1] = u


class ACNUMPOS(Register):
    """
    Registro AC específico para número do posto de vazão.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMPOS"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def posto(self) -> Optional[int]:
        return self.data[1]

    @posto.setter
    def posto(self, u: int):
        self.data[1] = u


class ACJUSENA(Register):
    """
    Registro AC específico para número da usina de jusante para
    cálculo das energias armazenadas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  JUSENA"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def aproveitamento(self) -> Optional[int]:
        return self.data[1]

    @aproveitamento.setter
    def aproveitamento(self, u: int):
        self.data[1] = u


class ACJUSMED(Register):
    """
    Registro AC específico para cota média do canal de fuga.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  JUSMED"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 3),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def cota(self) -> Optional[float]:
        return self.data[1]

    @cota.setter
    def cota(self, u: float):
        self.data[1] = u


class ACCOFEVA(Register):
    """
    Registro AC específico para alteração de mês e coeficiente
    de evaporação mensal.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COFEVA"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            IntegerField(5, 24),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes_coeficiente(self) -> Optional[int]:
        return self.data[1]

    @mes_coeficiente.setter
    def mes_coeficiente(self, u: int):
        self.data[1] = u

    @property
    def coeficiente(self) -> Optional[int]:
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, u: int):
        self.data[2] = u


class ACNUMMAQ(Register):
    """
    Registro AC específico para alteração do número de máquinas
    de um conjunto.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMMAQ"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            IntegerField(5, 24),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def conjunto(self) -> Optional[int]:
        return self.data[1]

    @conjunto.setter
    def conjunto(self, u: int):
        self.data[1] = u

    @property
    def maquinas(self) -> Optional[int]:
        return self.data[2]

    @maquinas.setter
    def maquinas(self, u: int):
        self.data[2] = u


class ACPOTEFE(Register):
    """
    Registro AC específico para alteração da potência efetiva
    das máquinas de um conjunto.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  POTEFE"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 2),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def conjunto(self) -> Optional[int]:
        return self.data[1]

    @conjunto.setter
    def conjunto(self, u: int):
        self.data[1] = u

    @property
    def potencia(self) -> Optional[float]:
        return self.data[2]

    @potencia.setter
    def potencia(self, u: float):
        self.data[2] = u


class ACDESVIO(Register):
    """
    Registro AC específico para número da usina de jusante para desvio
    e limite de desvio.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  DESVIO"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 2),
        ]
    )

    # Override
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def jusante(self) -> Optional[int]:
        return self.data[1]

    @jusante.setter
    def jusante(self, u: int):
        self.data[1] = u

    @property
    def limite_vazao(self) -> Optional[float]:
        return self.data[2]

    @limite_vazao.setter
    def limite_vazao(self, u: float):
        self.data[2] = u


class NI(Register):
    """
    Registro com o número máximo ou fixo de iterações caso
    se aplique a técnica de PDD para resolver o problema.
    """

    IDENTIFIER = "NI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([IntegerField(1, 4), IntegerField(3, 9)])

    @property
    def tipo_limite(self) -> Optional[int]:
        """
        Flag para indicar se será estabelecido um número
        máximo ou um número fixo de iterações.

        :return: O tipo de limite de iterações.
        :rtype: int | None
        """

        return self.data[0]

    @tipo_limite.setter
    def tipo_limite(self, n: int):
        self.data[0] = n

    @property
    def iteracoes(self) -> Optional[int]:
        """
        O número máximo ou fixo de iterações do modelo no estudo.

        :return: O número de iterações.
        :rtype: int | None
        """

        return self.data[1]

    @iteracoes.setter
    def iteracoes(self, n: int):
        self.data[1] = n


class VE(Register):
    """
    Registro que contém os volumes de espera das UHEs.

    """

    IDENTIFIER = "VE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            FloatField(10, 24, 2),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código da usina associada ao volume.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def volume(self) -> Optional[float]:
        """
        O volume de espera.

        :return: O volume.
        :rtype: float | None
        """
        return self.data[3]

    @volume.setter
    def volume(self, v: float):
        self.data[3] = v


class FP(Register):
    """
    Registro que contém alteração de parâmetros para a construção da
    função de produção aproximada (FPHA) das usinas.
    """

    IDENTIFIER = "FP "
    IDENTIFIER_DIGITS = 3
    LINE = Line(
        [
            IntegerField(3, 3),
            IntegerField(1, 7),
            IntegerField(3, 10),
            IntegerField(3, 15),
            IntegerField(1, 20),
            IntegerField(1, 24),
            FloatField(10, 29, 2),
            FloatField(10, 39, 2),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código da UHE associada à restrição FP.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def tipo_tratamento_volume(self) -> Optional[int]:
        """
        O tipo de tratamento do volume na construção da FPHA
        (1 = aproximação linear; 2 = envoltória 3d).

        :return: O tipo de tratamento
        :rtype: int | None
        """
        return self.data[1]

    @tipo_tratamento_volume.setter
    def tipo_tratamento_volume(self, t: int):
        self.data[1] = t

    @property
    def numero_pontos_turbinamento(self) -> Optional[int]:
        """
        O número de pontos para discretização da janela de
        turbinamento.

        :return: O número de pontos
        :rtype: int | None
        """
        return self.data[2]

    @numero_pontos_turbinamento.setter
    def numero_pontos_turbinamento(self, n: int):
        self.data[2] = n

    @property
    def numero_pontos_volume(self) -> Optional[int]:
        """
        O número de pontos para discretização da janela de
        volume.

        :return: O número de pontos
        :rtype: int | None
        """
        return self.data[3]

    @numero_pontos_volume.setter
    def numero_pontos_volume(self, n: int):
        self.data[3] = n

    @property
    def verifica_concavidade(self) -> Optional[int]:
        """
        O flag para habilitar verificação da concavidade da
        curva da função de produção.

        :return: O flag para verificar concavidade
        :rtype: int | None
        """
        return self.data[4]

    @verifica_concavidade.setter
    def verifica_concavidade(self, n: int):
        self.data[4] = n

    @property
    def ajuste_minimos_quadrados(self) -> Optional[int]:
        """
        O flag para habilitar ajuste de mínimos quadrados da função.

        :return: O flag para ajuste de mínimos quadrados
        :rtype: int | None
        """
        return self.data[5]

    @ajuste_minimos_quadrados.setter
    def ajuste_minimos_quadrados(self, n: int):
        self.data[5] = n

    @property
    def comprimento_janela_volume(self) -> Optional[float]:
        """
        O comprimento da janela para discretização do volume
        (em % do volume útil).

        :return: O comprimento.
        :rtype: float | None
        """
        return self.data[6]

    @comprimento_janela_volume.setter
    def comprimento_janela_volume(self, lim: float):
        self.data[6] = lim

    @property
    def tolerancia_desvio(self) -> Optional[float]:
        """
        A tolerância para desvio na função de produção (%).

        :return: A tolerância.
        :rtype: float | None
        """
        return self.data[7]

    @tolerancia_desvio.setter
    def tolerancia_desvio(self, lim: float):
        self.data[7] = lim


class TX(Register):
    """
    Registro que contém a taxa de desconto anual utilizada no modelo
    DECOMP quando na construção da FCF.
    """

    IDENTIFIER = "TX  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            FloatField(10, 4, 1),
        ]
    )

    @property
    def taxa(self) -> Optional[float]:
        """
        A taxa de desconto em % utilizada no estudo.

        :return: A taxa.
        :rtype: float | None
        """
        return self.data[0]

    @taxa.setter
    def taxa(self, t: float):
        self.data[0] = t


class EZ(Register):
    """
    Registro que contém o percentual máximo do
    volume útil para acoplamento.
    """

    IDENTIFIER = "EZ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(5, 9, 1),
        ]
    )

    @property
    def uhe(self) -> Optional[int]:
        """
        Código da UHE.

        :return: O código da UHE.
        :rtype: int | None
        """
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        """
        O volume útil considerado para cálculo.

        :return: O volume útil em % do volume máximo.
        :rtype: float | None
        """
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u


class R11(Register):
    """
    Registro que contém as restrições de variação horária
    e diária no nível da Régua 11.
    """

    IDENTIFIER = "R11 "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            StageDateField(starting_position=4, special_day_character="I"),
            StageDateField(starting_position=12, special_day_character="F"),
            FloatField(10, 20, 2),
            FloatField(10, 30, 2),
            FloatField(10, 40, 2),
        ]
    )

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[0][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[0][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[0][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[0][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[0][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[0][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[1][2] = n

    @property
    def cota_inicial(self) -> Optional[float]:
        """
        A cota na Régua 11 na meia hora anterior
        ao início do estudo.

        :return: A cota.
        :rtype: float | None
        """
        return self.data[2]

    @cota_inicial.setter
    def cota_inicial(self, n: float):
        self.data[2] = n

    @property
    def variacao_maxima_horaria(self) -> Optional[float]:
        """
        A restrição de variação máxima horária no nível
        da Régua 11.

        :return: A variação máxima horária.
        :rtype: float | None
        """
        return self.data[3]

    @variacao_maxima_horaria.setter
    def variacao_maxima_horaria(self, n: float):
        self.data[3] = n

    @property
    def variacao_maxima_diaria(self) -> Optional[float]:
        """
        A restrição de variação máxima diária no nível
        da Régua 11.

        :return: A variação máxima diária.
        :rtype: float | None
        """
        return self.data[4]

    @variacao_maxima_diaria.setter
    def variacao_maxima_diaria(self, n: float):
        self.data[4] = n


class CR(Register):
    """
    Registro com o polinômio cota x vazão (máximo grau 7)
    para seções de rio.
    """

    IDENTIFIER = "CR  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            LiteralField(12, 9),
            IntegerField(2, 24),
            FloatField(15, 27, 7, format="E"),
            FloatField(15, 43, 7, format="E"),
            FloatField(15, 59, 7, format="E"),
            FloatField(15, 75, 7, format="E"),
            FloatField(15, 91, 7, format="E"),
            FloatField(15, 107, 7, format="E"),
            FloatField(15, 123, 7, format="E"),
        ]
    )

    @property
    def codigo_secao(self) -> Optional[int]:
        """
        Código de identificação da seção de rio conforme
        registro SECR.

        :return: O código.
        :rtype: int | None
        """

        return self.data[0]

    @codigo_secao.setter
    def codigo_secao(self, n: int):
        self.data[0] = n

    @property
    def nome_secao(self) -> Optional[str]:
        """
        Nome da seção de rio.

        :return: O nome.
        :rtype: str | None
        """

        return self.data[1]

    @nome_secao.setter
    def nome_secao(self, n: str):
        self.data[1] = n

    @property
    def grau(self) -> Optional[int]:
        """
        Grau do polinômio.

        :return: O grau.
        :rtype: int | None
        """

        return self.data[2]

    @grau.setter
    def grau(self, n: int):
        self.data[2] = n

    @property
    def coeficiente_a0(self) -> Optional[float]:
        """
        O coeficiente de grau 0 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[3]

    @coeficiente_a0.setter
    def coeficiente_a0(self, c: float):
        self.data[3] = c

    @property
    def coeficiente_a1(self) -> Optional[float]:
        """
        O coeficiente de grau 1 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[4]

    @coeficiente_a1.setter
    def coeficiente_a1(self, c: float):
        self.data[4] = c

    @property
    def coeficiente_a2(self) -> Optional[float]:
        """
        O coeficiente de grau 2 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[5]

    @coeficiente_a2.setter
    def coeficiente_a2(self, c: float):
        self.data[5] = c

    @property
    def coeficiente_a3(self) -> Optional[float]:
        """
        O coeficiente de grau 3 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[6]

    @coeficiente_a3.setter
    def coeficiente_a3(self, c: float):
        self.data[6] = c

    @property
    def coeficiente_a4(self) -> Optional[float]:
        """
        O coeficiente de grau 4 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[7]

    @coeficiente_a4.setter
    def coeficiente_a4(self, c: float):
        self.data[7] = c

    @property
    def coeficiente_a5(self) -> Optional[float]:
        """
        O coeficiente de grau 5 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[8]

    @coeficiente_a5.setter
    def coeficiente_a5(self, c: float):
        self.data[8] = c

    @property
    def coeficiente_a6(self) -> Optional[float]:
        """
        O coeficiente de grau 6 do polinômio.

        :return: O coeficiente.
        :rtype: float | None
        """

        return self.data[9]

    @coeficiente_a6.setter
    def coeficiente_a6(self, c: float):
        self.data[9] = c


class SECR(Register):
    """
    Registro que define as seções de rio. Cada seção de rio pode
    conter até 5 usinas de montante.
    """

    IDENTIFIER = "SECR "
    IDENTIFIER_DIGITS = 5
    LINE = Line(
        [
            IntegerField(3, 5),
            LiteralField(12, 9),
            IntegerField(3, 24),
            FloatField(5, 28, 2),
            IntegerField(3, 34),
            FloatField(5, 38, 2),
            IntegerField(3, 44),
            FloatField(5, 48, 2),
            IntegerField(3, 54),
            FloatField(5, 58, 2),
            IntegerField(3, 64),
            FloatField(5, 68, 2),
        ]
    )

    @property
    def codigo_secao(self) -> Optional[int]:
        """
        O código da seção de rio.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_secao.setter
    def codigo_secao(self, n: int):
        self.data[0] = n

    @property
    def nome_secao(self) -> Optional[str]:
        """
        Nome da seção de rio.

        :return: O nome.
        :rtype: str | None
        """

        return self.data[1]

    @nome_secao.setter
    def nome_secao(self, n: str):
        self.data[1] = n

    @property
    def codigo_usina_montante_1(self) -> Optional[int]:
        """
        O código da 1ª usina de montante a seção de rio.

        :return: O código.
        :rtype: int | None
        """
        return self.data[2]

    @codigo_usina_montante_1.setter
    def codigo_usina_montante_1(self, n: int):
        self.data[2] = n

    @property
    def fator_participacao_1(self) -> Optional[float]:
        """
        O fator de participação da 1ª usina de montante a seção de rio.

        :return: O fator.
        :rtype: float | None
        """
        return self.data[3]

    @fator_participacao_1.setter
    def fator_participacao_1(self, n: float):
        self.data[3] = n

    @property
    def codigo_usina_montante_2(self) -> Optional[int]:
        """
        O código da 2ª usina de montante a seção de rio.

        :return: O código.
        :rtype: int | None
        """
        return self.data[4]

    @codigo_usina_montante_2.setter
    def codigo_usina_montante_2(self, n: int):
        self.data[4] = n

    @property
    def fator_participacao_2(self) -> Optional[float]:
        """
        O fator de participação da 2ª usina de montante a seção de rio.

        :return: O fator.
        :rtype: float | None
        """
        return self.data[5]

    @fator_participacao_2.setter
    def fator_participacao_2(self, n: float):
        self.data[5] = n

    @property
    def codigo_usina_montante_3(self) -> Optional[int]:
        """
        O código da 3ª usina de montante a seção de rio.

        :return: O código.
        :rtype: int | None
        """
        return self.data[6]

    @codigo_usina_montante_3.setter
    def codigo_usina_montante_3(self, n: int):
        self.data[6] = n

    @property
    def fator_participacao_3(self) -> Optional[float]:
        """
        O fator de participação da 3ª usina de montante a seção de rio.

        :return: O fator.
        :rtype: float | None
        """
        return self.data[7]

    @fator_participacao_3.setter
    def fator_participacao_3(self, n: float):
        self.data[7] = n

    @property
    def codigo_usina_montante_4(self) -> Optional[int]:
        """
        O código da 4ª usina de montante a seção de rio.

        :return: O código.
        :rtype: int | None
        """
        return self.data[8]

    @codigo_usina_montante_4.setter
    def codigo_usina_montante_4(self, n: int):
        self.data[8] = n

    @property
    def fator_participacao_4(self) -> Optional[float]:
        """
        O fator de participação da 4ª usina de montante a seção de rio.

        :return: O fator.
        :rtype: float | None
        """
        return self.data[9]

    @fator_participacao_4.setter
    def fator_participacao_4(self, n: float):
        self.data[9] = n

    @property
    def codigo_usina_montante_5(self) -> Optional[int]:
        """
        O código da 5ª usina de montante a seção de rio.

        :return: O código.
        :rtype: int | None
        """
        return self.data[10]

    @codigo_usina_montante_5.setter
    def codigo_usina_montante_5(self, n: int):
        self.data[10] = n

    @property
    def fator_participacao_5(self) -> Optional[float]:
        """
        O fator de participação da 5ª usina de montante a seção de rio.

        :return: O fator.
        :rtype: float | None
        """
        return self.data[11]

    @fator_participacao_5.setter
    def fator_participacao_5(self, n: float):
        self.data[11] = n


class DA(Register):
    """
    Registro que contém as taxas de retirada de água.
    """

    IDENTIFIER = "DA  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            FloatField(10, 24, 2),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def taxa(self) -> Optional[float]:
        """
        A taxa de retirada de água.

        :return: A taxa.
        :type: float | None
        """
        return self.data[3]

    @taxa.setter
    def taxa(self, c: float):
        self.data[3] = c


class RE(Register):
    """
    Registro que contém os cadastros de restrições elétricas.
    """

    IDENTIFIER = "RE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=9, special_day_character="I"),
            StageDateField(starting_position=17, special_day_character="F"),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código para a restrição

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n


class LU(Register):
    """
    Registro que contém os cadastros de limites das restrições elétricas.

    """

    IDENTIFIER = "LU  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            FloatField(10, 24, 1),
            FloatField(10, 34, 1),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição RE associada aos limites.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def limite_inferior(self) -> Optional[float]:
        """
        O limite inferior para a restrição elétrica.

        :return: O limite
        :rtype: float | None
        """
        return self.data[3]

    @limite_inferior.setter
    def limite_inferior(self, lim: float):
        self.data[3] = lim

    @property
    def limite_superior(self) -> Optional[float]:
        """
        O limite superior para a restrição elétrica.

        :return: O limite
        :rtype: float | None
        """
        return self.data[4]

    @limite_superior.setter
    def limite_superior(self, lim: float):
        self.data[4] = lim


class FH(Register):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições elétricas.
    """

    IDENTIFIER = "FH  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            IntegerField(3, 24),
            IntegerField(2, 28),
            FloatField(10, 34, 7),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidráulica.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[3]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[3] = c

    @property
    def conjunto(self) -> Optional[int]:
        """
        O conjunto de máquinas da usina.

        :return: O conjunto.
        :rtype: int | None
        """
        return self.data[4]

    @conjunto.setter
    def conjunto(self, c: int):
        self.data[4] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da usina na restrição.

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[5]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[5] = f


class FT(Register):
    """
    Registro que contém os coeficientes das usinas térmicas
    nas restrições elétricas.
    """

    IDENTIFIER = "FT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            IntegerField(3, 24),
            FloatField(10, 34, 7),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina térmica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[3]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[3] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da usina na restrição.

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[4]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[4] = f


class FI(Register):
    """
    Registro que contém o sentido do fluxo da interligação
    entre os subsistemas associados à restrição elétrica.
    """

    IDENTIFIER = "FI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            LiteralField(2, 24),
            LiteralField(2, 29),
            FloatField(10, 34, 7),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def submercado_de(self) -> Optional[str]:
        """
        O submercado de origem (de).

        :return: O submercado.
        :rtype: str | None
        """
        return self.data[3]

    @submercado_de.setter
    def submercado_de(self, s: str):
        self.data[3] = s

    @property
    def submercado_para(self) -> Optional[str]:
        """
        O submercado de destino (para).

        :return: O submercado.
        :rtype: str | None
        """
        return self.data[4]

    @submercado_para.setter
    def submercado_para(self, s: str):
        self.data[4] = s

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da interligação.

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[5]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[5] = f


class FE(Register):
    """
    Registro que contém os coeficientes de participação dos
    contratos de importação/exportação de energia
    nas restrições elétricas.
    """

    IDENTIFIER = "FE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=8, special_day_character="I"),
            StageDateField(starting_position=16, special_day_character="F"),
            IntegerField(3, 24),
            FloatField(10, 34, 7),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def codigo_contrato(self) -> Optional[int]:
        """
        O código do contrato de importação/exportação.

        :return: O código.
        :rtype: int | None
        """
        return self.data[3]

    @codigo_contrato.setter
    def codigo_contrato(self, c: int):
        self.data[3] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação do contrato na restrição.

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[4]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[4] = f


class FR(Register):
    """
    Registro que contém os coeficientes de participação das
    fontes renováveis eólicas nas restrições elétricas.
    """

    IDENTIFIER = "FR  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=10, special_day_character="I"),
            StageDateField(starting_position=18, special_day_character="F"),
            IntegerField(5, 26),
            FloatField(10, 36, 7),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina eólica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[3]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[3] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da usina na restrição.

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[4]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[4] = f


class FC(Register):
    """
    Registro que contém os coeficientes de participação das
    demandas/cargas especiais nas restrições elétricas.
    """

    IDENTIFIER = "FC  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=10, special_day_character="I"),
            StageDateField(starting_position=18, special_day_character="F"),
            IntegerField(3, 26),
            FloatField(10, 36, 7),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[1][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[1][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[1][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[1][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[2][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[2][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[2][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[2][2] = n

    @property
    def codigo_demanda(self) -> Optional[int]:
        """
        O código da demanda especial.

        :return: O código.
        :rtype: int | None
        """
        return self.data[3]

    @codigo_demanda.setter
    def codigo_demanda(self, c: int):
        self.data[3] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da demanda
         especial na restrição.

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[4]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[4] = f


class CI(Register):
    """
    Registro que define contratos de importação de energia.
    """

    IDENTIFIER = "CI  "
    IDENTIFIER_DIGITS = 3
    LINE = Line(
        [
            IntegerField(3, 3),
            LiteralField(10, 7),
            IntegerField(5, 18),
            IntegerField(1, 23),
            StageDateField(starting_position=25, special_day_character="I"),
            StageDateField(starting_position=33, special_day_character="F"),
            IntegerField(1, 41),
            FloatField(10, 43, 1),
            FloatField(10, 53, 1),
            FloatField(10, 63, 1),
            FloatField(10, 73, 1),
            IntegerField(1, 85),
            FloatField(10, 88, 1),
        ]
    )


class CE(Register):
    """
    Registro que define contratos de exportação de energia.
    """

    IDENTIFIER = "CE  "
    IDENTIFIER_DIGITS = 3
    LINE = Line(
        [
            IntegerField(3, 3),
            LiteralField(10, 7),
            IntegerField(5, 18),
            IntegerField(1, 23),
            StageDateField(starting_position=25, special_day_character="I"),
            StageDateField(starting_position=33, special_day_character="F"),
            IntegerField(1, 41),
            FloatField(10, 43, 1),
            FloatField(10, 53, 1),
            FloatField(10, 63, 1),
            FloatField(10, 73, 1),
            IntegerField(1, 85),
            FloatField(10, 88, 1),
        ]
    )


class MH(Register):
    """
    Registro que contém as manutenções programadas das unidades
    geradoras hidráulicas.

    """

    IDENTIFIER = "MH  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(2, 12),
            StageDateField(starting_position=14, special_day_character="I"),
            StageDateField(starting_position=22, special_day_character="F"),
            IntegerField(1, 30),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto de unidades geradoras.

        :return: O código.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int):
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora.

        :return: O código.
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int):
        self.data[2] = c

    @property
    def dia_inicial(self) -> Optional[Union[str, int]]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[3][0]

    @dia_inicial.setter
    def dia_inicial(self, n: Union[str, int]):
        self.data[3][0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[3][1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[3][1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[3][2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[3][2] = n

    @property
    def dia_final(self) -> Optional[Union[str, int]]:
        """
        O dia final.

        :return: O dia.
        :rtype: str | int | None
        """

        return self.data[4][0]

    @dia_final.setter
    def dia_final(self, n: Union[str, int]):
        self.data[4][0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[4][1]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[4][1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[4][2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[4][2] = n

    @property
    def disponivel(self) -> Optional[int]:
        """
        O flag que indica se a unidade está disponível
        (0=indisponível, 1=disponível).

        :return: O flag.
        :rtype: int | None
        """
        return self.data[5]

    @disponivel.setter
    def disponivel(self, n: int):
        self.data[5] = n


class PE(Register):
    """
    Registro para definição de penalidades a serem consideradas
    no problema de otimização.
    """

    IDENTIFIER = "PE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([FloatField(10, 4, 3), FloatField(10, 14, 3)])

    @property
    def penalidade_vertimento(self) -> Optional[float]:
        """
        A penalidade de vertimento ($/hm³).

        :return: A penalidade.
        :rtype: float | None
        """

        return self.data[0]

    @penalidade_vertimento.setter
    def penalidade_vertimento(self, n: float):
        self.data[0] = n

    @property
    def fator_penalidade_violacao(self) -> Optional[float]:
        """
        O fator a ser aplicado à penalidade de violação de retrições
        físicas e operativas.

        :return: O fator.
        :rtype: float | None
        """

        return self.data[1]

    @fator_penalidade_violacao.setter
    def fator_penalidade_violacao(self, n: float):
        self.data[1] = n
