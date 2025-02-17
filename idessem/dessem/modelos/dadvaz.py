from typing import IO, List, Optional

import pandas as pd  # type: ignore
from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.section import Section
from idessem.dessem.modelos.componentes.stagedatefield import StageDateField

class BlocoDataInicioEstudo(Section):
    """
    Bloco com a data de início do estudo.
    """

    __slots__ = ["__linha", "__cabecalhos"]

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([
            IntegerField(2, 0),
            IntegerField(2, 4),
            IntegerField(2, 8),
            IntegerField(4, 12),
        ])
        self.__cabecalhos: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDataInicioEstudo):
            return False
        bloco: BlocoDataInicioEstudo = o
        if not all([
            isinstance(self.data, list),
            isinstance(o.data, list),
        ]):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        for _ in range(9):
            self.__cabecalhos.append(file.readline())
        self.data = self.__linha.read(file.readline())

     # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__cabecalhos:
            file.write(linha)
        if not isinstance(self.data, list):
            raise ValueError("Dados do dadvaz.dat não foram lidos com sucesso")
        file.write(self.__linha.write(self.data))

    @property
    def hora(self) -> Optional[int]:
        """
        A hora de referência para realização do estudo

        :return: A hora
        :rtype: int | None
        """
        return self.data[0]

    @hora.setter
    def hora(self, d: int):
        self.data[0] = d

    @property
    def dia(self) -> Optional[int]:
        """
        O dia de referência para realização do estudo

        :return: O dia
        :rtype: int | None
        """
        return self.data[1]

    @dia.setter
    def dia(self, d: int):
        self.data[1] = d

    @property
    def mes(self) -> Optional[int]:
        """
        O mês de referência para realização do estudo

        :return: O mês
        :rtype: int | None
        """
        return self.data[2]

    @mes.setter
    def mes(self, m: int):
        self.data[2] = m

    @property
    def ano(self) -> Optional[int]:
        """
        O ano de referência para realização do estudo

        :return: O ano
        :rtype: int | None
        """
        return self.data[3]

    @ano.setter
    def ano(self, a: int):
        self.data[3] = a


class BlocoDadosHorizonte(Section):
    """
    Bloco com os dados do horizonte considerado.
    """

    __slots__ = ["__linha", "__cabecalhos"]

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([
            IntegerField(1, 0),
            IntegerField(1, 2),
            IntegerField(1, 4),
            IntegerField(1, 6),
        ])
        self.__cabecalhos: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDadosHorizonte):
            return False
        bloco: BlocoDadosHorizonte = o
        if not all([
            isinstance(self.data, list),
            isinstance(o.data, list),
        ]):
            return False
        else:
            return self.data == bloco.data
        

    def read(self, file: IO, *args, **kwargs):
        for _ in range(2):
            self.__cabecalhos.append(file.readline())
        self.data = self.__linha.read(file.readline())

     # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__cabecalhos:
            file.write(linha)
        if not isinstance(self.data, list):
            raise ValueError("Dados do dadvaz.dat não foram lidos com sucesso")
        file.write(self.__linha.write(self.data))


    @property
    def dia_semana_inicial(self) -> Optional[int]:
        """
        O código para o dia da semana inicial (1=sex,...,7=sex)

        :return: O código do dia
        :rtype: int | None
        """
        return self.data[0]

    @dia_semana_inicial.setter
    def dia_semana_inicial(self, d: int):
        self.data[0] = d

    @property
    def semana_acoplamento_fcf(self) -> Optional[int]:
        """
        O índice da semana da FCF acoplada

        :return: O código do dia
        :rtype: int | None
        """
        return self.data[1]

    @semana_acoplamento_fcf.setter
    def semana_acoplamento_fcf(self, d: int):
        self.data[1] = d

    @property
    def numero_semanas(self) -> Optional[int]:
        """
        O número de semanas no estudo

        :return: O código do dia
        :rtype: int | None
        """
        return self.data[2]

    @numero_semanas.setter
    def numero_semanas(self, d: int):
        self.data[2] = d

    @property
    def considera_periodo_simulacao(self) -> Optional[int]:
        """
        O flag que indica presença de período de simulação 

        :return: O código do dia
        :rtype: int | None
        """
        return self.data[3]

    @considera_periodo_simulacao.setter
    def considera_periodo_simulacao(self, d: int):
        self.data[3] = d


class BlocoVazoes(Section):
    """
    Bloco com as vazões incrementais ao longo do estudo.
    """

    __slots__ = ["__linha", "__cabecalhos"]

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([
            IntegerField(3, 0),
            LiteralField(12,4),
            IntegerField(1, 19),
            StageDateField(starting_position=24,special_day_character="I"),
            StageDateField(starting_position=32,special_day_character="F"),
            FloatField(9,44,2)
        ])
        self.__cabecalhos: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoVazoes):
            return False
        bloco: BlocoVazoes = o
        if not all([
            isinstance(self.data, pd.DataFrame),
            isinstance(o.data, pd.DataFrame),
        ]):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, file: IO, *args, **kwargs):
        def extrai_coluna_de_listas(listas: List[list], coluna: int, elemento: int | None = None) -> list:
            if elemento is None:
                return [lista[coluna] for lista in listas] 
            else:
                return [lista[coluna][elemento] for lista in listas] 

        def transforma_uhes_em_tabela() -> pd.DataFrame:
            # Converte as informações de cada linha em colunas
            col_num = extrai_coluna_de_listas(dados_uhes, 0)
            col_nome = extrai_coluna_de_listas(dados_uhes, 1)
            col_tipo = extrai_coluna_de_listas(dados_uhes, 2)
            col_dia_inicial = extrai_coluna_de_listas(dados_uhes, 3, 0)
            col_hora_inicial = extrai_coluna_de_listas(dados_uhes, 3, 1)
            col_meia_hora_inicial = extrai_coluna_de_listas(dados_uhes, 3, 2)
            col_dia_final = extrai_coluna_de_listas(dados_uhes, 4, 0)
            col_hora_final = extrai_coluna_de_listas(dados_uhes, 4, 1)
            col_meia_hora_final = extrai_coluna_de_listas(dados_uhes, 4, 2)
            col_vazao = extrai_coluna_de_listas(dados_uhes, 5)
            dados = {
                "codigo_usina": col_num,
                "nome_usina": col_nome,
                "tipo_dado": col_tipo,
                "dia_inicial": col_dia_inicial,
                "hora_inicial": col_hora_inicial,
                "meia_hora_inicial": col_meia_hora_inicial,
                "dia_final": col_dia_final,
                "hora_final": col_hora_final,
                "meia_hora_final": col_meia_hora_final,
                "vazao": col_vazao
            }
            return pd.DataFrame(data=dados)

        # Salta as linhas adicionais
        for _ in range(3):
            self.__cabecalhos.append(file.readline())

        # Para cada usina, lê e processa as informações
        dados_uhes: List[list] = []
        while True:
            linha = file.readline()
            # Confere se terminaram as usinas
            if len(linha) < 5:
                # Converte para df e salva na variável
                if len(dados_uhes) > 0:
                    self.data = transforma_uhes_em_tabela()
                break
            dados_uhe = self.__linha.read(linha)
            dados_uhes.append(dados_uhe)


    # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__cabecalhos:
            file.write(linha)
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("Dados do dadvaz.dat não foram lidos com sucesso")

        for _, lin in self.data.iterrows():
            file.write(self.__linha.write(lin.tolist()))


