from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.literalfield import LiteralField

from typing import Optional


class HidreletricaCurvaJusante(Register):
    """ """

    __slots__ = []

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

    __slots__ = []

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


class HidreletricaCurvaJusantePolinomioPorPartesSegmento(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "HIDRELETRICA-CURVAJUSANTE-POLINOMIOPORPARTES-SEGMENTO"
    IDENTIFIER_DIGITS = 54
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(size=20, decimal_digits=3),
            FloatField(size=20, decimal_digits=3),
            FloatField(size=20, decimal_digits=14, format="E"),
            FloatField(size=20, decimal_digits=14, format="E"),
            FloatField(size=20, decimal_digits=14, format="E"),
            FloatField(size=20, decimal_digits=14, format="E"),
            FloatField(size=20, decimal_digits=14, format="E"),
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
    def indice_polinomio(self) -> Optional[int]:
        """
        O índice do polinômio da respectiva família.

        :return: O índice do polinômio
        :rtype: int | None
        """
        return self.data[2]

    @indice_polinomio.setter
    def indice_polinomio(self, c: int):
        self.data[2] = c

    @property
    def limite_inferior_vazao_jusante(self) -> Optional[float]:
        """
        O limite inferior de vazão de jusante (defluência mais lateral)
        para janela de validade do polinômio.

        :return: O limite inferior de vazão de jusante
        :rtype: float | None
        """
        return self.data[3]

    @limite_inferior_vazao_jusante.setter
    def limite_inferior_vazao_jusante(self, c: float):
        self.data[3] = c

    @property
    def limite_superior_vazao_jusante(self) -> Optional[float]:
        """
        O limite superior de vazão de jusante (defluência mais lateral)
        para janela de validade do polinômio.

        :return: O limite superior de vazão de jusante
        :rtype: float | None
        """
        return self.data[4]

    @limite_superior_vazao_jusante.setter
    def limite_superior_vazao_jusante(self, c: float):
        self.data[4] = c

    @property
    def coeficiente_a0(self) -> Optional[float]:
        """
        O coeficiente de grau 0 do polinômio.

        :return: O coeficiente de grau 0 do polinômio
        :rtype: float | None
        """
        return self.data[5]

    @coeficiente_a0.setter
    def coeficiente_a0(self, c: float):
        self.data[5] = c

    @property
    def coeficiente_a1(self) -> Optional[float]:
        """
        O coeficiente de grau 1 do polinômio.

        :return: O coeficiente de grau 1 do polinômio
        :rtype: float | None
        """
        return self.data[6]

    @coeficiente_a1.setter
    def coeficiente_a1(self, c: float):
        self.data[6] = c

    @property
    def coeficiente_a2(self) -> Optional[float]:
        """
        O coeficiente de grau 2 do polinômio.

        :return: O coeficiente de grau 2 do polinômio
        :rtype: float | None
        """
        return self.data[7]

    @coeficiente_a2.setter
    def coeficiente_a2(self, c: float):
        self.data[7] = c

    @property
    def coeficiente_a3(self) -> Optional[float]:
        """
        O coeficiente de grau 3 do polinômio.

        :return: O coeficiente de grau 3 do polinômio
        :rtype: float | None
        """
        return self.data[8]

    @coeficiente_a3.setter
    def coeficiente_a3(self, c: float):
        self.data[8] = c

    @property
    def coeficiente_a4(self) -> Optional[float]:
        """
        O coeficiente de grau 4 do polinômio.

        :return: O coeficiente de grau 4 do polinômio
        :rtype: float | None
        """
        return self.data[9]

    @coeficiente_a4.setter
    def coeficiente_a4(self, c: float):
        self.data[9] = c


class HidreletricaCurvaJusanteAfogamentoExplicitoUsina(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "HIDRELETRICA-CURVAJUSANTE-AFOGAMENTO-EXPLICITO-USINA"
    IDENTIFIER_DIGITS = 53
    LINE = Line(
        [
            IntegerField(),
            LiteralField(size=3),
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
    def considera_afogamento(self) -> Optional[str]:
        """
        Habilitação do afogamento explícito.

        :return: O flag da habilitação.
        :rtype: str | None
        """
        return self.data[1]

    @considera_afogamento.setter
    def considera_afogamento(self, c: str):
        self.data[1] = c


class HidreletricaCurvaJusanteAfogamentoExplicitoPadrao(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "HIDRELETRICA-CURVAJUSANTE-AFOGAMENTO-EXPLICITO-PADRAO"
    IDENTIFIER_DIGITS = 54
    LINE = Line(
        [
            LiteralField(size=3),
        ],
        delimiter=";",
    )

    @property
    def considera_afogamento(self) -> Optional[str]:
        """
        Habilitação do afogamento explícito.

        :return: O flag da habilitação.
        :rtype: str | None
        """
        return self.data[0]

    @considera_afogamento.setter
    def considera_afogamento(self, c: str):
        self.data[0] = c


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
