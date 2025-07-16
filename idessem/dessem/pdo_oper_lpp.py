from idessem.dessem.modelos.pdo_oper_lpp import TabelaaPdoOperLpp
from idessem.dessem.modelos.arquivos.arquivocsv import (
    DataEstudo,
    VersaoModelo,
    ArquivoCSV,
)


class PdoOperLpp(ArquivoCSV):
    """
    Armazena os dados das saídas referentes as restrições lineares por partes.

    Essa classe lida com as informações de saída fornecidas pelo arquivo PDO_OPER_LPP.
    """

    BLOCKS = [VersaoModelo, DataEstudo, TabelaaPdoOperLpp]
    ENCODING = "iso-8859-1"

    @property
    def tabela(self):
        """
        Obtém a tabela com informações referente a operação das unidades térmicas.

        - estagio (`int`)
        - codigo_lpp (`int`)
        - codigo_dref (`int`)
        - codigo_re (`int`)
        - valor (`float`)
        - limite_superior (`float`)
        - indice_corte_ativo (`int`)
        - coeficiente_linear (`float`)
        - codigo_controladora (`str`)
        - tipo_controladora (`str`)
        - valor_parametro (`float`)
        - coeficiente_angular (`float`)
        - multiplicador (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
