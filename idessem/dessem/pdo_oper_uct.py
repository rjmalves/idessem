from idessem.dessem.modelos.pdo_oper_uct import TabelaPdoOperUct
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class PdoOperUct(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as unidades térmicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_OPER_UCT.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoOperUct]
    ENCODING = "iso-8859-1"

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_OPER_UCT.DAT"
    ) -> "PdoOperUct":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades térmicas.

        - estagio (`int`)
        - indice_usina (`int`)
        - unidade (`int`)
        - nome_usina (`str`)
        - submercado (`str`)
        - barra (`int`)
        - numero_maximo_oscilacoes (`int`)
        - flag_geracao_minima_maxima (`int`)
        - geracao_minima (`float`)
        - geracao_minima_unidade (`float`)
        - geracao_maxima (`float`)
        - geracao_maxima_unidade (`float`)
        - geracao_minima_acionamento (`float`)
        - tempo_on (`int`)
        - tempo_off (`int`)
        - status (`int`)
        - geracao (`float`)
        - tempo (`float`)
        - custo_linear (`float`)
        - custo_partida_unidade (`float`)
        - cmo (`float`)
        - cmb (`float`)
        - variavel_dual (`float`)
        - titulacao (`str`)
        - rampa_subida (`float`)
        - rampa_descida (`float`)
        - unidade_equivalente (`int`)
        - rampa_transicao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
