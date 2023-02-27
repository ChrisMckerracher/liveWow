from dataclasses import dataclass

from .spell import Spell
from .spell_outcome import SpellOutcome
from ..event.event import Event
from ..actor.actor import Actor


#ToDo: take into account that we need to track actual outcomes like numerically how much damage was done. this can possibly be done inside spell outcome
@dataclass
class SpellEvent(Event):
    caster: Actor
    target: Actor
    spell: Spell
    spell_outcome: SpellOutcome
