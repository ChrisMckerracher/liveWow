from src.domain.event.damage.damage_event import DamageEvent

class SpellDamageEvent(DamageEvent):
    event_type = "SPELL_DAMAGE"
