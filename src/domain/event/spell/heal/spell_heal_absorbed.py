from dataclasses import dataclass

from src.domain.event.spell.spell_event import SpellEvent

@dataclass
class SpellHealAbsorbedEvent(SpellEvent):
    event_type = "SPELL_HEAL_ABSORBED"

    amount : int