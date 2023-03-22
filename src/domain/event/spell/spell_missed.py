from dataclasses import dataclass

from src.domain.event.spell.spell_event import SpellEvent


@dataclass
class SpellMissedEvent(SpellEvent):
    event_type = "SPELL_MISSED"

    miss_type: int