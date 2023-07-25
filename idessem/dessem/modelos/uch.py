from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField

from typing import Optional

# Registros faltantes
# UCH-OPCAO-UNIDADE-VAZIO-PADRAO
# UCH-OPCAO-CONJUNTO-VAZIO-PADRAO
# UCH-OPCAO-USINA-VAZIO-PADRAO
# UCH-CUSTO-PARTIDA-UNIDADE
# UCH-CUSTO-PARTIDA-CONJUNTO
# UCH-CUSTO-PARTIDA-USINA
# UCH-CUSTO-PARTIDA-VAZIO-UNIDADE
# UCH-CUSTO-PARTIDA-VAZIO-CONJUNTO
# UCH-CUSTO-PARTIDA-VAZIO-USINA
# UCH-CONSUMO-AGUA-VAZIO-UNIDADE
# UCH-CONSUMO-AGUA-VAZIO-CONJUNTO
# UCH-CONSUMO-AGUA-VAZIO-USINA
# UCH-LIMITE-MUDANCA-STATUS-VAZIO-UNIDADE
# UCH-LIMITE-MUDANCA-STATUS-VAZIO-CONJUNTO
# UCH-LIMITE-MUDANCA-STATUS-VAZIO-USINA


class UchOpcaoPadrao(Register):
    """ """

    IDENTIFIER = "UCH-OPCAO-PADRAO"
    IDENTIFIER_DIGITS = 16
    LINE = Line(
        [
            IntegerField(),
        ],
        delimiter=";",
    )

    @property
    def considera_uch(self) -> Optional[int]:
        """
        O flag se o modelo considerará UCH na sua execução.

        :return: O flag
        :rtype: int | None
        """
        return self.data[0]

    @considera_uch.setter
    def considera_uch(self, c: int):
        self.data[0] = c


class UchOpcaoUsina(Register):
    """ """

    IDENTIFIER = "UCH-OPCAO-USINA"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
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
    def considera_uch_usina(self) -> Optional[int]:
        """
        O flag se a usina considerará UCH na sua execução.

        :return: O flag
        :rtype: int | None
        """
        return self.data[1]

    @considera_uch_usina.setter
    def considera_uch_usina(self, c: int):
        self.data[1] = c


class UchOpcaoPadraoData(Register):
    """ """

    IDENTIFIER = "UCH-OPCAO-PADRAO-DATA"
    IDENTIFIER_DIGITS = 21
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
        ],
        delimiter=";",
    )

    @property
    def dia_inicial(self) -> Optional[int]:
        """
        O dia inicial.

        :return: O dia.
        :rtype: int | None
        """

        return self.data[0]

    @dia_inicial.setter
    def dia_inicial(self, n: int):
        self.data[0] = n

    @property
    def hora_inicial(self) -> Optional[int]:
        """
        A hora inicial.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1]

    @hora_inicial.setter
    def hora_inicial(self, n: int):
        self.data[1] = n

    @property
    def meia_hora_inicial(self) -> Optional[int]:
        """
        A meia-hora inicial.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2]

    @meia_hora_inicial.setter
    def meia_hora_inicial(self, n: int):
        self.data[2] = n

    @property
    def dia_final(self) -> Optional[int]:
        """
        O dia final.

        :return: O dia.
        :rtype: int | None
        """

        return self.data[3]

    @dia_final.setter
    def dia_final(self, n: int):
        self.data[3] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[4]

    @hora_final.setter
    def hora_final(self, n: int):
        self.data[4] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[5]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int):
        self.data[5] = n


class UchTonToffUnidade(Register):
    """ """

    IDENTIFIER = "UCH-TON-TOFF-UNIDADE"
    IDENTIFIER_DIGITS = 20
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
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
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica relacionada ao polinômio.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int):
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica relacionada ao polinômio.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int):
        self.data[2] = c

    @property
    def tempo_minimo_ligada(self) -> Optional[int]:
        """
        O ftempo mínimo ligada (Ton) em horas.

        :return: O flag
        :rtype: int | None
        """
        return self.data[3]

    @tempo_minimo_ligada.setter
    def tempo_minimo_ligada(self, c: int):
        self.data[3] = c

    @property
    def tempo_minimo_desligada(self) -> Optional[int]:
        """
        O ftempo mínimo desligada (Toff) em horas.

        :return: O flag
        :rtype: int | None
        """
        return self.data[4]

    @tempo_minimo_desligada.setter
    def tempo_minimo_desligada(self, c: int):
        self.data[4] = c


