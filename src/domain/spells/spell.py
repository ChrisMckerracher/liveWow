import json
from dataclasses import dataclass
from .spell_school import SpellSchool

@dataclass
class Spell:
    id : str
    name: str
    school: str

    def __str__(self):
        return str(json.dumps(self.__dict__))
