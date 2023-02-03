from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField

from typing import Optional


class HidreletricaCurvaJusante(Register):
    """ """

    IDENTIFIER = "HIDRELETRICA-CURVAJUSANTE"
    IDENTIFIER_DIGITS = 26
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=4),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica relacionada ao polinômio.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def indice_familia(self) -> Optional[int]:
        """
        O índice da família de polinômios.

        :return: O índice (sequencial).
        :rtype: int | None
        """
        return self.data[1]

    @indice_familia.setter
    def indice_familia(self, c: int):
        self.data[1] = c

    @property
    def nivel_montante_referencia(self) -> Optional[float]:
        """
        O nível de montante da usina de jusante
        de referência.

        :return: O nível em metros
        :rtype: float | None
        """
        return self.data[2]

    @nivel_montante_referencia.setter
    def nivel_montante_referencia(self, c: float):
        self.data[2] = c


class HidreletricaCurvaJusantePolinomioPorPartes(Register):
    """ """

    IDENTIFIER = "HIDRELETRICA-CURVAJUSANTE-POLINOMIOPORPARTES"
    IDENTIFIER_DIGITS = 45
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica relacionada ao polinômio.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def indice_familia(self) -> Optional[int]:
        """
        O índice da família de polinômios.

        :return: O índice (sequencial).
        :rtype: int | None
        """
        return self.data[1]

    @indice_familia.setter
    def indice_familia(self, c: int):
        self.data[1] = c

    @property
    def numero_polinomios(self) -> Optional[int]:
        """
        O número de polinômios existentes na família.

        :return: O número de polinômios
        :rtype: int | None
        """
        return self.data[2]

    @numero_polinomios.setter
    def numero_polinomios(self, c: int):
        self.data[2] = c
