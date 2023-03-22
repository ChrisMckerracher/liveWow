from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event


@dataclass
class SwingMissed(Event):
    source : Actor
    destination : Actor
    miss_type : int