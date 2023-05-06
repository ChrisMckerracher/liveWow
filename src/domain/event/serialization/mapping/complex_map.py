from dataclasses import dataclass

from typing import TypeVar, Generic, Tuple, List

from src.domain.event.serialization.mapping.simple_map import SimpleMap

T = TypeVar("T")

# ToDo: a complex map should be a collection of simple maps. rewrite this later
@dataclass
class ComplexMap(Generic[T]):
    #ToDo: why the fuck is this a tuple and not just three fucking attributes? was i stoned?
    assignment : Tuple[str, List[SimpleMap], T]

    def get_field_name(self) -> str:
        return self.assignment[0]

    def get_maps(self) -> List[SimpleMap]:
        return self.assignment[1]

    def get_typing(self) -> T:
        return self.assignment[2]
