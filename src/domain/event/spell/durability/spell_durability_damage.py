from src.domain.event.spell.spell_event import SpellEvent


class SpellDurabilityDamageEvent(SpellEvent):
    event_type = "SPELL_DURABILITY_DAMAGE"