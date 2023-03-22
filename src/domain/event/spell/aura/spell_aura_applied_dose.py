from dataclasses import dataclass

from src.domain.event.spell.aura.spell_aura_event import SpellAuraEvent

@dataclass
class SpellAuraAppliedDoseEvent(SpellAuraEvent):
    #ToDo: prolly not string
    amount : str
    event_type = "SPELL_AURA_APPLIED_DOSE"
