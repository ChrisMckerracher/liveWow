from dataclasses import dataclass

from src.domain.actor.position import Position
from src.domain.event.event import Event


@dataclass
class WorldMarkerPlacedEvent(Event):
    event_type = "WORLD_MARKER_PLACED"

    map_id: str
    marker_id: str
    position: Position