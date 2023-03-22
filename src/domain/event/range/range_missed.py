from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event
from src.domain.spells.spell import Spell


@dataclass
class RangeMissedEvent(Event):
    event_type = "RANGE_MISSED"

    source : Actor
    destination : Actor
    spell : Spell
    #ToDo: not sure what miss type is yet
    missType : int
    is_off_hand : bool
    amount_missed : int
    critical : int
    unmitigated_amount : int