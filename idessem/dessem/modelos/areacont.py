from typing import IO, Dict, List

import pandas as pd  # type: ignore
from cfinterface.components.block import Block
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField


class BlocoArea(Block):
    """
    Bloco de informações de definição das áreas de controle
    do DESSEM, existente no `areacont.dat`.
    """

    BEGIN_PATTERN = r"^AREA"
    END_PATTERN = r"FIM"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(3, 0),
                LiteralField(40, 9),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoArea):
            return False
        bloco: BlocoArea = o
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

    def read(self, file: IO, *args, **kwargs):

        def _monta_df(dados: dict, cols: list) -> pd.DataFrame:
            return pd.DataFrame(data=dados, columns=cols)

        cols = [
            "codigo_area",
            "nome_area",
        ]

        # Salta a linha do BEGIN_PATTERN
        linha = file.readline()
        indice_linha = 0
        comentarios: Dict[int, List[str]] = {}
        dados: Dict[str, List] = {c: [] for c in cols}
        while True:
            linha = file.readline()

            # Confere se terminou o bloco
            if BlocoArea.END_PATTERN in linha[:4]:
                df = _monta_df(dados, cols)
                self.data = [comentarios, df]
                break
            # Confere se a linha é de comentário
            if linha[0] == "&":
                if comentarios.get(indice_linha) is None:
                    comentarios[indice_linha] = []
                comentarios[indice_linha].append(linha)
            else:
                # Senão, lê como dado/tabela
                dados_linha = self.__linha.read(linha)
                indice_linha += 1
                for i, c in enumerate(cols):
                    dados[c].append(dados_linha[i])
                    

    # Override
    def write(self, file: IO, *args, **kwargs):
        if not isinstance(self.data, list):
            raise ValueError("Dados do areacont.dat não foram lidos com sucesso")

        file.write("AREA\n")
        comentarios = self.data[0]
        df = self.data[1]
        for indice, linha in df.iterrows():
            linhas_comentario = comentarios.get(indice)
            if linhas_comentario is not None:
                for linha_comentario in linhas_comentario:
                    file.write(linha_comentario)
            file.write(self.__linha.write(linha.tolist()))
        file.write(BlocoArea.END_PATTERN + "\n")


class BlocoUsina(Block):
    """
    Bloco de informações das usinas que compõem cada área de controle
    do DESSEM, existente no `areacont.dat`.
    """

    BEGIN_PATTERN = r"^USINA"
    END_PATTERN = r"FIM"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(3, 0),
                IntegerField(1, 4),
                LiteralField(1, 7),
                LiteralField(3, 9),
                LiteralField(40, 14),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoUsina):
            return False
        bloco: BlocoUsina = o
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

        def _monta_df(dados: dict, cols: list) -> pd.DataFrame:
            return pd.DataFrame(data=dados, columns=cols)

        cols = [
            "codigo_area",
            "codigo_conjunto",
            "tipo_componente",
            "codigo_componente",
            "nome_componente",
        ]

        # Salta a linha do BEGIN_PATTERN
        linha = file.readline()
        indice_linha = 0
        comentarios: Dict[int, List[str]] = {}
        dados: Dict[str, List] = {c: [] for c in cols}
        while True:
            linha = file.readline()

            # Confere se terminou o bloco
            if BlocoArea.END_PATTERN in linha[:4]:
                df = _monta_df(dados, cols)
                self.data = [comentarios, df]
                break
            # Confere se a linha é de comentário
            if linha[0] == "&":
                if comentarios.get(indice_linha) is None:
                    comentarios[indice_linha] = []
                comentarios[indice_linha].append(linha)
            else:
                # Senão, lê como dado/tabela
                dados_linha = self.__linha.read(linha)
                indice_linha += 1
                for i, c in enumerate(cols):
                    dados[c].append(dados_linha[i])
                    

    # Override
    def write(self, file: IO, *args, **kwargs):
        if not isinstance(self.data, list):
            raise ValueError("Dados do areacont.dat não foram lidos com sucesso")

        file.write("USINA\n")
        comentarios = self.data[0]
        df = self.data[1]
        for indice, linha in df.iterrows():
            linha_write = linha.tolist()
            linhas_comentario = comentarios.get(indice)
            if linhas_comentario is not None:
                for linha_comentario in linhas_comentario:
                    file.write(linha_comentario)
            file.write(self.__linha.write(linha_write))
        file.write(BlocoUsina.END_PATTERN + "\n")
