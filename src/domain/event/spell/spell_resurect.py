from src.domain.event.spell.spell_event import SpellEvent


class SpellResurrectEvent(SpellEvent):
    event_type = "SPELL_RESURRECT"
