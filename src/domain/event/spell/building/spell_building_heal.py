from src.domain.event.spell.spell_event import SpellEvent


class SpellBuildingHealEvent(SpellEvent):
    event_type = "SPELL_BUILDING_HEAL"