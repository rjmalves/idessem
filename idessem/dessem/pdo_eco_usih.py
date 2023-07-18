from idessem.dessem.modelos.pdo_eco_usih import (
    TabelaPdoEcoUsih,
    TabelaPdoEcoUsih190301,
)
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoEcoUsih(ArquivoCSV):
    """
    Armazena os dados de eco referentes as usinas hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_ECO_USIH.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEcoUsih]
    VERSIONS = {
        "19.3.1": [VersaoModelo, DataEstudo, TabelaPdoEcoUsih190301],
        "19.4.2": [VersaoModelo, DataEstudo, TabelaPdoEcoUsih],
    }
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_ECO_USIH.DAT"
    ) -> "PdoEcoUsih":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a caracaterísticas das usinas
        hidrelétricas e topologia das cascatas.

        - indice_usina (`int`)
        - nome_usina (`str`)
        - submercado (`str`)
        - indice_usina_jusante (`int`)
        - indice_usina_desvio (`int`)
        - indice_usina_jusante_earm (`int`)
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
