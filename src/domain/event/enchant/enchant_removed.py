from dataclasses import dataclass

from src.domain.actor.actor import Actor
from src.domain.event.event import Event
from src.domain.item.item import Item
from src.domain.spells.spell import Spell


@dataclass
class EnchantRemovedEvent(Event):
    event_type = "ENCHANT_REMOVED"

    source : Actor
    destination : Actor
    spell : Spell
    item : Item
