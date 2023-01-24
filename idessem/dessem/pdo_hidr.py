from idessem.dessem.modelos.pdo_hidr import TabelaPdoHidr
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoHidr(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as unidades hidráulicas.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_HIDR.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaPdoHidr]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="PDO_HIDR.DAT"
    ) -> "PdoHidr":
        return cls.read(diretorio, nome_arquivo)

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente ao processo iterativo de convergência.

        - estagio (`int`)
        - patamar (`str`)
        - indiceUsina (`int`)
        - nomeUsina (`str`)
        - submercado (`str`)
        - conjunto (`int`)
        - unidade (`int`)
        - valorAgua (`float`)
        - volumeFinalHm3 (`float`)
        - volumeFinalPerc (`float`)
        - vazaoIncrementalM3s (`float`)
        - vazaoIncrementalHm3 (`float`)
        - vazaoMontanteM3s (`float`)
        - vazaoMontanteHm3 (`float`)
        - vazaoMontanteTempoViagemM3s (`float`)
        - vazaoMontanteTempoViagemHm3 (`float`)
        - vazaoDesviadaM3s (`float`)
        - vazaoDesviadaHm3 (`float`)
        - vazaoEvaporadaM3s (`float`)
        - vazaoEvaporadaHm3 (`float`)
        - vazaoUsoAlternativoM3s (`float`)
        - vazaoUsoAlternativoHm3 (`float`)
        - vazaoTurbinadaM3s (`float`)
        - vazaoTurbinadaHm3 (`float`)
        - vazaoTurbinadaMinimaM3s (`float`)
        - vazaoTurbinadaMinimaHm3 (`float`)
        - vazaoTurbinadaMaximaM3s (`float`)
        - vazaoTurbinadaMaximaHm3 (`float`)
        - engolimentoMaximoM3s (`float`)
        - engolimentoMaximoHm3 (`float`)
        - vazaoVertidaM3s (`float`)
        - vazaoVertidaHm3 (`float`)
        - geracao (`float`)
        - geracaoMaxima (`float`)
        - capacidade (`float`)
        - ld (`str`)
        - perdasHidraulicas (`float`)
        - alturaQueda (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
