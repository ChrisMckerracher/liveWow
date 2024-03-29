from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.actor.hp import HP
from src.domain.actor.position import Position
from src.domain.event.spell.spell_event import SpellEvent
from src.domain.resource.Resource import Resource
from src.domain.spells.spell import Spell


@dataclass
class SpellDrainEvent(SpellEvent):
    event_type = "SPELL_DRAIN"

    #ToDo: this is a common pattern, refactor a 'base' class
    unit_guid : str
    owner_guid : str
    hp : HP
    attack_power : int
    spell_power : int
    armor : int
    total_damage_absorbs : int
    resource : Resource
    position : Position
    map_id : str
    #todo: ???
    facing : str
    ilvl : float
    amount : int
    power : int
    extra : int
    gained : int