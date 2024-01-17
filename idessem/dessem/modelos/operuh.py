from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from idessem.dessem.modelos.componentes.stagedatefield import StageDateField
from typing import Optional, Union


class REST(Register):
    """
    Registro que define as restrições operativas hidráulicas.
    """

    IDENTIFIER = "OPERUH REST  "
    IDENTIFIER_DIGITS = 13
    LINE = Line(
        [
            IntegerField(size=5, starting_position=14),
            LiteralField(size=1, starting_position=21),
            LiteralField(size=1, starting_position=23),
            LiteralField(size=12, starting_position=27),
            FloatField(size=10, starting_position=40, decimal_digits=2),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código para a restrição OPERUH.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def tipo(self) -> Optional[str]:
        """
        O tipo da restrição.

        :return: O tipo.
        :rtype: str | None
        """
        return self.data[1]

    @tipo.setter
    def tipo(self, c: str):
        self.data[1] = c

    @property
    def intervalo_aplicacao(self) -> Optional[str]:
        """
        O intervalo de aplicação.

        :return: O tipo.
        :rtype: str | None
        """
        return self.data[2]

    @intervalo_aplicacao.setter
    def intervalo_aplicacao(self, c: str):
        self.data[2] = c

    @property
    def justificativa(self) -> Optional[str]:
        """
        A justificativa para a restrição (informativo).

        :return: A justificativa.
        :rtype: str | None
        """
        return self.data[3]

    @justificativa.setter
    def justificativa(self, c: str):
        self.data[3] = c

    @property
    def valor_inicial(self) -> Optional[float]:
        """
        O valor da variável que está sendo restrita,
        na meia-hora anterior ao início.

        :return: O valor inicial.
        :rtype: float | None
        """
        return self.data[4]

    @valor_inicial.setter
    def valor_inicial(self, c: float):
        self.data[4] = c


class ELEM(Register):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    na restrição.
    """

    IDENTIFIER = "OPERUH ELEM  "
    IDENTIFIER_DIGITS = 13
    LINE = Line(
        [
            IntegerField(size=5, starting_position=14),
            IntegerField(size=3, starting_position=20),
            LiteralField(size=12, starting_position=25),
            IntegerField(size=2, starting_position=40),
            FloatField(size=5, starting_position=43, decimal_digits=2),
        ]
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código para a restrição OPERUH.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica.

        :return: O código.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[1] = c

    @property
    def nome_usina(self) -> Optional[str]:
        """
        O nome da usina hidrelétrica (apenas informativo).

        :return: O nome.
        :rtype: str | None
        """
        return self.data[2]

    @nome_usina.setter
    def nome_usina(self, c: str):
        self.data[2] = c

    @property
    def tipo(self) -> Optional[int]:
        """
        O tipo da variável que compõe a restrição.

        :return: O tipo da variável.
        :rtype: int | None
        """
        return self.data[3]

    @tipo.setter
    def tipo(self, c: int):
        self.data[3] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente da variável na restrição.

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[4]

    @coeficiente.setter
    def coeficiente(self, c: float):
        self.data[4] = c


class LIM(Register):
    """
    Registro que contém os limites da restrição.

    """

    IDENTIFIER = "OPERUH LIM   "
    IDENTIFIER_DIGITS = 13
    LINE = Line(
        [
            IntegerField(size=5, starting_position=14),
            StageDateField(starting_position=20, special_day_character="I"),
            StageDateField(starting_position=28, special_day_character="F"),
            FloatField(size=10, starting_position=38, decimal_digits=2),
            FloatField(size=10, starting_position=48, decimal_digits=2),
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
        O limite inferior para a restrição.

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
        O limite superior para a restrição.

        :return: O limite
        :rtype: float | None
        """
        return self.data[4]

    @limite_superior.setter
    def limite_superior(self, lim: float):
        self.data[4] = lim


class VAR(Register):
    """
    Registro que contém os limites da restrição de variação:
    rampas máximas horárias de acréscimo ou decréscimo.

    """

    IDENTIFIER = "OPERUH VAR   "
    IDENTIFIER_DIGITS = 13
    LINE = Line(
        [
            IntegerField(size=5, starting_position=14),
            StageDateField(starting_position=19, special_day_character="I"),
            StageDateField(starting_position=27, special_day_character="F"),
            FloatField(size=10, starting_position=37, decimal_digits=2),
            FloatField(size=10, starting_position=47, decimal_digits=2),
            FloatField(size=10, starting_position=57, decimal_digits=2),
            FloatField(size=10, starting_position=67, decimal_digits=2),
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
    def rampa_maxima_decrescimo_percentual(self) -> Optional[float]:
        """
        A rampa máxima para decréscimo em % do valor máximo da
        variável por hora.

        :return: A rampa.
        :rtype: float | None
        """
        return self.data[3]

    @rampa_maxima_decrescimo_percentual.setter
    def rampa_maxima_decrescimo_percentual(self, lim: float):
        self.data[3] = lim

    @property
    def rampa_maxima_acrescimo_percentual(self) -> Optional[float]:
        """
        A rampa máxima para acréscimo em % do valor máximo da
        variável por hora.

        :return: A rampa.
        :rtype: float | None
        """
        return self.data[4]

    @rampa_maxima_acrescimo_percentual.setter
    def rampa_maxima_acrescimo_percentual(self, lim: float):
        self.data[4] = lim

    @property
    def rampa_maxima_decrescimo_absoluta(self) -> Optional[float]:
        """
        A rampa máxima para decréscimo na unidade da variável
        por hora.

        :return: A rampa.
        :rtype: float | None
        """
        return self.data[5]

    @rampa_maxima_decrescimo_absoluta.setter
    def rampa_maxima_decrescimo_absoluta(self, lim: float):
        self.data[5] = lim

    @property
    def rampa_maxima_acrescimo_absoluta(self) -> Optional[float]:
        """
        A rampa máxima para acréscimo na unidade da variável
        por hora.

        :return: A rampa.
        :rtype: float | None
        """
        return self.data[6]

    @rampa_maxima_acrescimo_absoluta.setter
    def rampa_maxima_acrescimo_absoluta(self, lim: float):
        self.data[6] = lim
