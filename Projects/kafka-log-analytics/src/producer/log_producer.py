from kafka import KafkaProducer
import time, random, json, sys, os
# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.config.config import KAFKA_CONFIG, PRODUCER_CONFIG


def generate_log():
    """Generate a log entry."""
    log_level = random.choice(PRODUCER_CONFIG["log_levels"])
    message = random.choice(PRODUCER_CONFIG["messages"])
    return json.dumps({
        "timestamp": int(time.time()),
        "level": log_level,
        "message": message
    })

def main():
    producer = KafkaProducer(bootstrap_servers=KAFKA_CONFIG["bootstrap_servers"])
    try:
        while True:
            log_entry = generate_log()
            producer.send(KAFKA_CONFIG["topic_name"], log_entry.encode("utf-8"))
            print(f"---Sent: {log_entry}---")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Producer Stopped")

if __name__ == "__main__":
    main()