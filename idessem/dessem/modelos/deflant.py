from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from idessem.dessem.modelos.componentes.stagedatefield import StageDateField
from typing import Optional, Union

class DEFANT(Register):
    """
    Registro que contém as defluências anteriores ao início do período
    do estudo.
    """

    IDENTIFIER = "DEFANT   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            IntegerField(3, 9),
            IntegerField(3, 14),
            LiteralField(1,19),
            StageDateField(starting_position=24, special_day_character="I"),
            StageDateField(starting_position=32, special_day_character="F"),
            FloatField(10,44,1)
        ]
    )

    @property
    def codigo_usina_montante(self) -> Optional[int]:
        """
        O código da UHE a montante.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_montante.setter
    def codigo_usina_montante(self, u: int):
        self.data[0] = u

    @property
    def codigo_elemento_jusante(self) -> Optional[int]:
        """
        O código do elemento a jusante.

        :return: O código
        :rtype: int | None
        """
        return self.data[1]

    @codigo_elemento_jusante.setter
    def codigo_elemento_jusante(self, u: int):
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
    def defluencia(self) -> Optional[float]:
        """
        A defluência da usina.

        :return: A defluência.
        :rtype: float | None
        """
        return self.data[5]

    @defluencia.setter
    def defluencia(self, cod: float):
        self.data[5] = cod
