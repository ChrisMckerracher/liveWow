from copy import copy
from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event
from src.domain.event.serialization.mapping.complex_map import ComplexMap
from src.domain.event.serialization.mapping.simple_map import SimpleMap
from src.domain.event.spell.spell_event import SpellEvent
from src.domain.spells.spell import Spell
@dataclass
class SpellAuraEvent(SpellEvent):
    # ToDo This should be an enum
    aura_type : str

    @classmethod
    def get_mapping(cls, simple_maps: list[SimpleMap], complex_maps: list[ComplexMap]) -> EventMap:
        aura_type_simple_map = SimpleMap(("aura_type", 13, str))

        simple_maps = copy(simple_maps)

        simple_maps.append(aura_type_simple_map)

        return super().get_mapping(simple_maps=simple_maps, complex_maps=complex_maps)
