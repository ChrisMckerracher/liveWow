from dataclasses import dataclass

from src.domain.event.spell.spell_event import SpellEvent


@dataclass
class SpellAbsorbedEvent(SpellEvent):
    event_type = "SPELL_ABSORBED"
