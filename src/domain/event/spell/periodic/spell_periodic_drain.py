from src.domain.event.spell.spell_event import SpellEvent


class SpellPeriodicDrain(SpellEvent):
    event_type = "SPELL_PERIODIC_DRAIN"