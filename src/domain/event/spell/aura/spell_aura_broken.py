from dataclasses import dataclass

from src.domain.event.spell.aura.spell_aura_event import SpellAuraEvent
from src.domain.spells.spell import Spell


@dataclass
class SpellAuraBrokenEvent(SpellAuraEvent):
    breaker_spell : Spell
    event_type = "SPELL_AURA_BROKEN"
