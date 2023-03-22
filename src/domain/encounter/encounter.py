from dataclasses import dataclass


@dataclass
class Encounter:
    id : str
    name : str
    difficulty : int
    group_size : int