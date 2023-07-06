from typing import Optional, Union, Tuple

from cfinterface.components.field import Field
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField


class StageDateField(Field):
    """
    Class for representing an composed field for dealing with
    DESSEM specifics.
    """

    def __init__(
        self,
        size: int = 7,
        starting_position: int = 0,
        special_day_character: str = "F",
        value: Optional[
            Tuple[Optional[Union[str, int]], Optional[int], Optional[int]]
        ] = None,
    ) -> None:
        super().__init__(size, starting_position, value)
        self.__subfields: Tuple[LiteralField, IntegerField, IntegerField] = (
            LiteralField(size=2, starting_position=starting_position),
            IntegerField(size=2, starting_position=starting_position + 3),
            IntegerField(size=1, starting_position=starting_position + 6),
        )
        self.__special_day_character = special_day_character

    # Override
    def _binary_read(self, line: bytes) -> int:
        raise NotImplementedError("Binary files not supported for this field")

    # Override
    def _textual_read(self, line: str) -> tuple:
        values = [f._textual_read(line) for f in self.__subfields]
        if values[0] == self.__special_day_character or values[0] is None:
            return tuple(values)
        else:
            return (int(values[0]),) + tuple(values[1:])

    # Override
    def _binary_write(self) -> bytes:
        raise NotImplementedError("Binary files not supported for this field")

    # Override
    def _textual_write(self) -> str:
        if self.value is not None:
            for i, f in enumerate(self.__subfields):
                f.value = self.value[i]
        values = [f._textual_write() for f in self.__subfields]
        return " ".join(values)

    @property
    def value(
        self,
    ) -> Optional[
        Tuple[Optional[Union[str, int]], Optional[int], Optional[int]]
    ]:
        return self._value

    @value.setter
    def value(
        self,
        val: Tuple[Optional[Union[str, int]], Optional[int], Optional[int]],
    ):
        self._value = val
