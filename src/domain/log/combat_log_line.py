import exception.InvalidLogLine as InvalidLogLine

class CombatLogLine:
    __timestamp = null

    def __init__(self, String: log_line):
        pass

    def deserialize(String: log_line):
        if not is_valid_log_line(log_line):
            raise InvalidLogLine(log_line)
        pass

    def is_valid_log_line(String: log_line):
        return True