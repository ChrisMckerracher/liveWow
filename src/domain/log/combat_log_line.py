import exception.InvalidLogLine as InvalidLogLine

#ToDo: consider if it is necessary to have this class at all. It's just a nearly untranslated copy of the string. could we go straight to an Event object instead?
#In saying this, it may be useful to have this object for debugging purposes
class CombatLogLine:
    __timestamp = None

    def __init__(self, log_line: str):
        self.fields = {}
        pass

    @staticmethod
    def deserialize(log_line: str) -> CombatLogLine:
        if not CombatLogLine.is_valid_log_line(log_line):
            raise InvalidLogLine(log_line)
        pass

    @staticmethod
    def is_valid_log_line(log_line: str) -> bool:
        return True