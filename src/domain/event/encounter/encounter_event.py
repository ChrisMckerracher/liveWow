from dataclasses import dataclass

from src.domain.encounter.encounter import Encounter
from src.domain.event.event import Event

@dataclass
class EncounterEvent(Event):
    encounter : Encounter