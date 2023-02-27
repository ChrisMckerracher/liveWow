from dataclasses import dataclass
from .spell_school import SpellSchool
from .power_type import PowerType


@dataclass
class Spell:
    spell_name: str
    spell_school: SpellSchool
    power_type: PowerType
