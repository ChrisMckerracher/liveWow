from src.domain.event.spell.spell_event import SpellEvent

class SpellCreateEvent(SpellEvent):
    event_type = "SPELL_CREATE"