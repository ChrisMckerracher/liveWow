from src.domain.event.damage.damage_event import DamageEvent


class SpellPeriodicDamage(DamageEvent):
    event_type = "SPELL_PERIODIC_DAMAGE"
