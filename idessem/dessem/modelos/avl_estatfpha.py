from cfinterface.components.block import Block
from typing import List, IO
import pandas as pd  # type: ignore


class BlocoDesvios(Block):
    """
    Bloco com as estatísticas de desvios da função de produção do
    DESSEM, existente no `AVL_ESTATFPHA.DAT`.
    """

    BEGIN_PATTERN = r"DESVIO MEDIO \(MW\):"
    END_PATTERN = "DISTRIBUICOES ACUMULADAS TOTAL E POR PERIODO"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDesvios):
            return False
        bloco: BlocoDesvios = o
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
            valor_linha = float(dados_linha[1])
            variavel.append(dados_linha[0].strip())
            valores.append(valor_linha)
