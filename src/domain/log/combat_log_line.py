import exception.InvalidLogLine as InvalidLogLine

class CombatLogLine:
    __timestamp = None

    def __init__(self, log_line: str):
        pass

    @staticmethod
    def deserialize(log_line: str):
        if not CombatLogLine.is_valid_log_line(log_line):
            raise InvalidLogLine(log_line)
        pass

    @staticmethod
    def is_valid_log_line(log_line: str):
        return True