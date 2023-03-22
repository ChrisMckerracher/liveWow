from src.domain.event.event import Event


class EncounterEvent(Event):
    event_types = ["encounter.start",
                   "encounter.end"
                   ]
    pass