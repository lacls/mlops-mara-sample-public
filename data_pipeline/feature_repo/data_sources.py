from datetime import timedelta

from feast import FileSource, KafkaSource
from feast.data_format import JsonFormat, ParquetFormat

driver_stats_parquet_file = "../data_sources/network_attack.parquet" ##change here

driver_stats_batch_source = FileSource(
    name="network_attack", ##
    file_format=ParquetFormat(),
    path=driver_stats_parquet_file,
    timestamp_field="datetime",
    created_timestamp_column="created",
)

driver_stats_stream_source = KafkaSource(
    name="network_attack_stream",
    kafka_bootstrap_servers="localhost:29092",
    topic="network",
    timestamp_field="datetime",
    batch_source=driver_stats_batch_source,
    message_format=JsonFormat(
        schema_json="\
        attck_id string,\
        feature1 double,\
        feature2 string,\
        label integer,\
        created timestamp"
    ),
    watermark_delay_threshold=timedelta(minutes=5),
    description="The Kafka stream containing the network stats",
)
