from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event
from src.domain.spells.spell import Spell


@dataclass
class SpellAbsorbedEvent(Event):
    event_type = "SPELL_ABSORBED"

    source : Actor
    destination : Actor
    spell : Spell