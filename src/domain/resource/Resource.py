from dataclasses import dataclass


@dataclass
class Resource:
    type : int
    current_resource : int
    max_resource : int