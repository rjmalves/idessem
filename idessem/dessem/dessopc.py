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
from typing import Type, TypeVar, Optional, List

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="dessopc.dat"
    ) -> "Dessopc":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="dessopc.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def __bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.

        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        :return: O gerador de blocos, se houver
        :rtype: Optional[Generator[T], None, None]
        """
        try:
            return next(
                b
                for i, b in enumerate(self.data.of_type(bloco))
                if i == indice
            )
        except StopIteration:
            return None

    @property
    def uctpar(self) -> Optional[int]:
        """
        Número de threads utilizadas para o processamento paralelo.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.__bloco_por_tipo(BlocoUctPar, 0)
        if b is not None:
            return b.data
        return None

    @uctpar.setter
    def uctpar(self, valor: int):
        b = self.__bloco_por_tipo(BlocoUctPar, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoUcTerm, 0)
        if b is not None:
            return b.data
        return None

    @ucterm.setter
    def ucterm(self, valor: int):
        b = self.__bloco_por_tipo(BlocoUcTerm, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoPint, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoRegraNPTV, 0)
        if b is not None:
            return b.data
        return None

    @regranptv.setter
    def regranptv(self, valor: List[int]):
        b = self.__bloco_por_tipo(BlocoRegraNPTV, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoAvlCmo, 0)
        if b is not None:
            return b.data
        return None

    @avlcmo.setter
    def avlcmo(self, valor: int):
        b = self.__bloco_por_tipo(BlocoAvlCmo, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoCplexLog, 0)
        if b is not None:
            return "CPLEXLOG"
        return None

    @property
    def uctbusloc(self) -> Optional[str]:
        """
        Flag para habilitar a busca local.

        :return: O flag
        :rtype: str | None
        """
        b = self.__bloco_por_tipo(BlocoUctBusLoc, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoUctHeurFp, 0)
        if b is not None:
            return b.data
        return None

    @uctheurfp.setter
    def uctheurfp(self, valor: List[int]):
        b = self.__bloco_por_tipo(BlocoUctHeurFp, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoConstDados, 0)
        if b is not None:
            return b.data
        return None

    @constdados.setter
    def constdados(self, valor: List[int]):
        b = self.__bloco_por_tipo(BlocoConstDados, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoAjusteFcf, 0)
        if b is not None:
            return b.data
        return None

    @ajustefcf.setter
    def ajustefcf(self, valor: List[int]):
        b = self.__bloco_por_tipo(BlocoAjusteFcf, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoTolerIlh, 0)
        if b is not None:
            return b.data
        return None

    @tolerilh.setter
    def tolerilh(self, valor: int):
        b = self.__bloco_por_tipo(BlocoTolerIlh, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoCrossover, 0)
        if b is not None:
            return b.data
        return None

    @crossover.setter
    def crossover(self, valor: List[int]):
        b = self.__bloco_por_tipo(BlocoCrossover, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoEngolimento, 0)
        if b is not None:
            return b.data
        return None

    @engolimento.setter
    def engolimento(self, valor: int):
        b = self.__bloco_por_tipo(BlocoEngolimento, 0)
        if b is not None:
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
        b = self.__bloco_por_tipo(BlocoTrataInviabIlha, 0)
        if b is not None:
            return b.data
        return None

    @tratainviabilha.setter
    def tratainviabilha(self, valor: int):
        b = self.__bloco_por_tipo(BlocoTrataInviabIlha, 0)
        if b is not None:
            b.data = valor
        else:
            raise ValueError("Campo não lido")
