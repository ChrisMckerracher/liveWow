from dataclasses import dataclass

@dataclass
class SpellSchool:

    bitmask: bytearray
    spell_school: str
    spell_school_parents: list

    def __repr__(self):
        return self.get_bitmask(), self.get_spell_family(), self.get_spell_family_parents()


#TODO: Finish spell families listings, java-enumyify this event properly
class SpellSchools:
    __spell_schools = {
                           0b00000001: SpellSchool(0b00000001, "Physical", []),
                           0b00000010: SpellSchool(0b00000010, "Holy", []),
                           0b00000100: SpellSchool(0b00000100, "Fire", []),
                       }
    @classmethod
    def get(cls, bitmask):
        return cls.__spell_schools.get(bitmask)
