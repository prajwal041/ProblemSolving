# Prerequisites
    Before starting, ensure you have the following installed:
    Apache Kafka (with Zookeeper)
    Apache Spark (with Spark Streaming support)
    Java (JDK 8 or higher)
    Scala or Python (for Spark code)
    A log generator or sample log files for testing

# 2. Architecture Overview
    Log Producer: Generates log data and sends it to Kafka.
    Kafka: Acts as a message broker to ingest and store log data.
    Spark Streaming: Consumes log data from Kafka and processes it in real-time.
    Output: Store processed data in a database (e.g., HDFS, Cassandra, or MySQL) or visualize it using tools like Grafana or Kibana.

# 3. Setup - Manual
    Start zookeeper first:
    zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties

    Once Zookeeper is running, start Kafka in different terminal:
    kafka-server-start /opt/homebrew/etc/kafka/server.properties

    Check if Kafka is running and listening on port 9092:
    lsof -i :9092

# 4. Test Kafka
    Create a test topic, produce messages, and consume them to verify everything is working:

    Create a test topic:
    kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
    
    Produce messages:
    kafka-console-producer --topic test-topic --bootstrap-server localhost:9092

    Type a few messages and press Ctrl+D to exit
    
    Consume messages:
    kafka-console-consumer --topic test-topic --from-beginning --bootstrap-server localhost:9092

    You should see the messages you produced earlier.

# Start the Kafka & Zookeeper - Terminal 1
    $ ./scripts/start_kafka.sh
        You should see topics created with zookeeper

# Send messages via Producer - Terminal 2
    $ python3 src/producer/log_producer.py
        You should see message sent

# Collect the data via Spark Consumer - Terminal 3
    $ spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 src/spark_streaming/log_analytics.py
        Logs are collected in output/ directory in parquet & json file format
        Spark checksums data is collected in checkpoints/ directory
    
# Stop the service
    In Terminal 3: ctrl + c: stop the consumer
    In Terminal 2: ctrl + c: stop the producer
    In Terminal 3: kafka-server-stop
                   zookeeper-server-stop
        This stops kafka & zookeeper connections
    