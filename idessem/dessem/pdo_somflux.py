import warnings

# Para compatibilidade - até versão 1.0.0
from os.path import join

from idessem.dessem.modelos.arquivos.arquivocsv import (
    ArquivoCSV,
    DataEstudo,
    VersaoModelo,
)
from idessem.dessem.modelos.pdo_somflux import TabelaPdoSomFlux


class PdoSomFlux(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as restrições de somatório de fluxo.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_SOMFLUX.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoSomFlux]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="PDO_SOMFLUX.DAT") -> "PdoSomFlux":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referentes as restrições de somatório
        de fluxos.

        - estagio (`int`)
        - indice_restricao (`int`)
        - nome_patamar (`str`)
        - flag_V (`str`)
        - flag_L (`str`)
        - codigo_restricao (`int`)
        - nome_restricao (`str`)
        - codigo_barra_de (`int`)
        - codigo_barra_para (`int`)
        - indice_circuito (`int`)
        - valor (`float`)
        - limite_inferior (`float`)
        - limite_superior (`float`)
        - multiplicador (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
