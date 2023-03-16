from pyflink.common import Duration, WatermarkStrategy, Encoder, Types
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors.file_system import FileSource, StreamFormat, OutputFileConfig, FileSourceBuilder
from pyflink.datastream.connectors.number_seq import NumberSequenceSource
import logging

from source.timestamp.LogLineTimestampSupplier import LogLineTimestampSupplier
# from stream.map.DeserializeLogLine import DeserializeLogLine
from pyflink.datastream.connectors.file_system import StreamingFileSink

from domain.event.raw_event import RawEvent

"""
you need grpc installed else its all fucked
grpcio-tools
if youre on the py version im on 3.8.x, downgraded protobuf to 3.20.0
 flink run \
      -pyclientexec /Users/chris/.pyenv/versions/liveWow/bin/python \
      -pyexec /Users/chris/.pyenv/versions/liveWow/bin/python \
      -py job.py
"""

output_path = "../"
test_log = "/opt/liveWow/testlog.txt"

def raiseTest(x):
    raise Exception(x)
def testDebug(x):
    logging.warning(x)
    return x

def job():
    env = StreamExecutionEnvironment.get_execution_environment()
    source = FileSource\
        .for_record_stream_format(StreamFormat.text_line_format(), test_log) \
        .monitor_continuously(Duration.of_seconds(1)) \
        .build()

    initStream = env.from_source(source, WatermarkStrategy.no_watermarks(), "file-source")

    testStream = initStream.map(lambda raw_string: RawEvent(raw_string))\
        .key_by(lambda raw_event: hash(raw_event))


    #toDo: files arent actually being written
    dummySink = StreamingFileSink.for_row_format(output_path, Encoder.simple_string_encoder()) \
        .with_output_file_config(
        OutputFileConfig.builder().with_part_prefix('pre').with_part_suffix('suf').build()) \
        .build()

    testStream\
        .add_sink(dummySink)

    env.execute('job')


if __name__ == '__main__':
    job()