from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from typing import Optional


class RegistroCaso(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o nome do caso.
    """

    IDENTIFIER = "CASO     "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroTitulo(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o título do estudo.
    """

    IDENTIFIER = "TITULO   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroVazoes(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com as vazões naturais.
    """

    IDENTIFIER = "VAZOES   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroDadger(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com os dados gerais.
    """

    IDENTIFIER = "DADGER   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroMapfcf(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o cabeçalho da FCF do DECOMP.
    """

    IDENTIFIER = "MAPFCF   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroCortfcf(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com a FCF do DECOMP.
    """

    IDENTIFIER = "CORTFCF  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroCadusih(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o cadastro de usinas hidroelétricas.
    """

    IDENTIFIER = "CADUSIH  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroOperuh(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com restrições operativas de usinas hidroelétricas.
    """

    IDENTIFIER = "OPERUH   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroDeflant(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com defluências anteriores ao estudo.
    """

    IDENTIFIER = "DEFLANT  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroCadterm(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o cadastro das usinas térmicas.
    """

    IDENTIFIER = "CADTERM  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroOperut(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados da operação das unidades térmicas.
    """

    IDENTIFIER = "OPERUT   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroIndelet(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o índice da rede elétrica.
    """

    IDENTIFIER = "INDELET  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroIlstri(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados do Canal Pereira Barreto.
    """

    IDENTIFIER = "ILSTRI   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroCotasR11(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados do Canal Pereira Barreto.
    """

    IDENTIFIER = "COTASR11 "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroSimul(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados para a simulação.
    """

    IDENTIFIER = "SIMUL    "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroAreacont(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com cadastro de reserva de potência.
    """

    IDENTIFIER = "AREACONT "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroRespot(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o estudo de reserva de potência.
    """

    IDENTIFIER = "RESPOT   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroMlt(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados para a FPHA.
    """

    IDENTIFIER = "MLT      "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroTolperd(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados das tolerâncias das perdas.
    """

    IDENTIFIER = "TOLPERD  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroCurvtviag(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com a curva de propagação do tempo de viagem.
    """

    IDENTIFIER = "CURVTVIAG"
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroPtoper(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com o ponto de operação das usinas GNL.
    """

    IDENTIFIER = "PTOPER   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroInfofcf(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com a informação sobre os cortes recebidos.
    """

    IDENTIFIER = "INFOFCF  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroMetas(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com restrições de metas.
    """

    IDENTIFIER = "META     "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroREE(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados dos reservatórios equivalentes de energia.
    """

    IDENTIFIER = "REE      "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroEolica(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados de renováveis.
    """

    IDENTIFIER = "EOLICA   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroRampas(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados de trajetórias de rampas.
    """

    IDENTIFIER = "RAMPAS   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroRstlpp(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com restrições LPP.
    """

    IDENTIFIER = "RSTLPP   "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroRestseg(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com restrições de tabela.
    """

    IDENTIFIER = "RESTSEG  "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroRespotele(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com reserva de potência da rede elétrica.
    """

    IDENTIFIER = "RESPOTELE"
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroIlibs(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com funcionalidades das LIBS.
    """

    IDENTIFIER = "ILIBS    "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c


class RegistroUch(Register):
    """
    Registro com uma informação do arquivo de entrada do DESSEM `dessem.arq`
    com dados de entrada relacionados ao Unit Commitment Hidráulico (UCH).
    """

    IDENTIFIER = "UCH      "
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            LiteralField(size=38, starting_position=10),
            LiteralField(size=80, starting_position=49),
        ],
    )

    @property
    def descricao(self) -> Optional[str]:
        """
        A descrição do campo.

        :return: A descrição do campo como uma string.
        :rtype: str | None
        """
        return self.data[0].strip()

    @descricao.setter
    def descricao(self, c: str):
        self.data[0] = c

    @property
    def valor(self) -> Optional[str]:
        """
        O valor do campo.

        :return: O valor do campo como uma string.
        :rtype: str | None
        """
        return self.data[1].strip()

    @valor.setter
    def valor(self, c: str):
        self.data[1] = c
