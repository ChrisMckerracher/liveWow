import json
from dataclasses import dataclass


@dataclass
class Actor:
    id: str
    name: str
    flags: str
    raid_flags: str

    def __str__(self):
        return str(json.dumps(self.__dict__))