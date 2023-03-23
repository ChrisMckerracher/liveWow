from dataclasses import dataclass

from src.domain.event.serialization.mapping.event_map import EventMapping


@dataclass
class Event():
    event_type : str

    def mapping(self, maps : dict) -> EventMapping:
        return EventMapping(**maps)
