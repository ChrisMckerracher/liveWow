#toDo: add hp to a different domain object?
from dataclasses import dataclass


@dataclass
class HP:
    current_hp : int
    max_hp : int