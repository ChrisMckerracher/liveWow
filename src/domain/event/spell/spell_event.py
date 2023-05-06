from copy import copy
from dataclasses import dataclass
from typing import List

from src.domain.event.serialization.mapping.complex_map import ComplexMap
from src.domain.event.serialization.mapping.event_map import EventMap
from src.domain.event.serialization.mapping.simple_map import SimpleMap
from src.domain.spells.spell import Spell
from src.domain.event.event import Event
from src.domain.actor.actor import Actor


#ToDo: take into account that we need to track actual outcomes like numerically how much damage was done. this can possibly be done inside spell outcome
@dataclass
class SpellEvent(Event):
    caster: Actor
    target: Actor
    spell: Spell

    @classmethod
    def get_mapping(cls, simple_maps : List[SimpleMap], complex_maps : List[ComplexMap]) -> EventMap:
        caster_complex_map = ComplexMap(("caster", [SimpleMap(("id", 2, str)), SimpleMap(("name", 3, str)), SimpleMap(("flags", 4, str)), SimpleMap(("raid_flags", 5, str))], Actor))
        target_complex_map = ComplexMap(("target", [SimpleMap(("id", 6, str)), SimpleMap(("name", 7, str)), SimpleMap(("flags", 8, str)), SimpleMap(("raid_flags", 9, str))], Actor))
        spell_complex_map = ComplexMap(("spell", [SimpleMap(("id", 10, str)), SimpleMap(("name", 11, str)), SimpleMap(("school", 12, str))], Spell))

        complex_maps = copy(complex_maps)

        complex_maps.append(caster_complex_map)
        complex_maps.append(target_complex_map)
        complex_maps.append(spell_complex_map)

        return super().get_mapping(simple_maps = simple_maps, complex_maps = complex_maps)