class UchTonToffConjunto(Register):
    """ """

    IDENTIFIER = "UCH-OPCAO-CONJUNTO"
    IDENTIFIER_DIGITS = 18
    LINE = Line(
        [
            IntegerField(),
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
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica relacionada ao polinômio.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int):
        self.data[1] = c

    @property
    def tempo_minimo_ligada(self) -> Optional[int]:
        """
        O ftempo mínimo ligada (Ton) em horas.

        :return: O flag
        :rtype: int | None
        """
        return self.data[2]

    @tempo_minimo_ligada.setter
    def tempo_minimo_ligada(self, c: int):
        self.data[2] = c

    @property
    def tempo_minimo_desligada(self) -> Optional[int]:
        """
        O ftempo mínimo desligada (Toff) em horas.

        :return: O flag
        :rtype: int | None
        """
        return self.data[3]

    @tempo_minimo_desligada.setter
    def tempo_minimo_desligada(self, c: int):
        self.data[3] = c


class UchTonToffUsina(Register):
    """ """

    IDENTIFIER = "UCH-TON-TOFF-USINA"
    IDENTIFIER_DIGITS = 18
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
    def tempo_minimo_ligada(self) -> Optional[int]:
        """
        O ftempo mínimo ligada (Ton) em horas.

        :return: O flag
        :rtype: int | None
        """
        return self.data[1]

    @tempo_minimo_ligada.setter
    def tempo_minimo_ligada(self, c: int):
        self.data[1] = c

    @property
    def tempo_minimo_desligada(self) -> Optional[int]:
        """
        O ftempo mínimo desligada (Toff) em horas.

        :return: O flag
        :rtype: int | None
        """
        return self.data[2]

    @tempo_minimo_desligada.setter
    def tempo_minimo_desligada(self, c: int):
        self.data[2] = c


class UchGminGmaxUnidade(Register):
    """ """

    IDENTIFIER = "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE"
    IDENTIFIER_DIGITS = 33
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=2),
            FloatField(decimal_digits=2),
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
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica relacionada ao polinômio.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int):
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica relacionada ao polinômio.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int):
        self.data[2] = c

    @property
    def geracao_minima_unidade(self) -> Optional[float]:
        """
        A geração mínima da unidade geradora.

        :return: A geração mínima
        :rtype: float | None
        """
        return self.data[3]

    @geracao_minima_unidade.setter
    def geracao_minima_unidade(self, c: float):
        self.data[3] = c

    @property
    def geracao_maxima_unidade(self) -> Optional[float]:
        """
        A geração máxima da unidade geradora.

        :return: A geração máxima
        :rtype: float | None
        """
        return self.data[4]

    @geracao_maxima_unidade.setter
    def geracao_maxima_unidade(self, c: float):
        self.data[4] = c


class UchQturminQturmaxUnidade(Register):
    """ """

    IDENTIFIER = "UCH-TURBINAMENTO-MINIMO-MAXIMO-UNIDADE"
    IDENTIFIER_DIGITS = 38
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=2),
            FloatField(decimal_digits=2),
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
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica relacionada ao polinômio.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int):
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica relacionada ao polinômio.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int):
        self.data[2] = c

    @property
    def turbinamento_minimo_unidade(self) -> Optional[float]:
        """
        O turbinamento mínimo da unidade geradora.

        :return: O turbinamento mínimo
        :rtype: float | None
        """
        return self.data[3]

    @turbinamento_minimo_unidade.setter
    def turbinamento_minimo_unidade(self, c: float):
        self.data[3] = c

    @property
    def turbinamento_maximo_unidade(self) -> Optional[float]:
        """
        O turbinamento máximo da unidade geradora.

        :return:  O turbinamento máximo
        :rtype: float | None
        """
        return self.data[4]

    @turbinamento_maximo_unidade.setter
    def turbinamento_maximo_unidade(self, c: float):
        self.data[4] = c


class UchCondicaoInicialUnidade(Register):
    """ """

    IDENTIFIER = "UCH-CONDICAO-INICIAL-UNIDADE"
    IDENTIFIER_DIGITS = 28
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=2),
            FloatField(decimal_digits=2),
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
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica relacionada ao polinômio.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int):
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica relacionada ao polinômio.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int):
        self.data[2] = c

    @property
    def status_inicial(self) -> Optional[int]:
        """
        O flag de status inicial da unidade geradora.

        :return: O status inicial
        :rtype: int | None
        """
        return self.data[3]

    @status_inicial.setter
    def status_inicial(self, c: int):
        self.data[3] = c

    @property
    def tempo_permanencia_unidade(self) -> Optional[int]:
        """
        O tempo de permanência da unidade geradora em horas.

        :return:  O tempo de permanência
        :rtype: int | None
        """
        return self.data[4]

    @tempo_permanencia_unidade.setter
    def tempo_permanencia_unidade(self, c: int):
        self.data[4] = c

    @property
    def geracao_inicial_unidade(self) -> Optional[float]:
        """
        A geração inicial da unidade geradora.

        :return:  A geração inicial
        :rtype: float | None
        """
        return self.data[5]

    @geracao_inicial_unidade.setter
    def geracao_inicial_unidade(self, c: float):
        self.data[5] = c

    @property
    def turbinamento_inicial_unidade(self) -> Optional[float]:
        """
        O turbinamento inicial da unidade geradora.

        :return:  O turbinamento inicial
        :rtype: float | None
        """
        return self.data[6]

    @turbinamento_inicial_unidade.setter
    def turbinamento_inicial_unidade(self, c: float):
        self.data[6] = c
