from dataclasses import dataclass

from src.domain.event.serialization.mapping.complex_map import ComplexMap
from src.domain.event.serialization.mapping.event_map import EventMap
from src.domain.event.serialization.mapping.simple_map import SimpleMap


@dataclass
class Event():
    event_type : str

    # ToDo: maps is in the method here so we can extend this for subclasses. this is a leaky abstraction and should be reconsidered
    @classmethod
    def get_mapping(cls, simple_maps : list[SimpleMap], complex_maps : list[ComplexMap]) -> EventMap:
        return EventMap(simple_map, complex_map)