from pyflink.common import WatermarkStrategy, Encoder
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors.file_system import FileSource, StreamFormat, OutputFileConfig, FileSourceBuilder
from pyflink.datastream.connectors.file_system import FileSink, OutputFileConfig, RollingPolicy
from pyflink.datastream.connectors.number_seq import NumberSequenceSource
import logging

from source.timestamp.LogLineTimestampSupplier import LogLineTimestampSupplier
# from stream.map.DeserializeLogLine import DeserializeLogLine
from pyflink.datastream.connectors.file_system import StreamingFileSink

#https://stackoverflow.com/questions/70020100/import-local-packages-inside-pyflink
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

output_path = "/opt/output"
test_log = "/opt/liveWow/testlog.txt"

def map_test(input):
    return input[0:10]

def job():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.enable_checkpointing(100)
    ds = env.from_source(
        source=FileSource.for_record_stream_format(StreamFormat.text_line_format(),
                                                   test_log)
                         .process_static_file_set().build(),
        watermark_strategy=WatermarkStrategy.for_monotonous_timestamps(),
        source_name="file_source"
    )

    testStream = ds.map(lambda raw_string: RawEvent(raw_string))\
        .key_by(lambda raw_event: hash(raw_event))\
        .map(lambda raw_event: str(raw_event), output_type=Types.STRING())\

    testStream.sink_to(
        sink=FileSink.for_row_format(
            base_path=output_path,
            encoder=Encoder.simple_string_encoder())
        .with_output_file_config(
            OutputFileConfig.builder()
            .with_part_prefix("prefix")
            .with_part_suffix(".ext")
            .build())
        .with_rolling_policy(RollingPolicy.default_rolling_policy())
        .build()
    )

    env.execute('job')

if __name__ == '__main__':
    job()