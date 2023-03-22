from enum import Enum

from src.domain.event.spell.aura import SpellAuraAppliedEvent
from src.domain.event.spell.aura import SpellAuraAppliedDoseEvent


class Events(Enum):
    SPELL_AURA_APPLIED = SpellAuraAppliedEvent
    SPELL_AURA_APPLIED_DOSE = SpellAuraAppliedDoseEvent
