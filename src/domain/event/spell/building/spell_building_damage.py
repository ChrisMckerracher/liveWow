from src.domain.event.spell.spell_event import SpellEvent


class SpellBuildingDamageEvent(SpellEvent):
    event_type = "SPELL_BUILDING_DAMAGE"