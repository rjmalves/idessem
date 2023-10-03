from idessem.dessem.modelos.dessemarq import (
    RegistroCaso,
    RegistroTitulo,
    RegistroVazoes,
    RegistroDadger,
    RegistroMapfcf,
    RegistroCortfcf,
    RegistroCadusih,
    RegistroOperuh,
    RegistroDeflant,
    RegistroCadterm,
    RegistroOperut,
    RegistroIndelet,
    RegistroIlstri,
    RegistroCotasR11,
    RegistroSimul,
    RegistroAreacont,
    RegistroRespot,
    RegistroMlt,
    RegistroTolperd,
    RegistroCurvtviag,
    RegistroPtoper,
    RegistroInfofcf,
    RegistroMetas,
    RegistroREE,
    RegistroEolica,
    RegistroRampas,
    RegistroRstlpp,
    RegistroRestseg,
    RegistroRespotele,
    RegistroIlibs,
    RegistroUch,
)

from cfinterface.files.registerfile import RegisterFile
from cfinterface.components.register import Register
from typing import Type, List, Optional, TypeVar

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DessemArq(RegisterFile):
    """
    Armazena os arquivos de entrada do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `dessem.arq`. Possui métodos para acessar individualmente
    cada nome e editá-lo.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    REGISTERS = [
        RegistroCaso,
        RegistroTitulo,
        RegistroVazoes,
        RegistroDadger,
        RegistroMapfcf,
        RegistroCortfcf,
        RegistroCadusih,
        RegistroOperuh,
        RegistroDeflant,
        RegistroCadterm,
        RegistroOperut,
        RegistroIndelet,
        RegistroIlstri,
        RegistroCotasR11,
        RegistroSimul,
        RegistroAreacont,
        RegistroRespot,
        RegistroMlt,
        RegistroTolperd,
        RegistroCurvtviag,
        RegistroPtoper,
        RegistroInfofcf,
        RegistroMetas,
        RegistroREE,
        RegistroEolica,
        RegistroRampas,
        RegistroRstlpp,
        RegistroRestseg,
        RegistroRespotele,
        RegistroIlibs,
        RegistroUch,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="dessem.arq"
    ) -> "DessemArq":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="dessem.arq"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def __obtem_registro(self, tipo: Type[T]) -> Optional[T]:
        r = [b for b in self.data.of_type(tipo)]
        return r[0] if len(r) > 0 else None

    def cria_registro(self, anterior: Register, registro: Register):
        """
        Adiciona um registro ao arquivo após um outro registro previamente
        existente.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.add_after(anterior, registro)

    def deleta_registro(self, registro: Register):
        """
        Remove um registro existente no arquivo.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.remove(registro)

    def lista_registros(self, tipo: Type[T]) -> List[T]:
        """
        Lista todos os registros presentes no arquivo que tenham o tipo `T`.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        return [r for r in self.data.of_type(tipo)]

    def append_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na última posição.


        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.append(registro)

    def preppend_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na primeira posição.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.preppend(registro)

    @property
    def caso(self) -> Optional[RegistroCaso]:
        """
        A extensão utilizada para o nome do caso.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCaso` | None.
        """
        return self.__obtem_registro(RegistroCaso)

    @property
    def titulo(self) -> Optional[RegistroTitulo]:
        """
        O título do estudo.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroTitulo` | None.
        """
        return self.__obtem_registro(RegistroTitulo)

    @property
    def vazoes(self) -> Optional[RegistroVazoes]:
        """
        O nome do arquivo de vazões naturais.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroVazoes` | None.
        """
        return self.__obtem_registro(RegistroVazoes)

    @property
    def dadger(self) -> Optional[RegistroDadger]:
        """
        O nome do arquivo com os dados gerais.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroDadger` | None.
        """
        return self.__obtem_registro(RegistroDadger)

    @property
    def mapfcf(self) -> Optional[RegistroMapfcf]:
        """
        O nome do arquivo com o cabeçalho dos cortes do DECOMP.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroMapfcf` | None.
        """
        return self.__obtem_registro(RegistroMapfcf)

    @property
    def cortfcf(self) -> Optional[RegistroCortfcf]:
        """
        O nome do arquivo com os cortes do DECOMP.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCortfcf` | None.
        """
        return self.__obtem_registro(RegistroCortfcf)

    @property
    def cadusih(self) -> Optional[RegistroCadusih]:
        """
        O nome do arquivo com o cadastro de usinas hidroelétricas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCadusih` | None.
        """
        return self.__obtem_registro(RegistroCadusih)

    @property
    def operuh(self) -> Optional[RegistroOperuh]:
        """
        O nome do arquivo com as restrições operativas das
        usinas hidroelétricas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroOperuh` | None.
        """
        return self.__obtem_registro(RegistroOperuh)

    @property
    def deflant(self) -> Optional[RegistroDeflant]:
        """
        O nome do arquivo com as defluências anteriores ao
        período de estudo.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroDeflant` | None.
        """
        return self.__obtem_registro(RegistroDeflant)

    @property
    def cadterm(self) -> Optional[RegistroCadterm]:
        """
        O nome do arquivo com o cadastro de usinas térmicas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCadterm` | None.
        """
        return self.__obtem_registro(RegistroCadterm)

    @property
    def operut(self) -> Optional[RegistroOperut]:
        """
        O nome do arquivo com a operação das unidades térmicas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroOperut` | None.
        """
        return self.__obtem_registro(RegistroOperut)

    @property
    def indelet(self) -> Optional[RegistroIndelet]:
        """
        O nome do arquivo com o índice da rede elétrica.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroIndelet` | None.
        """
        return self.__obtem_registro(RegistroIndelet)

    @property
    def ilstri(self) -> Optional[RegistroIlstri]:
        """
        O nome do arquivo com dados do Canal Pereira Barreto.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroIlstri` | None.
        """
        return self.__obtem_registro(RegistroIlstri)

    @property
    def cotasr11(self) -> Optional[RegistroCotasR11]:
        """
        O nome do arquivo com dados das cotas de Régua 11 de Itaipu.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCotasR11` | None.
        """
        return self.__obtem_registro(RegistroCotasR11)

    @property
    def simul(self) -> Optional[RegistroSimul]:
        """
        O nome do arquivo com dados da simulação.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroSimul` | None.
        """
        return self.__obtem_registro(RegistroSimul)

    @property
    def areacont(self) -> Optional[RegistroAreacont]:
        """
        O nome do arquivo de cadastro da reserva de potência.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroAreacont` | None.
        """
        return self.__obtem_registro(RegistroAreacont)

    @property
    def respot(self) -> Optional[RegistroRespot]:
        """
        O nome do arquivo do estudo de reserva de potência.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRespot` | None.
        """
        return self.__obtem_registro(RegistroRespot)

    @property
    def mlt(self) -> Optional[RegistroMlt]:
        """
        O nome do arquivo com dados para a FPHA.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroMlt` | None.
        """
        return self.__obtem_registro(RegistroMlt)

    @property
    def tolperd(self) -> Optional[RegistroTolperd]:
        """
        O nome do arquivo com as tolerâncias das perdas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroTolperd` | None.
        """
        return self.__obtem_registro(RegistroTolperd)

    @property
    def curvtviag(self) -> Optional[RegistroCurvtviag]:
        """
        O nome do arquivo com as curvas de propagação dos
        tempos de viagem.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCurvtviag` | None.
        """
        return self.__obtem_registro(RegistroCurvtviag)

    @property
    def ptoper(self) -> Optional[RegistroPtoper]:
        """
        O nome do arquivo com os pontos de operação das usinas
        témmicas a GNL.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroPtoper` | None.
        """
        return self.__obtem_registro(RegistroPtoper)

    @property
    def infofcf(self) -> Optional[RegistroInfofcf]:
        """
        O nome do arquivo com as informações sobre os cortes.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroInfofcf` | None.
        """
        return self.__obtem_registro(RegistroInfofcf)

    @property
    def meta(self) -> Optional[RegistroMetas]:
        """
        O nome do arquivo com as restrições de metas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroMetas` | None.
        """
        return self.__obtem_registro(RegistroMetas)

    @property
    def ree(self) -> Optional[RegistroREE]:
        """
        O nome do arquivo com os reservatórios equivalentes
        de energia.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroREE` | None.
        """
        return self.__obtem_registro(RegistroREE)

    @property
    def eolica(self) -> Optional[RegistroEolica]:
        """
        O nome do arquivo com os dados de fontes renováveis.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroEolica` | None.
        """
        return self.__obtem_registro(RegistroEolica)

    @property
    def rampas(self) -> Optional[RegistroRampas]:
        """
        O nome do arquivo com trajetórias das rampas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRampas` | None.
        """
        return self.__obtem_registro(RegistroRampas)

    @property
    def rstlpp(self) -> Optional[RegistroRstlpp]:
        """
        O nome do arquivo com as restrições lineares por partes (LPP).

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRstlpp` | None.
        """
        return self.__obtem_registro(RegistroRstlpp)

    @property
    def restseg(self) -> Optional[RegistroRestseg]:
        """
        O nome do arquivo com as restrições de tabela.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRestseg` | None.
        """
        return self.__obtem_registro(RegistroRestseg)

    @property
    def respotele(self) -> Optional[RegistroRespotele]:
        """
        O nome do arquivo com os dados de reserva de potência
        da rede elétrica.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRespotele` | None.
        """
        return self.__obtem_registro(RegistroRespotele)

    @property
    def ilibs(self) -> Optional[RegistroIlibs]:
        """
        O nome do arquivo com as funcionalidades LIBS.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroIlibs` | None.
        """
        return self.__obtem_registro(RegistroIlibs)

    @property
    def uch(self) -> Optional[RegistroUch]:
        """
        O nome do arquivo com os dados do Unit Commitment
        Hidráulico (UCH).

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroIlibs` | None.
        """
        return self.__obtem_registro(RegistroUch)
