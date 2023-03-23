# Tests an 'integration' of all serialization code from raw_event to processed event
import unittest

from src.domain.event.raw_event import RawEvent
from src.domain.event.serialization.event_deserializer import EventDeserializer
from src.domain.event.spell.aura.spell_aura_applied import SpellAuraAppliedEvent


class FuncTestSerialization(unittest.TestCase):

    def test_SpellAuraAppliedEvent(self):
        log_string = '1/4 11:48:42.414  SPELL_AURA_APPLIED,Player-76-05488328,"Rabbery-Sargeras",0x518,0x0,Player-76-05488328,"Rabbery-Sargeras",0x518,0x0,231390,"Trailblazer",0x1,BUFF'
        raw_event_log = RawEvent(log_string)
        spell_aura_applied_event = EventDeserializer.deserialize(raw_event_log, SpellAuraAppliedEvent)
        print(spell_aura_applied_event)



if __name__ == '__main__':
    unittest.main()