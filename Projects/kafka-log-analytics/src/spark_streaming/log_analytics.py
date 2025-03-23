from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, current_timestamp, lit, to_timestamp, window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
import json, os, sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.config.config import KAFKA_CONFIG, SPARK_CONFIG, OUTPUT_CONFIG

# Define the schema for the log data
log_schema = StructType([
    StructField("timestamp", IntegerType(), True),  # Unix epoch time in seconds
    StructField("level", StringType(), True),
    StructField("message", StringType(), True)
])

# Define the schema for batch-wise statistics
stats_schema = StructType([
    StructField("batch_id", StringType(), True),  # Unique ID for each batch
    StructField("batch_timestamp", TimestampType(), True),  # Timestamp of the batch
    StructField("level", StringType(), True),  # Log level
    StructField("count", IntegerType(), True)  # Count of log level
])

def save_stats_to_file(batch_df, batch_id):
    """
    Save batch-wise statistics to a file.
    """
    print(f"Processing batch {batch_id}")  # Debugging statement
    if not batch_df.isEmpty():
        print(f"Saving batch {batch_id} to file")  # Debugging statement
        # Convert DataFrame to JSON and save to a file
        stats_path = os.path.join(OUTPUT_CONFIG["output_dir"], f"batch_{batch_id}.json")
        batch_df.toPandas().to_json(stats_path, orient="records", lines=True)
    else:
        print(f"Batch {batch_id} is empty")  # Debugging statement

def main():
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName(SPARK_CONFIG["app_name"]) \
        .master(SPARK_CONFIG["master"]) \
        .getOrCreate()

    # Read data from Kafka
    kafka_stream = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_CONFIG["bootstrap_servers"]) \
        .option("subscribe", KAFKA_CONFIG["topic_name"]) \
        .option("startingOffsets", "earliest") \
        .load()

    # Parse the Kafka data
    parsed_stream = kafka_stream \
        .select(from_json(col("value").cast("string"), log_schema).alias("data")) \
        .select("data.*")

    # Convert the timestamp field to TimestampType
    parsed_stream = parsed_stream \
        .withColumn("timestamp", to_timestamp(col("timestamp")))  # Convert Unix epoch time to timestamp

    # Add a watermark to handle late-arriving data
    watermarked_stream = parsed_stream \
        .withWatermark("timestamp", "10 minutes")  # 10-minute watermark

    # Perform windowed aggregation
    windowed_counts = watermarked_stream \
        .groupBy(
            window(col("timestamp"), "10 minutes"),  # 10-minute window
            col("level")
        ) \
        .count()

    # Add batch ID and timestamp to the log counts
    batch_stats = windowed_counts \
        .withColumn("batch_id", lit(str(id(windowed_counts)))) \
        .withColumn("batch_timestamp", current_timestamp())

    # Write batch-wise statistics to a file (using Append mode)
    batch_stats.writeStream \
        .format("json") \
        .option("path", "output/log_counts_json") \
        .option("checkpointLocation", "checkpoints/log_counts_json") \
        .outputMode("append").start()

    batch_stats.writeStream \
        .format("parquet") \
        .option("path", "output/log_counts_parquet") \
        .option("checkpointLocation", "checkpoints/log_counts_parquet") \
        .outputMode("append").start()

    # Write the output to the console (using Complete mode)
    query = batch_stats \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    main()