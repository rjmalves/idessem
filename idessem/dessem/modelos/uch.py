from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField

from typing import Optional


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
    def considera_uch(self, c: int) -> None:
        self.data[0] = c


class UchOpcaoPadraoUsina(Register):
    """ """

    IDENTIFIER = "UCH-OPCAO-PADRAO-USINA"
    IDENTIFIER_DIGITS = 22
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
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
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
    def considera_uch_usina(self, c: int) -> None:
        self.data[1] = c

    @property
    def tipo_agregacao(self) -> Optional[int]:
        """
        Identificação do nível de agregação adotado na
        modelagem do UCH:

        1: Unidade Geradora
        2: Agregado por Conjunto de Máquinas
        3: Agregado por Usina.

        :return: Tipo da agregação
        :rtype: int | None
        """
        return self.data[2]

    @tipo_agregacao.setter
    def tipo_agregacao(self, c: int) -> None:
        self.data[2] = c


class UchPadraoData(Register):
    """ """

    IDENTIFIER = "UCH-PADRAO-DATA"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
        ],
        delimiter=";",
    )

    @property
    def dia_final(self) -> Optional[int]:
        """
        O dia final.

        :return: O dia.
        :rtype: int | None
        """

        return self.data[0]

    @dia_final.setter
    def dia_final(self, n: int) -> None:
        self.data[0] = n

    @property
    def hora_final(self) -> Optional[int]:
        """
        A hora final.

        :return: A hora.
        :rtype: int | None
        """
        return self.data[1]

    @hora_final.setter
    def hora_final(self, n: int) -> None:
        self.data[1] = n

    @property
    def meia_hora_final(self) -> Optional[int]:
        """
        A meia-hora final.

        :return: A meia-hora.
        :rtype: int | None
        """
        return self.data[2]

    @meia_hora_final.setter
    def meia_hora_final(self, n: int) -> None:
        self.data[2] = n


class UchOpcaoVazioUnidade(Register):
    """ """

    IDENTIFIER = "UCH-OPCAO-VAZIO-UNIDADE"
    IDENTIFIER_DIGITS = 23
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
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
        self.data[2] = c

    @property
    def considera_operacao_vazio(self) -> Optional[int]:
        """
        O flag se a unidade considerará operação a vazio.

        :return: O flag
        :rtype: int | None
        """
        return self.data[3]

    @considera_operacao_vazio.setter
    def considera_operacao_vazio(self, c: int) -> None:
        self.data[3] = c


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
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
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
    def tempo_minimo_ligada(self, c: int) -> None:
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
    def tempo_minimo_desligada(self, c: int) -> None:
        self.data[4] = c


class UchGminGmaxUnidade(Register):
    """ """

    IDENTIFIER = "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE"
    IDENTIFIER_DIGITS = 33
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=3),
            FloatField(decimal_digits=3),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
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
    def geracao_minima_unidade(self, c: float) -> None:
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
    def geracao_maxima_unidade(self, c: float) -> None:
        self.data[4] = c


class UchGminGmaxConjunto(Register):
    """ """

    IDENTIFIER = "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO"
    IDENTIFIER_DIGITS = 34
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=3),
            FloatField(decimal_digits=3),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def geracao_minima_conjunto(self) -> Optional[float]:
        """
        A geração mínima do conjunto de máquinas.

        :return: A geração mínima
        :rtype: float | None
        """
        return self.data[2]

    @geracao_minima_conjunto.setter
    def geracao_minima_conjunto(self, c: float) -> None:
        self.data[2] = c

    @property
    def geracao_maxima_conjunto(self) -> Optional[float]:
        """
        A geração máxima do conjunto de máquinas.

        :return: A geração máxima
        :rtype: float | None
        """
        return self.data[3]

    @geracao_maxima_conjunto.setter
    def geracao_maxima_conjunto(self, c: float) -> None:
        self.data[3] = c


