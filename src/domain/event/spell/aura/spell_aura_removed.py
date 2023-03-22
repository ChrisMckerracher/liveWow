from dataclasses import dataclass

from src.domain.event.spell.aura.spell_aura_event import SpellAuraEvent

@dataclass
class SpellAuraRemovedEvent(SpellAuraEvent):
    #ToDo: should this be a string?
    amount : str
    event_type = "SPELL_AURA_REMOVED"
