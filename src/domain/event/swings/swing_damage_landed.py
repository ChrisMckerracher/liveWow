from src.domain.event.damage.damage_event import DamageEvent


class SwingDamageLandaedEvent(DamageEvent):
    event_type = "SWING_DAMAGE_LANDED"