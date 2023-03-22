from dataclasses import dataclass

from src.domain.event.spell.spell_event import SpellEvent


@dataclass
class SpellLeechEvent(SpellEvent):
    event_type = "SPELL_LEECH"

    amount : int
    power_type : int
    extra_amount : int