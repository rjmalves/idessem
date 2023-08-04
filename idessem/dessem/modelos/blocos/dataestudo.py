from cfinterface.components.block import Block
from cfinterface.components.datetimefield import DatetimeField
from datetime import datetime
from typing import IO


class DataEstudo(Block):
    """
    Bloco para ler a data base do estudo a partir da linha de
    título do estudo existente no arquivo.
    """

    BEGIN_PATTERN = r"Data do Caso:"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, DataEstudo):
            return False
        else:
            if not all(
                [type(self.data) is datetime, type(o.data) is datetime]
            ):
                return False
            return self.data == o.data

    def read(self, file: IO, *args, **kwargs):
        linha = file.readline()
        dados = linha.split(DataEstudo.BEGIN_PATTERN)
        campo = DatetimeField(size=10, starting_position=0, format="%d/%m/%Y")
        self.data = campo.read(dados[1].strip())
