from dataclasses import dataclass

from typing import TypeVar, Generic, Tuple

T = TypeVar("T")
@dataclass
class SimpleMap(Generic[T]):
    assignment : Tuple[str, int, T]

    def get_field_name(self) -> str:
        return self.assignment[0]

    def get_index(self) -> int:
        return self.assignment[1]


    def get_typing(self) -> T:
        return self.assignment[2]