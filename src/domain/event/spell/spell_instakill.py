from src.domain.event.spell.spell_event import SpellEvent


class SpellInstakillEvent(SpellEvent):
    event_type = "SPELL_INSTAKILL"