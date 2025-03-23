# Kafka Configuration
KAFKA_CONFIG = {
    "bootstrap_servers": "localhost:9092",  # Kafka broker address
    "topic_name": "logs",                   # Kafka topic for log data
    "group_id": "log-analytics-group",     # Consumer group ID
    "auto_offset_reset": "latest",         # Start reading from the latest offset
    "enable_auto_commit": False            # Disable auto-commit for offsets
}

# Spark Configuration
SPARK_CONFIG = {
    "app_name": "LogAnalytics",            # Spark application name
    "master": "local[*]",                  # Spark master URL
    "batch_duration": 10,                  # Batch duration in seconds
    "checkpoint_dir": "checkpoints"         # Directory for Spark Streaming checkpoints
}

# Log Producer Configuration
PRODUCER_CONFIG = {
    "log_levels": ["INFO", "WARN", "ERROR", "DEBUG"],  # Log levels for random generation
    "messages": [                                      # Sample log messages
        "User logged in",
        "Failed login attempt",
        "Database connection lost",
        "Cache cleared",
        "Request processed successfully"
    ],
    "sleep_interval": 1                               # Time interval between logs (in seconds)
}

# Output Configuration
OUTPUT_CONFIG = {
    "output_dir": "output/log_counts",                # Directory to store processed logs
    "visualization_tool": "console"                  # Options: "console", "elasticsearch", "grafana"
}

# Logging Configuration
LOGGING_CONFIG = {
    "log_file": "logs/app.log",                       # Log file path
    "log_level": "INFO"                               # Logging level (DEBUG, INFO, WARN, ERROR)
}