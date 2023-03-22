from dataclasses import dataclass

from src.domain.spells.spell import Spell
from src.domain.event.event import Event
from src.domain.actor.actor import Actor


#ToDo: take into account that we need to track actual outcomes like numerically how much damage was done. this can possibly be done inside spell outcome
@dataclass
class SpellEvent(Event):
    caster: Actor
    target: Actor
    spell: Spell
