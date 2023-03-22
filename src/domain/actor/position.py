#todo: probably should be wrapped in something else?
from dataclasses import dataclass


@dataclass
class Position:
    x : int
    y : int