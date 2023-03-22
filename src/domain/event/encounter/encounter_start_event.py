from src.domain.event.encounter.encounter_event import EncounterEvent

class EncounterStartEvent(EncounterEvent):
    event_type = "ENCOUNTER_START"