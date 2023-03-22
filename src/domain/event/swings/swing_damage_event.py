from src.domain.event.damage.damage_event import DamageEvent


class SwingDamageEvent(DamageEvent):
    event_type = "SWING_DAMAGE"