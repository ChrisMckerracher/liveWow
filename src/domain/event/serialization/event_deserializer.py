from dataclasses import dataclass

from typing import TypeVar

from src.domain.event.event import Event
from src.domain.event.serialization.mapping.complex_map import ComplexMap
from src.domain.event.serialization.mapping.simple_map import SimpleMap
from src.test import RawEvent

#ToDo: verify if the binding can work like this
T = TypeVar("T", bound=Event)
class EventDeserializer:

    @classmethod
    def deserialize(cls, log : RawEvent, event_class : T) -> T:
        event_map = T.get_mapping({})
        deserialized_mapping = {}
        # Sanity check event map before doing any more serialization work
        event_map.verify()

        simple_mappings = event_map.simple_map
        complex_mappings = event_map.complex_map
        cls.__deserialize_simple_maps(log, simple_mappings, deserialized_mapping)
        cls.__deserialize_simple_maps(log, complex_mappings, deserialized_mapping)

        return T(**deserialized_mapping)

    @classmethod
    def __deserialize_simple_maps(cls, log : RawEvent, simple_mappings : list[SimpleMap], deserialized_mapping : dict) -> None:
        for simple_map in simple_mappings:
            field_name = simple_map.get_field_name()
            index = simple_map.get_index()
            processed_class = simple_map.get_typing()

            raw_log_value = log[index]

            # ToDo: type has to be able to process string
            processed_log_value = processed_class(raw_log_value)
            deserialized_mapping[field_name] = processed_log_value

    @classmethod
    def __deserialize_complex_maps(cls, log : RawEvent, complex_mappings : list[ComplexMap], deserialized_mapping : dict) -> None:
        for complex_map in complex_mappings:
            cls.__deserialize_complex_map(log, complex_map, deserialized_mapping)

    @classmethod
    def __deserialize_complex_map(cls, log: RawEvent, complex_map : ComplexMap, deserialized_mapping : dict) -> None:
        field_name = complex_map.get_field_name()
        indices = complex_map.get_typing()
        processed_class = complex_map.get_typing()

        args = []

        for index in indices :
            args.append(log[index])

        # ToDo: type has to be able to process string
        processed_log_value = processed_class(*args)
        deserialized_mapping[field_name] = processed_log_value
