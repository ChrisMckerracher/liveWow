from src.domain.event.heal.spell_heal_base import SpellHealBase


class SpellPeriodicHeal(SpellHealBase):
    event_type = "SPELL_PERIODIC_HEAL"
