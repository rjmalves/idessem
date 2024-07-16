from idessem.dessem.modelos.pdo_oper_tviag_calha import TabelaPdoOperTviagCalha
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoOperTviagCalha(ArquivoCSV):
    """
    Armazena os dados das saídas referentes a operação dos volumes das usinas hidráulicas
    na calha do rio no fim do horizonte do estudo.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_OPER_TVIAG_CALHA.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoOperTviagCalha]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_HIDR.DAT"
    ) -> "PdoOperTviagCalha":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação dos volumes na calha do rio
        no fim do horizonte de estudo.

        - estagio (`int`)
        - duracao (`float`)
        - codigo_usina_montante (`int`)
        - nome_usina_montante (`str`)
        - tipo_elemento_jusante (`str`)
        - codigo_elemento_jusante (`int`)
        - nome_elemento_jusante (`str`)
        - tempo_viagem (`float`)
        - tipo_tempo_viagem (`str`)
        - tempo_restante (`float`)
        - percentual_volume_calha (`float`)
        - volume_calha_hm3 (`float`)


        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
