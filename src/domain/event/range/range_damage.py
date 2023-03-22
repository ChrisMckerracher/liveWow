from src.domain.event.damage.damage_event import DamageEvent


class RangeDamageEvent(DamageEvent):
    event_type = "RANGE_DAMAGE"
