from idessem.dessem.modelos.avl_desvfpha import TabelaAvlDesvFpha
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class AvlDesvFpha(ArquivoCSV):
    """
    Armazena os dados das saídas referentes aos desvios da função de produção.

    Essa classe lida com as informações de saída fornecidas pelo arquivo AVL_DESVFPHA.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaAvlDesvFpha]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="AVL_DESVFPHA.DAT"
    ) -> "AvlDesvFpha":
        return cls.read(diretorio, nome_arquivo)

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente aos desvios da função de produção.

        - estagio (`int`)
        - indiceUsina (`int`)
        - nomeUsina (`str`)
        - volumeMedioHm3 (`float`)
        - volumeMedioPerc (`float`)
        - vazaoTurbinadaM3s (`float`)
        - vazaoVertidaM3s (`float`)
        - vazaoJusanteM3s (`float`)
        - vazaoLateralUsinaM3s (`float`)
        - vazaoLateralPostoM3s (`float`)
        - alturaJusante (`float`)
        - alturaMontante (`float`)
        - produtibilidaEspecifica (`float`)
        - perdasHidraulicas (`float`)
        - influenciaVertimentoCanalFuga (`int`)
        - afogamentoCanalFuga (`int`)
        - geracaoFph (`float`)
        - geracaoPl (`float`)
        - geracaoFpha (`float`)
        - desvioAbsolutoFphPl (`float`)
        - desvioPercentualFphPl (`float`)
        - desvioAbsolutoFphFpha (`float`)
        - desvioPercentualFphFpha (`float`)


        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
