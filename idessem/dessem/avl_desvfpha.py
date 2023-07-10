from idessem.dessem.modelos.avl_desvfpha import (
    TabelaAvlDesvFpha,
    TabelaAvlDesvFpha190300,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class AvlDesvFpha(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos desvios da função de produção.

    Essa classe lida com as informações de saída fornecidas pelo arquivo AVL_DESVFPHA.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaAvlDesvFpha]
    VERSIONS = {
        "19.3": [VersaoModelo, DataEstudo, TabelaAvlDesvFpha190300],
        "19.4.2": [VersaoModelo, DataEstudo, TabelaAvlDesvFpha],
    }
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="AVL_DESVFPHA.DAT"
    ) -> "AvlDesvFpha":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos desvios da função de produção.

        - estagio (`int`)
        - indice_usina (`int`)
        - nome_usina (`str`)
        - volume_medio_hm3 (`float`)
        - volume_medio_percentual (`float`)
        - vazao_incremental_m3s (`float`)
        - vazao_turbinada_m3s (`float`)
        - vazao_vertida_m3s (`float`)
        - vazao_jusante_m3s (`float`)
        - vazao_lateral_usina_m3s (`float`)
        - vazao_lateral_posto_m3s (`float`)
        - altura_jusante (`float`)
        - altura_montante (`float`)
        - produtibilidade_especifica (`float`)
        - tipo_perdas (`str`)
        - perdas_hidraulicas (`float`)
        - influencia_vertimento_canal_fuga (`int`)
        - afogamento_canal_fuga (`int`)
        - potencia_instalada (`float`)
        - geracao_fph (`float`)
        - geracao_pl (`float`)
        - geracao_fpha (`float`)
        - desvio_absoluto_fph_pl (`float`)
        - desvio_percentual_fph_pl (`float`)
        - desvio_absoluto_fph_fpha (`float`)
        - desvio_percentual_fph_fpha (`float`)


        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
