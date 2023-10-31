from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField

from typing import Optional


class HidreletricaVazaoJusanteInfluenciaDefluencia(Register):
    """ """

    IDENTIFIER = "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-DEFLUENCIA"
    IDENTIFIER_DIGITS = 48
    LINE = Line(
        [
            IntegerField(),
            FloatField(decimal_digits=3),
            FloatField(decimal_digits=3),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina_influenciada(self) -> Optional[int]:
        """
        O código da usina hidrelétrica influenciada.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_influenciada.setter
    def codigo_usina_influenciada(self, c: int):
        self.data[0] = c

    @property
    def fator_impacto_turbinamento(self) -> Optional[float]:
        """
        O fator de impacto referente ao turbinamento da usina.

        :return: O fator do turbinamento
        :rtype: float | None
        """
        return self.data[1]

    @fator_impacto_turbinamento.setter
    def fator_impacto_turbinamento(self, c: float):
        self.data[1] = c

    @property
    def fator_impacto_vertimento(self) -> Optional[float]:
        """
        O fator de impacto referente ao vertimento da usina.

        :return: O fator do vertimento
        :rtype: float | None
        """
        return self.data[2]

    @fator_impacto_vertimento.setter
    def fator_impacto_vertimento(self, c: float):
        self.data[2] = c


class HidreletricaVazaoJusanteInfluenciaPosto(Register):
    """ """

    IDENTIFIER = "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-POSTO"
    IDENTIFIER_DIGITS = 43
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=3),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina_influenciada(self) -> Optional[int]:
        """
        O código da usina hidrelétrica influenciada.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_influenciada.setter
    def codigo_usina_influenciada(self, c: int):
        self.data[0] = c

    @property
    def codigo_usina_influenciadora(self) -> Optional[float]:
        """
        O código da usina cuja vazão incremental influencia
        lateralmente.

        :return: O código da usina
        :rtype: float | None
        """
        return self.data[1]

    @codigo_usina_influenciadora.setter
    def codigo_usina_influenciadora(self, c: float):
        self.data[1] = c

    @property
    def fator_impacto(self) -> Optional[float]:
        """
        O fator de impacto referente a vazão lateral.

        :return: O fator da vazão lateral
        :rtype: float | None
        """
        return self.data[2]

    @fator_impacto.setter
    def fator_impacto(self, c: float):
        self.data[2] = c


class HidreletricaVazaoJusanteInfluenciaUsina(Register):
    """ """

    IDENTIFIER = "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-USINA"
    IDENTIFIER_DIGITS = 43
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=3),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina_influenciada(self) -> Optional[int]:
        """
        O código da usina hidrelétrica influenciada.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_influenciada.setter
    def codigo_usina_influenciada(self, c: int):
        self.data[0] = c

    @property
    def codigo_usina_influenciadora(self) -> Optional[float]:
        """
        O código da usina cuja vazão defluente influencia
        lateralmente.

        :return: O código da usina
        :rtype: float | None
        """
        return self.data[1]

    @codigo_usina_influenciadora.setter
    def codigo_usina_influenciadora(self, c: float):
        self.data[1] = c

    @property
    def fator_impacto(self) -> Optional[float]:
        """
        O fator de impacto referente a vazão lateral.

        :return: O fator da vazão lateral
        :rtype: float | None
        """
        return self.data[2]

    @fator_impacto.setter
    def fator_impacto(self, c: float):
        self.data[2] = c
