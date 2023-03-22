from dataclasses import dataclass

from src.domain.event.spell.spell_event import SpellEvent

@dataclass
class SpellCastFailedEvent(SpellEvent):
    event_type = "SPELL_CAST_FAILED"

    failed_type : int