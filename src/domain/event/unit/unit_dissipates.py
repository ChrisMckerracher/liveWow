from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event

@dataclass
class UnitDissipatesEvent(Event):
    event_type = "UNIT_DISSIPATES"

    source : Actor
    destination : Actor
    recap_id : str
    unconscious_on_death : bool