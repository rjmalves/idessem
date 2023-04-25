from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from typing import List, Dict, IO
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
from idessem.config import MAX_UG_UCT


class BlocoInitUT(Block):
    """
    Bloco de informações das condições iniciais das usinas
    termelétricas do DESSEM, existente no `operut.dat`.
    """

    BEGIN_PATTERN = r"^INIT"
    END_PATTERN = r"FIM"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(3, 0),
                LiteralField(12, 4),
                IntegerField(3, 18),
                IntegerField(2, 24),
                FloatField(10, 29, 3),
                IntegerField(5, 41),
                IntegerField(1, 48),
                IntegerField(1, 51),
                IntegerField(1, 54),
                FloatField(10, 57, 0),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoInitUT):
            return False
        bloco: BlocoInitUT = o
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        elif len(self.data) != len(o.data):
            return False
        elif not all(
            [
                isinstance(self.data[0], dict),
                isinstance(o.data[0], dict),
            ]
        ):
            return False
        elif not all(
            [
                isinstance(self.data[1], pd.DataFrame),
                isinstance(o.data[1], pd.DataFrame),
            ]
        ):
            return False
        else:
            return (self.data[0] == bloco.data[0]) and (
                self.data[1].equals(bloco.data[1])
            )

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = [
                "indice_usina",
                "indice_unidade_geradora",
                "estado",
                "geracao_inicial",
                "tempo_permanencia_estado",
                "meia_hora",
                "rampa_acionamento_desligamento",
                "titulacao_inicial",
                "inflexibilidade_titulacao",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            df = df.astype(
                {
                    "indice_usina": int,
                    "indice_unidade_geradora": int,
                    "estado": int,
                    "tempo_permanencia_estado": int,
                    "meia_hora": int,
                    "rampa_acionamento_desligamento": int,
                    "titulacao_inicial": int,
                }
            )
            df["nome_usina"] = lista_nomes
            df = df[[cols[0], "nome_usina"] + cols[1:]]
            return df

        # Salta a linha do BEGIN_PATTERN
        file.readline()

        indice_linha = 0
        comentarios: Dict[int, List[str]] = {}
        tabela = np.zeros((MAX_UG_UCT, 9))
        lista_nomes: List[str] = []
        while True:
            linha = file.readline()
            # Confere se terminou o bloco
            if BlocoInitUT.END_PATTERN in linha[:4]:
                tabela = tabela[:indice_linha, :]
                df = converte_tabela_em_df()
                self.data = [comentarios, df]
                break
            # Confere se a linha é de comentário
            if linha[0] == "&":
                if comentarios.get(indice_linha) is None:
                    comentarios[indice_linha] = []
                comentarios[indice_linha].append(linha)
            else:
                # Senão, lê como dado
                dados_linha = self.__linha.read(linha)
                tabela[indice_linha, :] = [dados_linha[0]] + dados_linha[2:]
                lista_nomes.append(dados_linha[1])
                indice_linha += 1

    # Override
    def write(self, file: IO, *args, **kwargs):
        if not isinstance(self.data, list):
            raise ValueError("Dados do operut.dat não foram lidos com sucesso")

        file.write("INIT\n")
        comentarios = self.data[0]
        df = self.data[1]
        for indice, linha in df.iterrows():
            linhas_comentario = comentarios.get(indice)
            if linhas_comentario is not None:
                for linha_comentario in linhas_comentario:
                    file.write(linha_comentario)
            file.write(self.__linha.write(linha.tolist()))
        file.write(BlocoInitUT.END_PATTERN + "\n")


class BlocoOper(Block):
    """
    Bloco de informações dos limites e condições operativas das unidades
    termelétricas do DESSEM, existente no `operut.dat`.
    """

    BEGIN_PATTERN = r"^OPER"
    END_PATTERN = r"FIM"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(3, 0),
                LiteralField(12, 4),
                IntegerField(2, 17),
                IntegerField(2, 20),
                IntegerField(2, 23),
                IntegerField(1, 26),
                IntegerField(2, 28),
                IntegerField(2, 31),
                IntegerField(1, 34),
                FloatField(10, 36, 2),
                FloatField(10, 46, 2),
                FloatField(10, 56, 2),
            ]
        )
        self.__linha_F = Line(
            [
                IntegerField(3, 0),
                LiteralField(12, 4),
                IntegerField(2, 17),
                IntegerField(2, 20),
                IntegerField(2, 23),
                IntegerField(1, 26),
                LiteralField(2, 28),
                IntegerField(2, 31),
                IntegerField(1, 34),
                FloatField(10, 36, 2),
                FloatField(10, 46, 2),
                FloatField(10, 56, 2),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoOper):
            return False
        bloco: BlocoOper = o
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        elif len(self.data) != len(o.data):
            return False
        elif not all(
            [
                isinstance(self.data[0], dict),
                isinstance(o.data[0], dict),
            ]
        ):
            return False
        elif not all(
            [
                isinstance(self.data[1], pd.DataFrame),
                isinstance(o.data[1], pd.DataFrame),
            ]
        ):
            return False
        else:
            return (self.data[0] == bloco.data[0]) and (
                self.data[1].equals(bloco.data[1])
            )

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = [
                "indice_usina",
                "indice_unidade_geradora",
                "dia_inicial",
                "hora_inicial",
                "meia_hora_inicial",
                "dia_final",
                "hora_final",
                "meia_hora_final",
                "geracao_minima",
                "geracao_maxima",
                "custo",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            df = df.astype(
                {
                    "indice_usina": int,
                    "indice_unidade_geradora": int,
                    "dia_inicial": int,
                    "hora_inicial": int,
                    "meia_hora_inicial": int,
                }
            )
            df["nome_usina"] = lista_nomes
            df = df[[cols[0], "nome_usina"] + cols[1:]]
            return df

        # Salta a linha do BEGIN_PATTERN
        file.readline()

        indice_linha = 0
        comentarios: Dict[int, List[str]] = {}
        tabela = np.zeros((MAX_UG_UCT, 11))
        lista_nomes: List[str] = []
        while True:
            linha = file.readline()
            # Confere se terminou o bloco
            if BlocoOper.END_PATTERN in linha[:4]:
                tabela = tabela[:indice_linha, :]
                df = converte_tabela_em_df()
                self.data = [comentarios, df]
                break
            # Confere se a linha é de comentário
            if linha[0] == "&":
                if comentarios.get(indice_linha) is None:
                    comentarios[indice_linha] = []
                comentarios[indice_linha].append(linha)
            else:
                # Senão, lê como dado
                dados_linha = self.__linha.read(linha)
                tabela[indice_linha, :] = [dados_linha[0]] + dados_linha[2:]
                lista_nomes.append(dados_linha[1])
                indice_linha += 1

    # Override
    def write(self, file: IO, *args, **kwargs):
        if not isinstance(self.data, list):
            raise ValueError("Dados do operut.dat não foram lidos com sucesso")

        file.write("OPER\n")
        comentarios = self.data[0]
        df = self.data[1]
        for indice, linha in df.iterrows():
            linha_write = linha.tolist()
            linhas_comentario = comentarios.get(indice)
            if linhas_comentario is not None:
                for linha_comentario in linhas_comentario:
                    file.write(linha_comentario)
            # Trata coluna de data final string
            if np.isnan(linha_write[6]):
                linha_write[6] = "F"
                file.write(self.__linha_F.write(linha_write))
            else:
                file.write(self.__linha.write(linha_write))
        file.write(BlocoOper.END_PATTERN + "\n")


class BlocoUctPar(Block):
    """
    Flag para definir o número de núcleos para processamento paralelo no
    DESSEM, existente no `operut.dat`
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
    DESSEM, existente no `operut.dat`
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
    DESSEM, existente no `operut.dat`
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
    hidráulica no DESSEM, existente no `operut.dat`
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
    de cálculo do CMO no DESSEM, existente no `operut.dat`
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
    CPLEX no DESSEM, existente no `operut.dat`
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
    no DESSEM, existente no `operut.dat`
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
    e Fixação de Variáveis de Status no DESSEM, existente no `operut.dat`
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
    existente no `operut.dat`
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
    no DESSEM, existente no `operut.dat`
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
    no DESSEM, existente no `operut.dat`
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
    por pontos interiores no DESSEM, existente no `operut.dat`
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
    no DESSEM, existente no `operut.dat`
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
    no DESSEM, existente no `operut.dat`
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
