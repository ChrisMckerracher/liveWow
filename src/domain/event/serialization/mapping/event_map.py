from dataclasses import dataclass
from typing import List

from src.domain.event.serialization.mapping.complex_map import ComplexMap
from src.domain.event.serialization.mapping.exception.verification_exception import VerificationException
from src.domain.event.serialization.mapping.simple_map import SimpleMap


@dataclass
class EventMap:
    simple_map : List[SimpleMap]
    complex_map : List[ComplexMap]

    #Sanity check the maps
    def verify(self):
        verification_map = {}
        self.__verify_simple_map(verification_map)
        self.__verify_complex_map(verification_map)

    def __verify_simple_map(self, verification_map):
        for i in self.simple_map:
            index = i.get_index()
            if index in verification_map:
                raise VerificationException(f"index {index} is defined more than once in the event map")
            verification_map[index] = True

    def __verify_complex_map(self, verification_map):
        for i in self.complex_map:
            for index in i.get_indices():
                if index in verification_map:
                    raise VerificationException(f"index {index} is defined more than once in the event map")
                verification_map[index] = True