class UchGminGmaxUsina(Register):
    """ """

    IDENTIFIER = "UCH-GERACAO-MINIMA-MAXIMA-USINA"
    IDENTIFIER_DIGITS = 31
    LINE = Line(
        [
            IntegerField(),
            FloatField(decimal_digits=3),
            FloatField(decimal_digits=3),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def geracao_minima_usina(self) -> Optional[float]:
        """
        A geração mínima da usina hidrelétrica.

        :return: A geração mínima
        :rtype: float | None
        """
        return self.data[1]

    @geracao_minima_usina.setter
    def geracao_minima_usina(self, c: float) -> None:
        self.data[1] = c

    @property
    def geracao_maxima_usina(self) -> Optional[float]:
        """
        A geração máxima da usina hidrelétrica.

        :return: A geração máxima
        :rtype: float | None
        """
        return self.data[2]

    @geracao_maxima_usina.setter
    def geracao_maxima_usina(self, c: float) -> None:
        self.data[2] = c


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
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
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
    def status_inicial(self, c: int) -> None:
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
    def tempo_permanencia_unidade(self, c: int) -> None:
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
    def geracao_inicial_unidade(self, c: float) -> None:
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
    def turbinamento_inicial_unidade(self, c: float) -> None:
        self.data[6] = c


class UchConsumoAguaVazioUnidade(Register):
    """ """

    IDENTIFIER = "UCH-CONSUMO-AGUA-VAZIO-UNIDADE"
    IDENTIFIER_DIGITS = 30
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=2),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
        self.data[2] = c

    @property
    def consumo_agua(self) -> Optional[float]:
        """
        O consumo de água durante a operação em vazio (m³/s).

        :return: O consumo
        :rtype: float | None
        """
        return self.data[3]

    @consumo_agua.setter
    def consumo_agua(self, c: float) -> None:
        self.data[3] = c


class UchLimiteMudancaStatusVazioUnidade(Register):
    """ """

    IDENTIFIER = "UCH-LIMITE-MUDANCA-STATUS-VAZIO-UNIDADE"
    IDENTIFIER_DIGITS = 39
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
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
        self.data[2] = c

    @property
    def limite_maximo_mudancas(self) -> Optional[int]:
        """
        O limite máximo de mudanças de status para operar em vazio.

        :return: O limite
        :rtype: int | None
        """
        return self.data[3]

    @limite_maximo_mudancas.setter
    def limite_maximo_mudancas(self, c: int) -> None:
        self.data[3] = c


class UchCustoPartidaUnidade(Register):
    """ """

    IDENTIFIER = "UCH-CUSTO-PARTIDA-UNIDADE"
    IDENTIFIER_DIGITS = 25
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=2),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
        self.data[2] = c

    @property
    def custo_partida(self) -> Optional[float]:
        """
        O custo de partida para acionamento (R$).

        :return: O custo
        :rtype: float | None
        """
        return self.data[3]

    @custo_partida.setter
    def custo_partida(self, c: float) -> None:
        self.data[3] = c


class UchCustoPartidaVazioUnidade(Register):
    """ """

    IDENTIFIER = "UCH-CUSTO-PARTIDA-VAZIO-UNIDADE"
    IDENTIFIER_DIGITS = 31
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=2),
        ],
        delimiter=";",
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina hidrelétrica.

        :return: O código da usina
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_conjunto(self) -> Optional[int]:
        """
        O código do conjunto da usina hidrelétrica.

        :return: O código do conjunto
        :rtype: int | None
        """
        return self.data[1]

    @codigo_conjunto.setter
    def codigo_conjunto(self, c: int) -> None:
        self.data[1] = c

    @property
    def codigo_unidade(self) -> Optional[int]:
        """
        O código da unidade geradora do conjunto da usina
        hidrelétrica.

        :return: O código da unidade
        :rtype: int | None
        """
        return self.data[2]

    @codigo_unidade.setter
    def codigo_unidade(self, c: int) -> None:
        self.data[2] = c

    @property
    def custo_partida(self) -> Optional[float]:
        """
        O custo de partida (transição) de desligado para vazio (R$).

        :return: O custo
        :rtype: float | None
        """
        return self.data[3]

    @custo_partida.setter
    def custo_partida(self, c: float) -> None:
        self.data[3] = c
