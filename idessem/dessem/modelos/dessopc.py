from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from typing import IO


class BlocoUctPar(Block):

    """
    Flag para definir o número de núcleos para processamento paralelo no
    DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^UCTPAR"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(6, 0),
                IntegerField(2, 7),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoUctPar):
            return False
        bloco: BlocoUctPar = o
        if not all(
            [
                isinstance(self.data, int),
                isinstance(o.data, int),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["UCTPAR", self.data]))


class BlocoUcTerm(Block):
    """
    Flag para habilitar o unit commitment térmico e definir estratégia geral
    de consideração das restrições de UCT na resolução do problema no
    DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^UCTERM"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(6, 0),
                IntegerField(1, 7),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoUcTerm):
            return False
        bloco: BlocoUcTerm = o
        if not all(
            [
                isinstance(self.data, int),
                isinstance(o.data, int),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["UCTERM", self.data]))


class BlocoPint(Block):
    """
    Flag para ativar a metodologia de Pontos Interiores no
    DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^PINT"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([LiteralField(4, 0)])

    def __eq__(self, o: object) -> bool:
        return isinstance(o, BlocoPint)

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[0]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["PINT"]))


class BlocoRegraNPTV(Block):
    """
    Flag para definição de valores default para a função de produção
    hidráulica no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^REGRANPTV"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(9, 0),
                IntegerField(1, 10),
                IntegerField(2, 14),
                IntegerField(2, 18),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoRegraNPTV):
            return False
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        else:
            return all([x == y for x, y in zip(self.data, o.data)])

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1:]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["REGRANPTV"] + self.data))


class BlocoAvlCmo(Block):
    """
    Flag para habilitar a impressão dos arquivos de memória
    de cálculo do CMO no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^AVLCMO"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(6, 0),
                IntegerField(1, 7),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoAvlCmo):
            return False
        bloco: BlocoAvlCmo = o
        if not all(
            [
                isinstance(self.data, int),
                isinstance(o.data, int),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["AVLCMO", self.data]))


class BlocoCplexLog(Block):
    """
    Flag para habilitar a impressão do arquivo de log do solver
    CPLEX no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^CPLEXLOG"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([LiteralField(8, 0)])

    def __eq__(self, o: object) -> bool:
        return isinstance(o, BlocoCplexLog)

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[0]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["CPLEXLOG"]))


class BlocoUctBusLoc(Block):
    """
    Flag para habilitar a restrição de busca local
    no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^UCTBUSLOC"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([LiteralField(9, 0)])

    def __eq__(self, o: object) -> bool:
        return isinstance(o, BlocoUctBusLoc)

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[0]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["UCTBUSLOC"]))


class BlocoUctHeurFp(Block):
    """
    Flag para ativar a metodologia Feasibility Pump com Busca Local
    e Fixação de Variáveis de Status no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^UCTHEURFP"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(9, 0),
                IntegerField(3, 10),
                IntegerField(3, 14),
                IntegerField(1, 18),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoUctHeurFp):
            return False
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        else:
            return all([x == y for x, y in zip(self.data, o.data)])

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1:]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["UCTHEURFP"] + self.data))


class BlocoConstDados(Block):
    """
    Flag para ativar a consistência de dados no DESSEM,
    existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^CONSTDADOS"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(10, 0),
                IntegerField(1, 11),
                IntegerField(1, 14),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoConstDados):
            return False
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        else:
            return all([x == y for x, y in zip(self.data, o.data)])

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1:]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["CONSTDADOS"] + self.data))


class BlocoAjusteFcf(Block):
    """
    Flag para habilitar o ajuste da função de custo futuro
    no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^AJUSTEFCF"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(9, 0),
                IntegerField(1, 10),
                IntegerField(1, 12),
                IntegerField(1, 14),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoAjusteFcf):
            return False
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        else:
            return all([x == y for x, y in zip(self.data, o.data)])

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1:]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["AJUSTEFCF"] + self.data))


class BlocoTolerIlh(Block):
    """
    Flag para ativar tolerância nas equações de demanda por ilha
    no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^TOLERILH"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(8, 0),
                IntegerField(1, 9),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoTolerIlh):
            return False
        bloco: BlocoTolerIlh = o
        if not all(
            [
                isinstance(self.data, int),
                isinstance(o.data, int),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["TOLERILH", self.data]))


class BlocoCrossover(Block):
    """
    Flag para ativar o crossover após a resolução de um PL
    por pontos interiores no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^CROSSOVER"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(9, 0),
                IntegerField(1, 10),
                IntegerField(1, 12),
                IntegerField(1, 14),
                IntegerField(1, 16),
                IntegerField(1, 18),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCrossover):
            return False
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        else:
            return all([x == y for x, y in zip(self.data, o.data)])

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1:]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["CROSSOVER"] + self.data))


class BlocoEngolimento(Block):
    """
    Flag para habilitar a consideração do engolimento máximo
    no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^ENGOLIMENTO"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(11, 0),
                IntegerField(1, 12),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoEngolimento):
            return False
        bloco: BlocoEngolimento = o
        if not all(
            [
                isinstance(self.data, int),
                isinstance(o.data, int),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["ENGOLIMENTO", self.data]))


class BlocoTrataInviabIlha(Block):
    """
    Flag para ativação do processo de tratamento de
    inviabilidades nas ilhas da rede elétrica
    no DESSEM, existente no `dessopc.dat`
    """

    BEGIN_PATTERN = r"^TRATA_INVIAB_ILHA"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                LiteralField(17, 0),
                IntegerField(1, 19),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoTrataInviabIlha):
            return False
        bloco: BlocoTrataInviabIlha = o
        if not all(
            [
                isinstance(self.data, int),
                isinstance(o.data, int),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        self.data = self.__linha.read(file.readline())[1]

    def write(self, file: IO, *args, **kwargs):
        file.write(self.__linha.write(["TRATA_INVIAB_ILHA", self.data]))
