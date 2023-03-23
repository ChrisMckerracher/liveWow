from dataclasses import dataclass
from .spell_school import SpellSchool

@dataclass
class Spell:
    id : str
    name: str
    school: str
