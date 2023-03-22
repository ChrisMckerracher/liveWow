from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event

@dataclass
class UnitDestroyedEvent(Event):
    event_type = "UNIT_DESTROYED"

    source : Actor
    destination : Actor
    recap_id : str
    unconscious_on_death : bool