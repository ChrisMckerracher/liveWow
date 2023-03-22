from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event


@dataclass
class PartyKillEvent(Event):
    event_type = "PARTY_KILL"

    source : Actor
    destination : Actor