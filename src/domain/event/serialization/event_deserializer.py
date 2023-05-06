from dataclasses import dataclass

from typing import TypeVar, List

from src.domain.event.event import Event
from src.domain.event.raw_event import RawEvent
from src.domain.event.serialization.mapping.complex_map import ComplexMap
from src.domain.event.serialization.mapping.simple_map import SimpleMap

#ToDo: verify if the binding can work like this
T = TypeVar("T", bound=Event)
class EventDeserializer:

    @classmethod
    def deserialize(cls, log : RawEvent, event_class : T) -> T:
        event_map = event_class.get_mapping([], [])
        deserialized_mapping = {}
        # Sanity check event map before doing any more serialization work
        event_map.verify()

        simple_mappings = event_map.simple_map
        complex_mappings = event_map.complex_map
        cls.__deserialize_simple_maps(log, simple_mappings, deserialized_mapping)
        cls.__deserialize_complex_maps(log, complex_mappings, deserialized_mapping)
        print(deserialized_mapping)

        return event_class(**deserialized_mapping)

    @classmethod
    def __deserialize_simple_maps(cls, log : RawEvent, simple_mappings : List[SimpleMap], deserialized_mapping : dict) -> None:
        for simple_map in simple_mappings:
            field_name = simple_map.get_field_name()
            deserialized_mapping[field_name] = cls.__deseriliaze_simple_map(log, simple_map)

    @classmethod
    def __deseriliaze_simple_map(cls, log: RawEvent, simple_map: SimpleMap):
        index = simple_map.get_index()
        processed_class = simple_map.get_typing()

        raw_log_value = log[index]

        return processed_class(raw_log_value)

    @classmethod
    def __deserialize_complex_maps(cls, log : RawEvent, complex_mappings : List[ComplexMap], deserialized_mapping : dict) -> None:
        for complex_map in complex_mappings:
            cls.__deserialize_complex_map(log, complex_map, deserialized_mapping)

    @classmethod
    def __deserialize_complex_map(cls, log: RawEvent, complex_map : ComplexMap, deserialized_mapping : dict) -> None:
        field_name = complex_map.get_field_name()
        simple_maps = complex_map.get_maps()
        processed_class = complex_map.get_typing()

        kargs = {}

        for simple_map in simple_maps:
            simple_field_name = simple_map.get_field_name()
            processed_value = cls.__deseriliaze_simple_map(log, simple_map)
            kargs[simple_field_name] = processed_value

        # ToDo: type has to be able to process string
        processed_log_value = processed_class(**kargs)
        deserialized_mapping[field_name] = processed_log_value
