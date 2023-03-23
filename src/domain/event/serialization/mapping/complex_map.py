from dataclasses import dataclass

from typing import TypeVar, Generic

T = TypeVar("T")
@dataclass
class ComplexMap(Generic[T]):
    assignment : tuple[list[int], T]

    def get_indices(self) -> list[int]:
        return self.assignment[0]

    def get_typing(self) -> T:
        return self.assignment[1]