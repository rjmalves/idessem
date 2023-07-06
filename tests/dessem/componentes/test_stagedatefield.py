from idessem.dessem.modelos.componentes.stagedatefield import StageDateField
import numpy as np


def test_stagedatefield_read():
    data = [6, 0, 0]
    field = StageDateField(starting_position=0)
    line = " 6  0 0-something-else"
    field.read(line)
    assert field.value == data


def test_stagedatefield_read_special():
    data = ["F", 0, 0]
    field = StageDateField(starting_position=0)
    line = " F  0 0-something-else"
    field.read(line)
    assert field.value == data


def test_stagedatefield_write():
    line_before = "field-6   0 0-else"
    data = (6, 0, 0)
    field = StageDateField(starting_position=6, value=data)
    line_after = field.write(line_before)
    assert line_before == line_after


def test_stagedatefield_write_empty():
    field = StageDateField(starting_position=0)
    assert len(field.write("")) == 7


def test_stagedatefield_write_short_line():
    line_before = "F   0 0"
    data = ("F", 0, 0)
    field = StageDateField(5, 6, value=data)
    line_after = field.write("   ")
    assert line_before == line_after[6:]
