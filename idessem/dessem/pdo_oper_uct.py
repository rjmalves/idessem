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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_OPER_UCT.DAT"
    ) -> "PdoOperUct":
        return cls.read(diretorio, nome_arquivo)

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades térmicas.

        - estagio (`int`)
        - indiceUsina (`int`)
        - unidade (`int`)
        - nomeUsina (`str`)
        - submercado (`str`)
        - barra (`int`)
        - numeroMaximoOscilacoes (`int`)
        - flagGeracaoMinimaMaxima (`int`)
        - geracaoMinima (`float`)
        - geracaoMinimaUnidade (`float`)
        - geracaoMaxima (`float`)
        - geracaoMaximaUnidade (`float`)
        - geracaoMinimaAcionamento (`float`)
        - tempoOn (`int`)
        - tempoOff (`int`)
        - status (`int`)
        - geracao (`float`)
        - tempo (`float`)
        - custoLinear (`float`)
        - custoPartidaUnidade (`float`)
        - cmo (`float`)
        - cmb (`float`)
        - variavelDual (`float`)
        - titulacao (`str`)
        - rampaSubida (`float`)
        - rampaDescida (`float`)
        - unidadeEquivalente (`int`)
        - rampaTransicao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
