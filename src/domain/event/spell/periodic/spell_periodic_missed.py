from src.domain.event.spell.spell_event import SpellEvent


class SpellPeriodicMissed(SpellEvent):
    event_type = "SPELL_PERIODIC_MISSED"

    miss_type = int