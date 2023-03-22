from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event
from src.domain.spells.spell import Spell
@dataclass
class SpellAuraEvent(Event):
    source : Actor
    destination : Actor
    spell : Spell
    # ToDo This should be an enum
    aura_type : str
