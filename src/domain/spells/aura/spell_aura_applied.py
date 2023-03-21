from dataclasses import dataclass

from src.domain.event.EventMapping import EventMapping
from src.domain.spells.aura.spell_aura_event import SpellAuraEvent

@dataclass
class SpellAuraAppliedEvent(SpellAuraEvent):
    event_type = "SPELL_AURA_APPLIED"


