from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from typing import Optional


class CADUSIT(Register):
    """
    Registro que define as características das usinas termoelétricas.
    """

    IDENTIFIER = "CADUSIT "
    IDENTIFIER_DIGITS = 8
    LINE = Line(
        [
            IntegerField(size=3, starting_position=8),
            LiteralField(size=12, starting_position=12),
            IntegerField(size=2, starting_position=25),
            IntegerField(size=4, starting_position=28),
            IntegerField(size=2, starting_position=33),
            IntegerField(size=2, starting_position=36),
            IntegerField(size=2, starting_position=39),
            IntegerField(size=1, starting_position=42),
            IntegerField(size=3, starting_position=45),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def nome_usina(self) -> Optional[str]:
        """
        O nome da usina termelétrica.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[1]

    @nome_usina.setter
    def nome_usina(self, c: str):
        self.data[1] = c

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O código do submercado.

        :return: O código.
        :rtype: int | None
        """
        return self.data[2]

    @codigo_submercado.setter
    def codigo_submercado(self, c: int):
        self.data[2] = c

    @property
    def ano_operacao(self) -> Optional[int]:
        """
        O ano em que a usina entra em operação.

        :return: O ano.
        :rtype: int | None
        """
        return self.data[3]

    @ano_operacao.setter
    def ano_operacao(self, c: int):
        self.data[3] = c

    @property
    def mes_operacao(self) -> Optional[int]:
        """
        O mês em que a usina entra em operação.

        :return: O mês.
        :rtype: int | None
        """
        return self.data[4]

    @mes_operacao.setter
    def mes_operacao(self, c: int):
        self.data[4] = c

    @property
    def dia_operacao(self) -> Optional[int]:
        """
        O dia em que a usina entra em operação.

        :return: O dia.
        :rtype: int | None
        """
        return self.data[5]

    @dia_operacao.setter
    def dia_operacao(self, c: int):
        self.data[5] = c

    @property
    def hora_operacao(self) -> Optional[int]:
        """
        A hora em que a usina entra em operação.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[6]

    @hora_operacao.setter
    def hora_operacao(self, c: int):
        self.data[6] = c

    @property
    def meia_hora_operacao(self) -> Optional[int]:
        """
        A meia-hora em que a usina entra em operação.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[7]

    @meia_hora_operacao.setter
    def meia_hora_operacao(self, c: int):
        self.data[7] = c

    @property
    def numero_unidades(self) -> Optional[int]:
        """
        O número de unidades da usina.

        :return: O número de unidades.
        :rtype: int | None
        """
        return self.data[8]

    @numero_unidades.setter
    def numero_unidades(self, c: int):
        self.data[8] = c


class CADUNIDT(Register):
    """
    Registro que define as características das unidades geradoras das
    usinas termoelétricas.
    """

    IDENTIFIER = "CADUNIDT "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            IntegerField(size=3, starting_position=9),
            IntegerField(size=3, starting_position=12),
            IntegerField(size=4, starting_position=16),
            IntegerField(size=2, starting_position=21),
            IntegerField(size=2, starting_position=24),
            IntegerField(size=2, starting_position=27),
            IntegerField(size=1, starting_position=30),
            FloatField(size=10, starting_position=33, decimal_digits=3),
            FloatField(size=10, starting_position=44, decimal_digits=3),
            IntegerField(size=5, starting_position=55),
            IntegerField(size=5, starting_position=61),
            FloatField(size=10, starting_position=67, decimal_digits=2),
            FloatField(size=10, starting_position=89, decimal_digits=2),
            FloatField(size=10, starting_position=100, decimal_digits=3),
            FloatField(size=10, starting_position=112, decimal_digits=3),
            IntegerField(size=1, starting_position=122),
            IntegerField(size=2, starting_position=124),
            IntegerField(size=3, starting_position=127),
            FloatField(size=10, starting_position=131, decimal_digits=3),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int):
        self.data[1] = c

    @property
    def ano_operacao(self) -> Optional[int]:
        """
        O ano em que a usina entra em operação.

        :return: O ano.
        :rtype: int | None
        """
        return self.data[2]

    @ano_operacao.setter
    def ano_operacao(self, c: int):
        self.data[2] = c

    @property
    def mes_operacao(self) -> Optional[int]:
        """
        O mês em que a usina entra em operação.

        :return: O mês.
        :rtype: int | None
        """
        return self.data[3]

    @mes_operacao.setter
    def mes_operacao(self, c: int):
        self.data[3] = c

    @property
    def dia_operacao(self) -> Optional[int]:
        """
        O dia em que a usina entra em operação.

        :return: O dia.
        :rtype: int | None
        """
        return self.data[4]

    @dia_operacao.setter
    def dia_operacao(self, c: int):
        self.data[4] = c

    @property
    def hora_operacao(self) -> Optional[int]:
        """
        A hora em que a usina entra em operação.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[5]

    @hora_operacao.setter
    def hora_operacao(self, c: int):
        self.data[5] = c

    @property
    def meia_hora_operacao(self) -> Optional[int]:
        """
        A meia-hora em que a usina entra em operação.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[6]

    @meia_hora_operacao.setter
    def meia_hora_operacao(self, c: int):
        self.data[6] = c

    @property
    def capacidade_geracao(self) -> Optional[float]:
        """
        A capacidade de geração da unidade geradora.

        :return: A capacidade.
        :rtype: float | None
        """
        return self.data[7]

    @capacidade_geracao.setter
    def capacidade_geracao(self, c: float):
        self.data[7] = c

    @property
    def geracao_minima(self) -> Optional[float]:
        """
        A geração mínima da unidade geradora.

        :return: A geração mínima.
        :rtype: float | None
        """
        return self.data[8]

    @geracao_minima.setter
    def geracao_minima(self, c: float):
        self.data[8] = c

    @property
    def tempo_on(self) -> Optional[int]:
        """
        O tempo mínimo de permanência ligado.

        :return: O tempo.
        :rtype: int | None
        """
        return self.data[9]

    @tempo_on.setter
    def tempo_on(self, c: int):
        self.data[9] = c

    @property
    def tempo_off(self) -> Optional[int]:
        """
        O tempo mínimo de permanência desligado.

        :return: O tempo.
        :rtype: int | None
        """
        return self.data[10]

    @tempo_off.setter
    def tempo_off(self, c: int):
        self.data[10] = c

    @property
    def custo_acionamento_frio(self) -> Optional[float]:
        """
        O custo de acionamento a frio.

        :return: O custo.
        :rtype: float | None
        """
        return self.data[11]

    @custo_acionamento_frio.setter
    def custo_acionamento_frio(self, c: float):
        self.data[11] = c

    @property
    def custo_acionamento_quente(self) -> Optional[float]:
        """
        O custo de acionamento a quente.

        :return: O custo.
        :rtype: float | None
        """
        return self.data[12]

    @custo_acionamento_quente.setter
    def custo_acionamento_quente(self, c: float):
        self.data[12] = c

    @property
    def rampa_subida(self) -> Optional[float]:
        """
        A rampa de subida.

        :return: A rampa.
        :rtype: float | None
        """
        return self.data[13]

    @rampa_subida.setter
    def rampa_subida(self, c: float):
        self.data[13] = c

    @property
    def rampa_descida(self) -> Optional[float]:
        """
        A rampa de descida.

        :return: A rampa.
        :rtype: float | None
        """
        return self.data[14]

    @rampa_descida.setter
    def rampa_descida(self, c: float):
        self.data[14] = c

    @property
    def geracao_maxima_ou_minima(self) -> Optional[int]:
        """
        O flag para ativar restrição de geração máxima
        ou mínima.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[15]

    @geracao_maxima_ou_minima.setter
    def geracao_maxima_ou_minima(self, c: int):
        self.data[15] = c

    @property
    def numero_maximo_oscilacoes(self) -> Optional[int]:
        """
        O número máximo de oscilações entre geração máxima
        e mínima.

        :return: O número máximo.
        :rtype: int | None
        """
        return self.data[16]

    @numero_maximo_oscilacoes.setter
    def numero_maximo_oscilacoes(self, c: int):
        self.data[16] = c

    @property
    def unidades_equivalentes(self) -> Optional[int]:
        """
        O flag para ativar a opcao de unidades equivalentes
        para tratamento de usinas a ciclo combinado.

        :return: O flag.
        :rtype: int | None
        """
        return self.data[17]

    @unidades_equivalentes.setter
    def unidades_equivalentes(self, c: int):
        self.data[17] = c

    @property
    def rampa_transicao(self) -> Optional[float]:
        """
        A rampa de transição entre unidades equivalentes.

        :return: O flag.
        :rtype: float | None
        """
        return self.data[18]

    @rampa_transicao.setter
    def rampa_transicao(self, c: float):
        self.data[18] = c


class CADCONF(Register):
    """
    Registro que define as unidades equivalentes e reais.
    """

    IDENTIFIER = "CADCONF "
    IDENTIFIER_DIGITS = 8
    LINE = Line(
        [
            IntegerField(size=3, starting_position=8),
            IntegerField(size=3, starting_position=12),
            IntegerField(size=3, starting_position=16),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def codigo_unidade_equivalente(self) -> Optional[int]:
        """
        O código da unidade equivalente da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_unidade_equivalente.setter
    def codigo_unidade_equivalente(self, c: int):
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora pertecente à
        unidade equivalente da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int):
        self.data[2] = c


class CADMIN(Register):
    """
    Registro que define a quantidade de unidades reais disponíveis para
    acionamento da unidade equivalente.
    """

    IDENTIFIER = "CADMIN "
    IDENTIFIER_DIGITS = 7
    LINE = Line(
        [
            IntegerField(size=3, starting_position=8),
            IntegerField(size=3, starting_position=12),
            IntegerField(size=3, starting_position=16),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def codigo_unidade_equivalente(self) -> Optional[int]:
        """
        O código da unidade equivalente da usina termelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_unidade_equivalente.setter
    def codigo_unidade_equivalente(self, c: int):
        self.data[1] = c

    @property
    def numero_minimo_unidades(self) -> Optional[int]:
        """
        O número mínimo de unidades reais disponíveis para
        acionar a unidade equivalente da usina termelétrica.

        :return: O número mínimo.
        :rtype: int | None
        """
        return self.data[2]

    @numero_minimo_unidades.setter
    def numero_minimo_unidades(self, c: int):
        self.data[2] = c
