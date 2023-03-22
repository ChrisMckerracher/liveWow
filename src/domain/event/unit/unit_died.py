from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event

@dataclass
class UnitDiedEvent(Event):
    event_type = "UNIT_DIED"

    source : Actor
    destination : Actor
    recap_id : str
