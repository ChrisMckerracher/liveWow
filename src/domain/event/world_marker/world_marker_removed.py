from dataclasses import dataclass

from src.domain.event.event import Event


@dataclass
class WorldMarkerRemovedEvent(Event):
    event_type = "WORLD_MARKER_REMOVED"

    marker_id : str
