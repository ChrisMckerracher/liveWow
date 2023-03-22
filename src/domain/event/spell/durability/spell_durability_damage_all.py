from src.domain.event.spell.spell_event import SpellEvent


class SpellDurabilityDamageAllEvent(SpellEvent):
    event_type = "SPELL_DURABILITY_DAMAGE_ALL"