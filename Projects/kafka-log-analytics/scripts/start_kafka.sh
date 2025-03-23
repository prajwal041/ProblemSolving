#!/bin/bash

# Start Zookeeper
echo "Starting Zookeeper..."
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties &

# Wait for Zookeeper to start
sleep 5

# Start Kafka
echo "Starting Kafka..."
kafka-server-start /opt/homebrew/etc/kafka/server.properties &

# Wait for Kafka to start
sleep 5

# Check if Kafka is running and listening on port 9092
echo "Checking if Kafka is running..."
lsof -i :9092

# Create a logs topic
echo "Creating logs topic..."
kafka-topics --create --topic logs-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

# Verify the topic was created
echo "Listing topics..."
kafka-topics --list --bootstrap-server localhost:9092

echo "Zookeeper and Kafka started successfully!"