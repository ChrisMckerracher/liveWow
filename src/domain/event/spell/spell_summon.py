from src.domain.event.spell.spell_event import SpellEvent


class SpellSummongEvent(SpellEvent):
    event_type = "SPELL_SUMMON"
