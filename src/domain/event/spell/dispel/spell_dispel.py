from dataclasses import dataclass

from src.domain.event.spell.dispel.spell_dispel_base import SpellDispelBaseEvent


@dataclass
class SpellDispelEvent(SpellDispelBaseEvent):
    event_type = "SPELL_DISPEL"

    aura_type : int