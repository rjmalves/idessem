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

    BEGIN_PATTERN = r"INIT"
    END_PATTERN = r"FIM"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(2, 1),
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
    def read(self, file: IO):
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
    def write(self, file: IO):
        if not isinstance(self.data, list):
            raise ValueError("Dados do operut.dat não foram lidos com sucesso")

        file.write(BlocoInitUT.BEGIN_PATTERN + "\n")
        comentarios = self.data[0]
        df = self.data[1]
        for indice, linha in df.iterrows():
            linhas_comentario = comentarios.get(indice)
            if linhas_comentario is not None:
                for linha_comentario in linhas_comentario:
                    file.write(linha_comentario)
            file.write(self.__linha.write(linha.tolist()))
        file.write(BlocoInitUT.END_PATTERN + "\n")
