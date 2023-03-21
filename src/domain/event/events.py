from enum import Enum

from src.domain.spells.aura.spell_aura_applied import SpellAuraAppliedEvent
from src.domain.spells.aura.spell_aura_applied_dose import SpellAuraAppliedDoseEvent


class Events(Enum):
    SPELL_AURA_APPLIED = SpellAuraAppliedEvent
    SPELL_AURA_APPLIED_DOSE = SpellAuraAppliedDoseEvent
