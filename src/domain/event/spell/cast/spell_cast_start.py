from src.domain.event.spell.spell_event import SpellEvent


class SpellCastStartEvent(SpellEvent):
    event_type = "SPELL_CAST_START"