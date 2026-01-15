import os
import json
import time
import random
import pandas as pd
from datetime import datetime
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

# ========= CONFIG =========
KAFKA_BROKER = os.getenv("KAFKA_BROKER")   # ex: "EC2_PUBLIC_IP:9092"
TOPIC = os.getenv("KAFKA_TOPIC")          # ex: "stock-topic"
SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", "1"))
MODE = os.getenv("MODE", "random")        # "csv" or "random"
CSV_FILE = os.getenv("CSV_FILE", "stock_data.csv")

symbols = ["AAPL", "AMZN", "GOOG", "MSFT", "TSLA"]

# ========= PRODUCER =========
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    retries=5
)

print("Producer connected to Kafka:", KAFKA_BROKER)
print("Topic:", TOPIC)
print("Mode:", MODE)


def generate_random_stock_event():
    symbol = random.choice(symbols)
    open_price = round(random.uniform(100, 350), 2)
    high_price = round(open_price + random.uniform(0, 5), 2)
    low_price = round(open_price - random.uniform(0, 5), 2)
    close_price = round(random.uniform(low_price, high_price), 2)
    volume = random.randint(10000, 5000000)

    now = datetime.utcnow()

    return {
        "symbol": symbol,
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price,
        "volume": volume,
        "event_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "year": now.strftime("%Y"),
        "month": now.strftime("%m"),
        "day": now.strftime("%d")
    }


def stream_from_csv():
    df = pd.read_csv(CSV_FILE)

    # Ensure required columns exist
    required_cols = ["symbol", "open", "high", "low", "close", "volume"]
    for col in required_cols:
        if col not in df.columns:
            raise Exception(f"Missing column in CSV: {col}")

    while True:
        for _, row in df.iterrows():
            now = datetime.utcnow()

            event = {
                "symbol": row["symbol"],
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": int(row["volume"]),
                "event_time": now.strftime("%Y-%m-%d %H:%M:%S"),
                "year": now.strftime("%Y"),
                "month": now.strftime("%m"),
                "day": now.strftime("%d")
            }

            producer.send(TOPIC, value=event)
            producer.flush()

            print("Sent:", event)
            time.sleep(SLEEP_SECONDS)


def stream_random_data():
    while True:
        event = generate_random_stock_event()

        producer.send(TOPIC, value=event)
        producer.flush()

        print( "Sent:", event)
        time.sleep(SLEEP_SECONDS)


if _name_ == "_main_":
    if MODE == "csv":
        stream_from_csv()
    else:
        stream_random_data()
