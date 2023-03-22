from dataclasses import dataclass

from src.domain.event.spell.aura.spell_aura_event import SpellAuraEvent

@dataclass
class SpellAuraRemovedDoseEvent(SpellAuraEvent):
    event_type = "SPELL_AURA_REMOVED_DOSE"
