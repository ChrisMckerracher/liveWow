from pyflink.common import Duration, WatermarkStrategy, Encoder
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.file_system import FileSource, StreamFormat, OutputFileConfig
from pyflink.datastream.connectors.number_seq import NumberSequenceSource

from source.timestamp.LogLineTimestampSupplier import LogLineTimestampSupplier
from stream.map.DeserializeLogLine import DeserializeLogLine
from pyflink.datastream.connectors.file_system import StreamingFileSink

"""
you need grpc installed else its all fucked 
grpcio-tools
if youre on the py version im on 3.8.x, downgraded protobuf to 3.20.0
 flink run \
      -pyclientexec /Users/chris/.pyenv/versions/liveWow/bin/python \
      -pyexec /Users/chris/.pyenv/versions/liveWow/bin/python \
      -py topology.py
"""

output_path = "../"
test_log = "/Users/chris/Code/liveWow/testlog.txt"
def topology():
    test = DeserializeLogLine()
    print(test.__class__)
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    source = FileSource.for_record_stream_format(StreamFormat.text_line_format(), test_log) \
        .monitor_continuously(Duration.of_millis(10)) \
        .build()
    seq_num_source = NumberSequenceSource(1, 1000)

    #ds = env.from_source(source=seq_num_source,watermark_strategy=WatermarkStrategy.for_monotonous_timestamps(),source_name='seq_num_source',type_info=Types.LONG())

    initStream = env.from_source(source, WatermarkStrategy.no_watermarks()\
                             .with_timestamp_assigner(LogLineTimestampSupplier()), "file-source")

    testStream = initStream.map(lambda x: x)#DeserializeLogLine())

    dummySink = StreamingFileSink.for_row_format(output_path, Encoder.simple_string_encoder()) \
        .with_output_file_config(
        OutputFileConfig.builder().with_part_prefix('pre').with_part_suffix('suf').build()) \
        .build()

    testStream.add_sink(dummySink)

    env.execute('topology')


if __name__ == '__main__':
    topology()