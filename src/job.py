from pyflink.common import Duration, WatermarkStrategy, Encoder, Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.file_system import FileSource, StreamFormat, OutputFileConfig, FileSourceBuilder
from pyflink.datastream.connectors.number_seq import NumberSequenceSource

from source.timestamp.LogLineTimestampSupplier import LogLineTimestampSupplier
# from stream.map.DeserializeLogLine import DeserializeLogLine
from pyflink.datastream.connectors.file_system import StreamingFileSink

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
def job():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    source = FileSource.for_record_stream_format(StreamFormat.text_line_format(), test_log) \
        .monitor_continuously(Duration.of_millis(100)) \
        .build()

    #ds = env.from_source(source=source,watermark_strategy=WatermarkStrategy.for_monotonous_timestamps(),source_name='seq_num_source',type_info=Types.LONG())



    initStream = env.from_source(source, WatermarkStrategy.no_watermarks()\
                             .with_timestamp_assigner(LogLineTimestampSupplier()), "file-source")

    testStream = initStream.map(lambda x : raiseTest(x))

    dummySink = StreamingFileSink.for_row_format(output_path, Encoder.simple_string_encoder()) \
        .with_output_file_config(
        OutputFileConfig.builder().with_part_prefix('pre').with_part_suffix('suf').build()) \
        .build()

    testStream.add_sink(dummySink)

    env.execute('job')


if __name__ == '__main__':
    job()