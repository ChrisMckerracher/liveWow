
class EventMapping:

    #todo: complex mapping of some indices to a resource?
    #toDo: define syntax
    def __init__(self, **kwargs):
        map.add("timestamp", 1)
        map.add("event_type", 2)
        map.add("source_guid", 3)
        map.add("source_name", 4)

        #todo: check syntax for this, i think you need to deference or something
        map = kwargs