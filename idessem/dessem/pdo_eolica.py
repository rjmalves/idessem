from idessem.dessem.modelos.pdo_eolica import TabelaPdoEolica
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoEolica(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as usinas renovaveis.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_EOLICA.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoEolica]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_EOLICA.DAT"
    ) -> "PdoEolica":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das usinas renováveis.

        - estagio (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - barra (`int`)
        - submercado (`str`)
        - potencia (`float`)
        - fator_de_capacidade (`float`)
        - geracao_pre_definida (`float`)
        - geracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
