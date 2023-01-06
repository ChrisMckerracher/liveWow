from pyflink.datastream import MapFunction


class DeserializeLogLine(MapFunction):

    def map(self, value):
        return value
