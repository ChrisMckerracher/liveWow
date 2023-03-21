from dataclasses import dataclass

from src.domain.event.EventMapping import EventMapping


@dataclass
class Event():
    event_type : str

    def mapping(self) -> EventMapping:
        pass
