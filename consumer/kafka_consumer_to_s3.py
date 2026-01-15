import os
import json
import time
import boto3
from kafka import KafkaConsumer
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# ========== CONFIG ==========
KAFKA_BROKER = os.getenv("KAFKA_BROKER")        # ex: "EC2_PUBLIC_IP:9092"
TOPIC = os.getenv("KAFKA_TOPIC")               # ex: "stock-topic"
GROUP_ID = os.getenv("KAFKA_GROUP_ID", "stock-consumer-group")

S3_BUCKET = os.getenv("S3_BUCKET")             # ex: "stock-market-datalake-anuj"
S3_PREFIX = os.getenv("S3_PREFIX", "stock_data")

BATCH_SIZE = int(os.getenv("BATCH_SIZE", "50"))     # upload every 50 records
SLEEP_SECONDS = int(os.getenv("SLEEP_SECONDS", "2"))

s3 = boto3.client("s3")

def upload_to_s3(records):
    """
    Upload records as a JSON file into S3 partitioned folders:
    year=YYYY/month=MM/day=DD/
    """
    now = datetime.utcnow()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    filename = f"{int(time.time())}.json"
    key = f"{S3_PREFIX}/year={year}/month={month}/day={day}/{filename}"

    body = "\n".join([json.dumps(r) for r in records])

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=body.encode("utf-8")
    )

    print(f"Uploaded {len(records)} records to s3://{S3_BUCKET}/{key}")


def main():
    print("Starting Kafka Consumer...")

    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=[KAFKA_BROKER],
        auto_offset_reset="latest",
        enable_auto_commit=True,
        group_id=GROUP_ID,
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )

    print(f"Connected to Kafka topic: {TOPIC}")

    buffer = []

    for msg in consumer:
        record = msg.value
        buffer.append(record)

        print("Received:", record)

        # Upload when buffer reaches batch size
        if len(buffer) >= BATCH_SIZE:
            upload_to_s3(buffer)
            buffer = []
            time.sleep(SLEEP_SECONDS)


if _name_ == "_main_":
    main()
