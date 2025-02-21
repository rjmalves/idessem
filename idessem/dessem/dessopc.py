from idessem.dessem.modelos.dessopc import (
    BlocoUctPar,
    BlocoUcTerm,
    BlocoPint,
    BlocoRegraNPTV,
    BlocoAvlCmo,
    BlocoCplexLog,
    BlocoUctBusLoc,
    BlocoUctHeurFp,
    BlocoConstDados,
    BlocoAjusteFcf,
    BlocoTolerIlh,
    BlocoCrossover,
    BlocoEngolimento,
    BlocoTrataInviabIlha,
)

from cfinterface.files.blockfile import BlockFile
from typing import TypeVar, Optional, List


class Dessopc(BlockFile):
    """
    Armazena os dados de entrada do DESSEM referentes às
    configurações da operação das usinas térmelétricas.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoUctPar,
        BlocoUcTerm,
        BlocoPint,
        BlocoRegraNPTV,
        BlocoAvlCmo,
        BlocoCplexLog,
        BlocoUctBusLoc,
        BlocoUctHeurFp,
        BlocoConstDados,
        BlocoAjusteFcf,
        BlocoTolerIlh,
        BlocoCrossover,
        BlocoEngolimento,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @property
    def uctpar(self) -> Optional[int]:
        """
        Número de threads utilizadas para o processamento paralelo.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoUctPar)
        if isinstance(b, BlocoUctPar):
            return b.data
        return None

    @uctpar.setter
    def uctpar(self, valor: int):
        b = self.data.get_blocks_of_type(BlocoUctPar)
        if isinstance(b, BlocoUctPar):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def ucterm(self) -> Optional[int]:
        """
        Metodologia de solução para inclusão de rede e UCT.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoUcTerm)
        if isinstance(b, BlocoUcTerm):
            return b.data
        return None

    @ucterm.setter
    def ucterm(self, valor: int):
        b = self.data.get_blocks_of_type(BlocoUcTerm)
        if isinstance(b, BlocoUcTerm):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def pint(self) -> Optional[str]:
        """
        Flag para ativar metodologia de pontos interiores.

        :return: O flag
        :rtype: str | None
        """
        b = self.data.get_blocks_of_type(BlocoPint)
        if isinstance(b, BlocoPint):
            return "PINT"
        return None

    @property
    def regranptv(self) -> Optional[List[int]]:
        """
        Definição de valores default para a função de produção
        hidráulica.

        :return: Lista com os flag
        :rtype: list | None
        """
        b = self.data.get_blocks_of_type(BlocoRegraNPTV)
        if isinstance(b, BlocoRegraNPTV):
            return b.data
        return None

    @regranptv.setter
    def regranptv(self, valor: List[int]):
        b = self.data.get_blocks_of_type(BlocoRegraNPTV)
        if isinstance(b, BlocoRegraNPTV):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def avlcmo(self) -> Optional[int]:
        """
        Impressão dos arquivos de avalição de CMO.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoAvlCmo)
        if isinstance(b, BlocoAvlCmo):
            return b.data
        return None

    @avlcmo.setter
    def avlcmo(self, valor: int):
        b = self.data.get_blocks_of_type(BlocoAvlCmo)
        if isinstance(b, BlocoAvlCmo):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def cplexlog(self) -> Optional[str]:
        """
        Flag para habilitar a impressão de arquivo log do CPLEX.

        :return: O flag
        :rtype: str | None
        """
        b = self.data.get_blocks_of_type(BlocoCplexLog)
        if isinstance(b, BlocoCplexLog):
            return "CPLEXLOG"
        return None

    @property
    def uctbusloc(self) -> Optional[str]:
        """
        Flag para habilitar a busca local.

        :return: O flag
        :rtype: str | None
        """
        b = self.data.get_blocks_of_type(BlocoUctBusLoc)
        if isinstance(b, BlocoUctBusLoc):
            return "UCTBUSLOC"
        return None

    @property
    def uctheurfp(self) -> Optional[List[int]]:
        """
        Metodologia Feasibility Pump com Busca Local
        e Fixação de Variáveis de Status.

        :return: Lista com os flag
        :rtype: list | None
        """
        b = self.data.get_blocks_of_type(BlocoUctHeurFp)
        if isinstance(b, BlocoUctHeurFp):
            return b.data
        return None

    @uctheurfp.setter
    def uctheurfp(self, valor: List[int]):
        b = self.data.get_blocks_of_type(BlocoUctHeurFp)
        if isinstance(b, BlocoUctHeurFp):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def constdados(self) -> Optional[List[int]]:
        """
        Consistência de dados.

        :return: Lista com os flag
        :rtype: list | None
        """
        b = self.data.get_blocks_of_type(BlocoConstDados)
        if isinstance(b, BlocoConstDados):
            return b.data
        return None

    @constdados.setter
    def constdados(self, valor: List[int]):
        b = self.data.get_blocks_of_type(BlocoConstDados)
        if isinstance(b, BlocoConstDados):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def ajustefcf(self) -> Optional[List[int]]:
        """
        Ajuste da função de custo futuro.

        :return: Lista com os flag
        :rtype: list | None
        """
        b = self.data.get_blocks_of_type(BlocoAjusteFcf)
        if isinstance(b, BlocoAjusteFcf):
            return b.data
        return None

    @ajustefcf.setter
    def ajustefcf(self, valor: List[int]):
        b = self.data.get_blocks_of_type(BlocoAjusteFcf)
        if isinstance(b, BlocoAjusteFcf):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def tolerilh(self) -> Optional[int]:
        """
        Tolerância nas equações de demanda por ilha.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoTolerIlh)
        if isinstance(b, BlocoTolerIlh):
            return b.data
        return None

    @tolerilh.setter
    def tolerilh(self, valor: int):
        b = self.data.get_blocks_of_type(BlocoTolerIlh)
        if isinstance(b, BlocoTolerIlh):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def crossover(self) -> Optional[List[int]]:
        """
        Metodologia Feasibility Pump com Busca Local
        e Fixação de Variáveis de Status.

        :return: Lista com os flag
        :rtype: list | None
        """
        b = self.data.get_blocks_of_type(BlocoCrossover)
        if isinstance(b, BlocoCrossover):
            return b.data
        return None

    @crossover.setter
    def crossover(self, valor: List[int]):
        b = self.data.get_blocks_of_type(BlocoCrossover)
        if isinstance(b, BlocoCrossover):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def engolimento(self) -> Optional[int]:
        """
        Consideração do engolimento máximo.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoEngolimento)
        if isinstance(b, BlocoEngolimento):
            return b.data
        return None

    @engolimento.setter
    def engolimento(self, valor: int):
        b = self.data.get_blocks_of_type(BlocoEngolimento)
        if isinstance(b, BlocoEngolimento):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def tratainviabilha(self) -> Optional[int]:
        """
        Tratamento automático de inviabilidades de ilha elétrica.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoTrataInviabIlha)
        if isinstance(b, BlocoTrataInviabIlha):
            return b.data
        return None

    @tratainviabilha.setter
    def tratainviabilha(self, valor: int):
        b = self.data.get_blocks_of_type(BlocoTrataInviabIlha)
        if isinstance(b, BlocoTrataInviabIlha):
            b.data = valor
        else:
            raise ValueError("Campo não lido")
