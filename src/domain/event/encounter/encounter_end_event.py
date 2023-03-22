from src.domain.event.encounter.encounter_event import EncounterEvent


class EncounterEndEvent(EncounterEvent):
    event_type = "ENCOUNTER_END"
