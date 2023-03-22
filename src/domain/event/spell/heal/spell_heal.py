from dataclasses import dataclass

from src.domain.event.heal.spell_heal_base import SpellHealBase


@dataclass
class SpellHealEvent(SpellHealBase):
    event_type = "SPELL_HEAL"