from dataclasses import dataclass


#TODO: finishi this event with the same structure for spell school
@dataclass
class SpellOutcome:
    #ex: _DAMAGE or _HEAL_ABSORBED
    outcome: str