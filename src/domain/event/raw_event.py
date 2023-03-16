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
