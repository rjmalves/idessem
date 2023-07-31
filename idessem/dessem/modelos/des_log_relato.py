from cfinterface.components.block import Block
from typing import List, IO
import pandas as pd  # type: ignore
from datetime import timedelta


class BlocoVariaveisOtimizacao(Block):
    """
    Bloco com variáveis obtidas da otimização do
    DESSEM, existente no `DES_LOG_RELATO.DAT`.
    """

    BEGIN_PATTERN = "Funcao objetivo do Problema Linear"
    END_PATTERN = "----------------"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoVariaveisOtimizacao):
            return False
        bloco: BlocoVariaveisOtimizacao = o
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
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(data={"variavel": variavel, "valor": valores})
            return df

        variavel: List[str] = []
        valores: List[float] = []
        while True:
            linha = file.readline()
            if self.ends(linha):
                self.data = converte_tabela_em_df()
                break
            if len(linha) < 5:
                continue
            dados_linha = linha.split(":")
            valor_linha = float(
                dados_linha[1].split("(")[0]
                if "(" in dados_linha[1]
                else dados_linha[1]
            )
            variavel.append(dados_linha[0].strip())
            valores.append(valor_linha)


class BlocoTempoProcessamento(Block):
    """
    Bloco com o tempo de processamento do modelo
    DESSEM, existente no `DES_LOG_RELATO.DAT`.
    """

    BEGIN_PATTERN = "  TEMPO DE PROCESSAMENTO DO MODELO DESSEM"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoTempoProcessamento):
            return False
        if not all([type(self.data) is timedelta, type(o.data) is timedelta]):
            return False
        else:
            return self.data == o.data

    # Override
    def read(self, file: IO, *args, **kwargs):
        linha = file.readline()
        dados = linha.split(":")
        self.data = timedelta(
            hours=int(dados[1]), minutes=int(dados[2]), seconds=int(dados[3])
        )
