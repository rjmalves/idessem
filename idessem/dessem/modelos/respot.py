from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from idessem.dessem.modelos.componentes.stagedatefield import StageDateField
from typing import Optional, Union

class RP(Register):
    """
    Registro que contém as áreas e janela de tempo para consideração das
    restrições de reserva de potência.
    """

    IDENTIFIER = "RP  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=9, special_day_character="I"),
            StageDateField(starting_position=17, special_day_character="F"),
            LiteralField(40,30)
        ]
    )

    @property
    def codigo_area(self) -> Optional[int]:
        """
        O código da área de controle.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_area.setter
    def codigo_area(self, u: int):
        self.data[0] = u


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
    def descricao(self) -> Optional[str]:
        """
        A descrição da área.

        :return: A descrição.
        :rtype: str | None
        """
        return self.data[3]

    @descricao.setter
    def descricao(self, cod: str):
        self.data[3] = cod

class LM(Register):
    """
    Registro que contém a reserva mínima de potência para a área.
    """

    IDENTIFIER = "LM  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            StageDateField(starting_position=9, special_day_character="I"),
            StageDateField(starting_position=17, special_day_character="F"),
            FloatField(10,25,2)
        ]
    )

    @property
    def codigo_area(self) -> Optional[int]:
        """
        O código da área de controle.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_area.setter
    def codigo_area(self, u: int):
        self.data[0] = u


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
        O limite inferior para reserva de potência.

        :return: O limite.
        :rtype: float | None
        """
        return self.data[3]

    @limite_inferior.setter
    def limite_inferior(self, cod: float):
        self.data[3] = cod
