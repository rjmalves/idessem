from idessem.dessem.modelos.pdo_eco_usih import (
    TabelaPdoEcoUsih,
    TabelaPdoEcoUsih190402,
    TabelaPdoEcoUsih190301,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoEcoUsih(ArquivoCSV):
    """
    Armazena os dados de eco referentes as usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_USIH.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoUsih]
    VERSIONS = {
        "19.3.1": [VersaoModelo, DataEstudo, TabelaPdoEcoUsih190301],
        "19.4.2": [VersaoModelo, DataEstudo, TabelaPdoEcoUsih190402],
        "20.3": [VersaoModelo, DataEstudo, TabelaPdoEcoUsih],
    }
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a caracaterísticas das usinas
        hidrelétricas e topologia das cascatas.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
        - codigo_usina_jusante (`int`)
        - codigo_usina_desvio (`int`)
        - codigo_usina_jusante_earm (`int`)
        - estagio_inicial (`int`)
        - volume_morto_inicial_hm3 (`float`)
        - volume_morto_inicial_percentual (`float`)
        - volume_util_inicial_hm3 (`float`)
        - volume_util_inicial_percentual (`float`)
        - volume_armazenado_minimo_hm3 (`float`)
        - volume_armazenado_maximo_hm3 (`float`)
        - volume_soleira_vertedouro_hm3 (`float`)
        - volume_soleira_vertedouro_util_percentual (`float`)
        - volume_soleira_desvio_hm3 (`float`)
        - volume_soleira_desvio_util_percentual (`float`)
        - volume_referencia_hm3 (`float`)
        - tipo_reservatorio (`str`)
        - tipo_regularizacao (`str`)
        - flag_evaporacao (`int`)
        - numero_conjuntos (`int`)
        - produtibilidade_especifica (`float`)
        - tipo_perdas (`str`)
        - perdas_hidraulicas (`float`)
        - canal_fuga_medio (`float`)
        - influencia_vertimento_canal_fuga (`int`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
