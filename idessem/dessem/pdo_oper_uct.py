from idessem.dessem.modelos.pdo_oper_uct import TabelaPdoOperUct
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoOperUct(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as unidades térmicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_OPER_UCT.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoOperUct]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades térmicas.

        - estagio (`int`)
        - codigo_usina (`int`)
        - codigo_unidade (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
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
