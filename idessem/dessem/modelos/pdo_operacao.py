from cfinterface.components.block import Block
from typing import IO
import pandas as pd  # type: ignore
from datetime import datetime


class BlocoDiscretizacaoTempo(Block):
    """
    Bloco com a discretização de tempo do estudo,
    existente no `PDO_OPERACAO.DAT`.
    """

    BEGIN_PATTERN = r"  DISCRETIZACAO DE TEMPO PARA O CASO EM ESTUDO"
    END_PATTERN = r"-----------------"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDiscretizacaoTempo):
            return False
        bloco: BlocoDiscretizacaoTempo = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(
                data={
                    "estagio": estagios,
                    "data_inicial": datasiniciais,
                    "data_final": datasfinais,
                    "duracao": duracoes,
                }
            )
            return df

        estagios = []
        datasiniciais = []
        datasfinais = []
        duracoes = []

        while True:
            linha = file.readline()
            if self.begins(linha):
                linha = file.readline()
                linha = file.readline()
                linha = file.readline()
                continue
            if self.ends(linha):
                self.data = converte_tabela_em_df()
                break
            if linha == "\n":
                continue

            dados_linha = [i for i in linha.split(" ") if i != ""]
            estagio = int(dados_linha[0])
            date_format = "%d/%m/%Y %H:%M"
            datainicial_str = dados_linha[1] + " " + dados_linha[2]
            datafinal_str = dados_linha[3] + " " + dados_linha[4]
            datainicial = datetime.strptime(datainicial_str, date_format)
            datafinal = datetime.strptime(datafinal_str, date_format)
            duracao = float(dados_linha[-1].split("\n")[0])

            estagios.append(estagio)
            datasiniciais.append(datainicial)
            datasfinais.append(datafinal)
            duracoes.append(duracao)


class BlocoCustos(Block):
    """
    Bloco com os custos presente e futuro obtidos da otimização do
    DESSEM, existente no `PDO_OPERACAO.DAT`.
    """

    BEGIN_PATTERN = r"PERIODO:"
    END_PATTERN = r"1 - BALANCO HIDRICO"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCustos):
            return False
        bloco: BlocoCustos = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(
                data={
                    "estagio": estagios,
                    "custo_presente": custos_presentes,
                    "custo_futuro": custos_futuros,
                }
            )
            return df

        custos_presentes = []
        custos_futuros = []
        estagios = []

        while True:
            posicao_ultima_linha = file.tell()
            linha = file.readline()
            if self.begins(linha):
                estagio = int(linha.split(":")[1].split()[0])
                continue
            if self.ends(linha):
                file.seek(posicao_ultima_linha)
                self.data = converte_tabela_em_df()
                break
            if len(linha) < 5 or "---------" in linha:
                continue

            custo_presente = float(linha.split(":")[1])
            linha = file.readline()
            custo_futuro = float(linha.split(":")[1])

            estagios.append(estagio)
            custos_presentes.append(custo_presente)
            custos_futuros.append(custo_futuro)


class BlocoCortesAtivos(Block):
    """
    Bloco com os os multiplicadores dos cortes sinalizando os
    cortes ativos, existente no `PDO_OPERACAO.DAT`.
    """

    BEGIN_PATTERN = r"   ITERACAO"
    END_PATTERN = r"========="

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCortesAtivos):
            return False
        bloco: BlocoCortesAtivos = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(
                data={
                    "indice_corte": iteracoes,
                    "multiplicador": multiplicadores,
                }
            )
            return df

        iteracoes = []
        multiplicadores = []

        while True:
            linha = file.readline()
            if self.begins(linha):
                continue
            if self.ends(linha):
                self.data = converte_tabela_em_df()
                break
            if "---------" in linha:
                continue

            iteracao = int(linha.strip(" ").split(" ")[0])
            mutiplicador = float(linha.strip(" ").split(" ")[-1])

            iteracoes.append(iteracao)
            multiplicadores.append(mutiplicador)
