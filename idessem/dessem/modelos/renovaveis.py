from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from typing import Optional


class EOLICA(Register):
    """
    Registro que contém o cadastro de uma fonte de geração
    não simulada.
    """

    IDENTIFIER = "EOLICA"
    IDENTIFIER_DIGITS = 6
    LINE = Line(
        [
            IntegerField(1, 0),
            LiteralField(40, 0),
            FloatField(10, 0, decimal_digits=0),
            FloatField(10, 0, decimal_digits=0),
            IntegerField(1, 0),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código de identificação da usina em questão
        no modelo.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, cod: int):
        self.data[0] = cod

    @property
    def nome_usina(self) -> Optional[str]:
        """
        O nome da usina em questão.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[1]

    @nome_usina.setter
    def nome_usina(self, n: str):
        self.data[1] = n

    @property
    def potencia_maxima(self) -> Optional[float]:
        """
        A potência máxima de geração da usina.

        :return: A potência máxima.
        :rtype: float | None
        """
        return self.data[2]

    @potencia_maxima.setter
    def potencia_maxima(self, p: float):
        self.data[2] = p

    @property
    def fator_capacidade(self) -> Optional[float]:
        """
        O fator de capacidade da usina

        :return: O fator de capacidade.
        :rtype: float | None
        """
        return self.data[3]

    @fator_capacidade.setter
    def fator_capacidade(self, p: float):
        self.data[3] = p

    @property
    def constrained_off(self) -> Optional[int]:
        """
        A consideração ou não de constrained-off para
        a usina.

        :return: O valor do flag.
        :rtype: int | None
        """
        return self.data[4]

    @constrained_off.setter
    def constrained_off(self, p: int):
        self.data[4] = p


class EOLICABARRA(Register):
    """
    Registro que contém o cadastro de uma relação entre uma
    usina e uma barra.
    """

    IDENTIFIER = "EOLICABARRA"
    IDENTIFIER_DIGITS = 11
    LINE = Line(
        [
            IntegerField(5, 0),
            IntegerField(5, 0),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código de identificação da usina que se conecta
        à barra.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, cod: int):
        self.data[0] = cod

    @property
    def codigo_barra(self) -> Optional[int]:
        """
        O código de identificação da barra à qual a usina
        se conecta.

        :return: O código.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_barra.setter
    def codigo_barra(self, n: int):
        self.data[1] = n


class EOLICASUBM(Register):
    """
    Registro que contém o cadastro de uma relação entre uma
    usina e um submercado à qual a usina pertence.
    """

    IDENTIFIER = "EOLICASUBM"
    IDENTIFIER_DIGITS = 10
    LINE = Line(
        [
            IntegerField(5, 0),
            LiteralField(2, 0),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código de identificação da usina que pertence ao submercado.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, cod: int):
        self.data[0] = cod

    @property
    def submercado(self) -> Optional[str]:
        """
        O nome do submercado à qual a usina pertence.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[1]

    @submercado.setter
    def submercado(self, n: str):
        self.data[1] = n


class EOLICAGERACAO(Register):
    """
    Registro que contém os valores das gerações disponíveis
    previstas das usinas.
    """

    IDENTIFIER = "EOLICA-GERACAO"
    IDENTIFIER_DIGITS = 14
    LINE = Line(
        [
            IntegerField(5, 0),
            IntegerField(2, 0),
            IntegerField(2, 0),
            IntegerField(1, 0),
            IntegerField(2, 0),
            IntegerField(2, 0),
            IntegerField(1, 0),
            FloatField(10, 0, decimal_digits=2),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código de identificação da usina que se conecta
        à barra.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, cod: int):
        self.data[0] = cod

    @property
    def dia_inicio(self) -> Optional[int]:
        """
        O dia de início da validade do valor de geração

        :return: O dia.
        :rtype: int | None
        """
        return self.data[1]

    @dia_inicio.setter
    def dia_inicio(self, n: int):
        self.data[1] = n

    @property
    def hora_inicio(self) -> Optional[int]:
        """
        A hora de início da validade do valor de geração

        :return: A hora.
        :rtype: int | None
        """
        return self.data[2]

    @hora_inicio.setter
    def hora_inicio(self, n: int):
        self.data[2] = n

    @property
    def meia_hora_inicio(self) -> Optional[int]:
        """
        O flag indicando a meia-hora de início da
        validade do valor de geração

        :return: O valor do flag.
        :rtype: int | None
        """
        return self.data[3]

    @meia_hora_inicio.setter
    def meia_hora_inicio(self, n: int):
        self.data[3] = n

    @property
    def dia_fim(self) -> Optional[int]:
        """
        O dia de fim da validade do valor de geração

        :return: O dia.
        :rtype: int | None
        """
        return self.data[4]

    @dia_fim.setter
    def dia_fim(self, n: int):
        self.data[4] = n

    @property
    def hora_fim(self) -> Optional[int]:
        """
        A hora de fim da validade do valor de geração

        :return: A hora.
        :rtype: int | None
        """
        return self.data[5]

    @hora_fim.setter
    def hora_fim(self, n: int):
        self.data[5] = n

    @property
    def meia_hora_fim(self) -> Optional[int]:
        """
        O flag indicando a meia-hora de fim da
        validade do valor de geração

        :return: O valor do flag.
        :rtype: int | None
        """
        return self.data[6]

    @meia_hora_fim.setter
    def meia_hora_fim(self, n: int):
        self.data[6] = n

    @property
    def geracao(self) -> Optional[float]:
        """
        O valor de geração válido para o intervalo
        definido.

        :return: O valor da geração.
        :rtype: float | None
        """
        return self.data[7]

    @geracao.setter
    def geracao(self, n: float):
        self.data[7] = n
