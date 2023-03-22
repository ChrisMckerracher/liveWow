from src.domain.actor.actor import Actor
from src.domain.actor.hp import HP
from src.domain.actor.position import Position
from src.domain.event.event import Event
from src.domain.resource.Resource import Resource
from src.domain.spells.spell import Spell


@dataclass
class SpellHealBase(Event):
    source : Actor
    destination : Actor
    spell : Spell
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
    unmitigated_amount: int
    overheal: int
    absorbed: int
    critical: int