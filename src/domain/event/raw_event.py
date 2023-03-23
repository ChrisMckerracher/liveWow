import json

class RawEvent:

    def __init__(self, log: str):
        self.index_mappings = {}
        split_log = log.split(",")
        timestamp_and_event_type = split_log[0]
        timestamp_and_event_type = timestamp_and_event_type.split(" ")[1:]
        split_log = split_log[1:]

        self.index_mappings[0] = timestamp_and_event_type[0]
        self.index_mappings[1] = timestamp_and_event_type[1]

        iterator = 2
        for i in range(0, len(split_log)):
            self.index_mappings[i + iterator] = split_log[i]

    def __getitem__(self, i):
        return self.index_mappings[i]
