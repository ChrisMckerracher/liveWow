from dataclasses import dataclass

from typing import TypeVar, Generic

T = TypeVar("T")
@dataclass
class SimpleMap(Generic[T]):
    assignment : tuple[int, T]

    def get_index(self) -> int:
        return self.assignment[0]

    def get_typing(self) -> T:
        return self.assignment[1]