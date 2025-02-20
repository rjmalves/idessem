from typing import IO, List

import pandas as pd  # type: ignore
from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.section import Section


class BlocoCasosBase(Section):
    """
    Bloco com os arquivos dos casos base.
    """

    __slots__ = ["__linha", "__comentarios"]

    FIM_BLOCO = "99999"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [IntegerField(5, 0), LiteralField(12, 5), LiteralField(40, 19)]
        )
        self.__comentarios: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCasosBase):
            return False
        bloco: BlocoCasosBase = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    def read(self, file: IO, *args, **kwargs):

        def extrai_coluna_de_listas(
            listas: List[list],
            coluna: int,
        ) -> list:
            return [lista[coluna] for lista in listas]

        def transforma_em_df(dados: list, mapa: dict) -> pd.DataFrame | None:
            if len(dados) == 0:
                return None
            dados_df = {}
            for key, value in mapa.items():
                col = extrai_coluna_de_listas(dados, value)
                dados_df[key] = col
            return pd.DataFrame(data=dados_df)

        mapa = {"indice_caso_base": 0, "nome_caso_base": 1, "arquivo": 2}

        # Para cada caso, lê e processa as informações
        dados: List[list] = []
        while True:
            linha = file.readline()
            # Converte para df
            if BlocoCasosBase.FIM_BLOCO in linha[:6] or len(linha) < 1:
                self.data = transforma_em_df(dados, mapa)
                break
            # Armazena linhas de comentarios
            if "(" == linha[0]:
                self.__comentarios.append(linha)
            else:
                dados.append(self.__linha.read(linha))

    # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__comentarios:
            file.write(linha)
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("Dados do desselet.dat não foram lidos com sucesso")
        for _, lin in self.data.iterrows():
            linha_escrita = lin.tolist()
            file.write(self.__linha.write(linha_escrita))
        file.write(BlocoCasosBase.FIM_BLOCO + "\n")


class BlocoCasosModificacao(Section):
    """
    Bloco com os arquivos de modificação do caso base por estágio.
    """

    __slots__ = ["__linha", "__comentarios"]

    FIM_BLOCO = "99999"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(4, 0),
                LiteralField(14, 4),
                IntegerField(4, 18),
                IntegerField(2, 22),
                IntegerField(2, 24),
                IntegerField(2, 27),
                IntegerField(2, 30),
                FloatField(5, 32, 1),
                IntegerField(4, 40),
                LiteralField(40, 45),
            ]
        )
        self.__comentarios: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCasosModificacao):
            return False
        bloco: BlocoCasosModificacao = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

        # Override

    def read(self, file: IO, *args, **kwargs):

        def extrai_coluna_de_listas(
            listas: List[list],
            coluna: int,
        ) -> list:
            return [lista[coluna] for lista in listas]

        def transforma_em_df(dados: list, mapa: dict) -> pd.DataFrame | None:
            if len(dados) == 0:
                return None
            dados_df = {}
            for key, value in mapa.items():
                col = extrai_coluna_de_listas(dados, value)
                dados_df[key] = col
            return pd.DataFrame(data=dados_df)

        mapa = {
            "codigo_estagio": 0,
            "nome_estagio": 1,
            "ano": 2,
            "mes": 3,
            "dia": 4,
            "hora": 5,
            "minuto": 6,
            "duracao_estagio": 7,
            "indice_caso_base": 8,
            "arquivo": 9,
        }

        # Para cada caso, lê e processa as informações
        dados: List[list] = []
        while True:
            linha = file.readline()
            # Converte para df
            if BlocoCasosModificacao.FIM_BLOCO in linha[:6] or len(linha) < 1:
                self.data = transforma_em_df(dados, mapa)
                break
            # Armazena linhas de comentarios
            if "(" == linha[0]:
                self.__comentarios.append(linha)
            else:
                dados.append(self.__linha.read(linha))

    # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__comentarios:
            file.write(linha)
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("Dados do desselet.dat não foram lidos com sucesso")
        for _, lin in self.data.iterrows():
            linha_escrita = lin.tolist()
            file.write(self.__linha.write(linha_escrita))
        file.write(BlocoCasosModificacao.FIM_BLOCO + "\n")
