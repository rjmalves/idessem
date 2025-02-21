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
    RegistroDessopc,
)

from cfinterface.files.registerfile import RegisterFile
from typing import Optional, TypeVar


class DessemArq(RegisterFile):
    """
    Armazena os arquivos de entrada do DESSEM.

    Esta classe lida com as informações de entrada fornecidas ao
    DESSEM no `dessem.arq`. Possui métodos para acessar individualmente
    cada nome e editá-lo.


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
        RegistroDessopc,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @property
    def caso(self) -> Optional[RegistroCaso]:
        """
        A extensão utilizada para o nome do caso.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCaso` | None.
        """
        r = self.data.get_registers_of_type(RegistroCaso)
        if isinstance(r, RegistroCaso):
            return r
        else:
            return None

    @property
    def titulo(self) -> Optional[RegistroTitulo]:
        """
        O título do estudo.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroTitulo` | None.
        """
        r = self.data.get_registers_of_type(RegistroTitulo)
        if isinstance(r, RegistroTitulo):
            return r
        else:
            return None

    @property
    def vazoes(self) -> Optional[RegistroVazoes]:
        """
        O nome do arquivo de vazões naturais.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroVazoes` | None.
        """
        r = self.data.get_registers_of_type(RegistroVazoes)
        if isinstance(r, RegistroVazoes):
            return r
        else:
            return None

    @property
    def dadger(self) -> Optional[RegistroDadger]:
        """
        O nome do arquivo com os dados gerais.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroDadger` | None.
        """
        r = self.data.get_registers_of_type(RegistroDadger)
        if isinstance(r, RegistroDadger):
            return r
        else:
            return None

    @property
    def mapfcf(self) -> Optional[RegistroMapfcf]:
        """
        O nome do arquivo com o cabeçalho dos cortes do DECOMP.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroMapfcf` | None.
        """
        r = self.data.get_registers_of_type(RegistroMapfcf)
        if isinstance(r, RegistroMapfcf):
            return r
        else:
            return None

    @property
    def cortfcf(self) -> Optional[RegistroCortfcf]:
        """
        O nome do arquivo com os cortes do DECOMP.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCortfcf` | None.
        """
        r = self.data.get_registers_of_type(RegistroCortfcf)
        if isinstance(r, RegistroCortfcf):
            return r
        else:
            return None

    @property
    def cadusih(self) -> Optional[RegistroCadusih]:
        """
        O nome do arquivo com o cadastro de usinas hidroelétricas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCadusih` | None.
        """
        r = self.data.get_registers_of_type(RegistroCadusih)
        if isinstance(r, RegistroCadusih):
            return r
        else:
            return None

    @property
    def operuh(self) -> Optional[RegistroOperuh]:
        """
        O nome do arquivo com as restrições operativas das
        usinas hidroelétricas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroOperuh` | None.
        """
        r = self.data.get_registers_of_type(RegistroOperuh)
        if isinstance(r, RegistroOperuh):
            return r
        else:
            return None

    @property
    def deflant(self) -> Optional[RegistroDeflant]:
        """
        O nome do arquivo com as defluências anteriores ao
        período de estudo.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroDeflant` | None.
        """
        r = self.data.get_registers_of_type(RegistroDeflant)
        if isinstance(r, RegistroDeflant):
            return r
        else:
            return None

    @property
    def cadterm(self) -> Optional[RegistroCadterm]:
        """
        O nome do arquivo com o cadastro de usinas térmicas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCadterm` | None.
        """
        r = self.data.get_registers_of_type(RegistroCadterm)
        if isinstance(r, RegistroCadterm):
            return r
        else:
            return None

    @property
    def operut(self) -> Optional[RegistroOperut]:
        """
        O nome do arquivo com a operação das unidades térmicas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroOperut` | None.
        """
        r = self.data.get_registers_of_type(RegistroOperut)
        if isinstance(r, RegistroOperut):
            return r
        else:
            return None

    @property
    def indelet(self) -> Optional[RegistroIndelet]:
        """
        O nome do arquivo com o índice da rede elétrica.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroIndelet` | None.
        """
        r = self.data.get_registers_of_type(RegistroIndelet)
        if isinstance(r, RegistroIndelet):
            return r
        else:
            return None

    @property
    def ilstri(self) -> Optional[RegistroIlstri]:
        """
        O nome do arquivo com dados do Canal Pereira Barreto.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroIlstri` | None.
        """
        r = self.data.get_registers_of_type(RegistroIlstri)
        if isinstance(r, RegistroIlstri):
            return r
        else:
            return None

    @property
    def cotasr11(self) -> Optional[RegistroCotasR11]:
        """
        O nome do arquivo com dados das cotas de Régua 11 de Itaipu.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCotasR11` | None.
        """
        r = self.data.get_registers_of_type(RegistroCotasR11)
        if isinstance(r, RegistroCotasR11):
            return r
        else:
            return None

    @property
    def simul(self) -> Optional[RegistroSimul]:
        """
        O nome do arquivo com dados da simulação.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroSimul` | None.
        """
        r = self.data.get_registers_of_type(RegistroSimul)
        if isinstance(r, RegistroSimul):
            return r
        else:
            return None

    @property
    def areacont(self) -> Optional[RegistroAreacont]:
        """
        O nome do arquivo de cadastro da reserva de potência.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroAreacont` | None.
        """
        r = self.data.get_registers_of_type(RegistroAreacont)
        if isinstance(r, RegistroAreacont):
            return r
        else:
            return None

    @property
    def respot(self) -> Optional[RegistroRespot]:
        """
        O nome do arquivo do estudo de reserva de potência.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRespot` | None.
        """
        r = self.data.get_registers_of_type(RegistroRespot)
        if isinstance(r, RegistroRespot):
            return r
        else:
            return None

    @property
    def mlt(self) -> Optional[RegistroMlt]:
        """
        O nome do arquivo com dados para a FPHA.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroMlt` | None.
        """
        r = self.data.get_registers_of_type(RegistroMlt)
        if isinstance(r, RegistroMlt):
            return r
        else:
            return None

    @property
    def tolperd(self) -> Optional[RegistroTolperd]:
        """
        O nome do arquivo com as tolerâncias das perdas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroTolperd` | None.
        """
        r = self.data.get_registers_of_type(RegistroTolperd)
        if isinstance(r, RegistroTolperd):
            return r
        else:
            return None

    @property
    def curvtviag(self) -> Optional[RegistroCurvtviag]:
        """
        O nome do arquivo com as curvas de propagação dos
        tempos de viagem.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroCurvtviag` | None.
        """
        r = self.data.get_registers_of_type(RegistroCurvtviag)
        if isinstance(r, RegistroCurvtviag):
            return r
        else:
            return None

    @property
    def ptoper(self) -> Optional[RegistroPtoper]:
        """
        O nome do arquivo com os pontos de operação das usinas
        témmicas a GNL.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroPtoper` | None.
        """
        r = self.data.get_registers_of_type(RegistroPtoper)
        if isinstance(r, RegistroPtoper):
            return r
        else:
            return None

    @property
    def infofcf(self) -> Optional[RegistroInfofcf]:
        """
        O nome do arquivo com as informações sobre os cortes.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroInfofcf` | None.
        """
        r = self.data.get_registers_of_type(RegistroInfofcf)
        if isinstance(r, RegistroInfofcf):
            return r
        else:
            return None

    @property
    def meta(self) -> Optional[RegistroMetas]:
        """
        O nome do arquivo com as restrições de metas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroMetas` | None.
        """
        r = self.data.get_registers_of_type(RegistroMetas)
        if isinstance(r, RegistroMetas):
            return r
        else:
            return None

    @property
    def ree(self) -> Optional[RegistroREE]:
        """
        O nome do arquivo com os reservatórios equivalentes
        de energia.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroREE` | None.
        """
        r = self.data.get_registers_of_type(RegistroREE)
        if isinstance(r, RegistroREE):
            return r
        else:
            return None

    @property
    def eolica(self) -> Optional[RegistroEolica]:
        """
        O nome do arquivo com os dados de fontes renováveis.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroEolica` | None.
        """
        r = self.data.get_registers_of_type(RegistroEolica)
        if isinstance(r, RegistroEolica):
            return r
        else:
            return None

    @property
    def rampas(self) -> Optional[RegistroRampas]:
        """
        O nome do arquivo com trajetórias das rampas.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRampas` | None.
        """
        r = self.data.get_registers_of_type(RegistroRampas)
        if isinstance(r, RegistroRampas):
            return r
        else:
            return None

    @property
    def rstlpp(self) -> Optional[RegistroRstlpp]:
        """
        O nome do arquivo com as restrições lineares por partes (LPP).

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRstlpp` | None.
        """
        r = self.data.get_registers_of_type(RegistroRstlpp)
        if isinstance(r, RegistroRstlpp):
            return r
        else:
            return None

    @property
    def restseg(self) -> Optional[RegistroRestseg]:
        """
        O nome do arquivo com as restrições de tabela.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRestseg` | None.
        """
        r = self.data.get_registers_of_type(RegistroRestseg)
        if isinstance(r, RegistroRestseg):
            return r
        else:
            return None

    @property
    def respotele(self) -> Optional[RegistroRespotele]:
        """
        O nome do arquivo com os dados de reserva de potência
        da rede elétrica.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroRespotele` | None.
        """
        r = self.data.get_registers_of_type(RegistroRespotele)
        if isinstance(r, RegistroRespotele):
            return r
        else:
            return None

    @property
    def ilibs(self) -> Optional[RegistroIlibs]:
        """
        O nome do arquivo com as funcionalidades LIBS.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroIlibs` | None.
        """
        r = self.data.get_registers_of_type(RegistroIlibs)
        if isinstance(r, RegistroIlibs):
            return r
        else:
            return None

    @property
    def uch(self) -> Optional[RegistroUch]:
        """
        O nome do arquivo com os dados do Unit Commitment
        Hidráulico (UCH).

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroUch` | None.
        """
        r = self.data.get_registers_of_type(RegistroUch)
        if isinstance(r, RegistroUch):
            return r
        else:
            return None

    @property
    def dessopc(self) -> Optional[RegistroDessopc]:
        """
        O nome do arquivo com as opções de execução.

        :return: Um registro, se existir.
        :rtype:  :class:`RegistroDessopc` | None.
        """
        r = self.data.get_registers_of_type(RegistroDessopc)
        if isinstance(r, RegistroDessopc):
            return r
        else:
            return None
