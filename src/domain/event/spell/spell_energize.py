from dataclasses import dataclass

from src.domain.actor.hp import HP
from src.domain.actor.position import Position
from src.domain.event.spell.spell_event import SpellEvent
from src.domain.resource.Resource import Resource


@dataclass
class SpellEnergizeEvent(SpellEvent):
    event_type = "SPELL_ENERGIZE"

    # ToDo: this is a common pattern, refactor a 'base' class
    unit_guid: str
    owner_guid: str
    hp: HP
    attack_power: int
    spell_power: int
    armor: int
    total_damage_absorbs: int
    resource: Resource
    position: Position
    map_id: str
    # todo: ???
    facing: str
    ilvl: float
    amount: int
    over_energize: int
    power_type: int
    alternate_power_type: int