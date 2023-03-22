from dataclasses import dataclass

from src.domain.event.spell.spell_event import SpellEvent
from src.domain.spells.spell import Spell


@dataclass
class SpellInterruptEvent(SpellEvent):
    event_type = "SPELL_INTERRUPT"

    interrupt : Spell