import json

class RawEvent:

    def __init__(self, log: str):
        split_log = log.split(",")
        timestamp_and_event_type = split_log[0]
        timestamp_and_event_type = timestamp_and_event_type.split(" ")[1:]
        self.timestamp = timestamp_and_event_type[0]
        self.event_type = timestamp_and_event_type[1]
        self.player_id = split_log[1]
        self.player_name = split_log[2]
        self.other = split_log[3:]

    def __hash__(self):
        return hash((self.timestamp, self.event_type, self.player_id))

    def __str__(self):
        return str(json.dumps(self.__dict__))



if __name__ == "__main__":
    new_event = RawEvent('1/4 11:48:42.414  SPELL_AURA_APPLIED,Player-76-05488328,"Rabbery-Sargeras",0x518,0x0,Player-76-05488328,"Rabbery-Sargeras",0x518,0x0,231390,"Trailblazer",0x1,BUFF')
    print(hash(new_event))
    print(str(new_event))
