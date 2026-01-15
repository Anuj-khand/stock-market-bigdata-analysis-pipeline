# 📈 Stock Market Real-Time ETL Pipeline using Kafka + AWS

This project simulates a *real-time stock market streaming pipeline* using *Apache Kafka* and AWS services.  
Stock market events are produced continuously, streamed through Kafka, stored in an *Amazon S3 data lake, cataloged using **AWS Glue, queried with **Amazon Athena, and visualized using **Amazon QuickSight*.

---

## 🚀 Project Objective
To build an end-to-end *big data streaming pipeline* that demonstrates real-time ingestion, storage, cataloging, querying, and dashboarding.

---

## 🏗️ Architecture
Producer → Kafka (EC2) → Consumer → S3 → Glue Crawler → Athena → QuickSight Dashboard

📌 Architecture Diagram:  
![Architecture](architecture/architecture.png)

---

## 🛠️ Tech Stack
- *Python*
- *Apache Kafka*
- *AWS EC2*
- *Amazon S3*
- *AWS Glue (Crawler + Data Catalog)*
- *Amazon Athena*
- *Amazon QuickSight*

---

## 📂 Repository Structure

```bash
.
├── producer/
│   ├── kafka_producer_realtime.py
│   ├── requirements.txt
│   ├── config.example.env
│   └── README.md
│
├── consumer/
│   ├── kafka_consumer_to_s3.py
│   ├── requirements.txt
│   ├── config.example.env
│   └── README.md
│
├── glue/
│   ├── README.md
│   ├── crawler_config.md
│   ├── table_schema.md
│   ├── permissions.md
│   └── athena_queries.sql
│
└── architecture/
    ├── architecture.png
    └── dashboard_preview.png



**Sample Kafka Event (JSON)**
Json
{
  "symbol": "AAPL",
  "open": 179.0,
  "high": 180.09,
  "low": 178.36,
  "close": 178.85,
  "volume": 218029,
  "event_time": "2026-01-12T17:41:44.425Z"
}
**⚙️ How to Run the Project**
1️⃣** Start Kafka on EC2**
Install Kafka on EC2
Start Zookeeper + Kafka Broker
Create Kafka topic
2️⃣ **Run Producer (Local / Laptop)**
Copy code
Bash
cd producer
pip install -r requirements.txt
python kafka_producer_realtime.py
3️⃣ **Run Consumer (EC2) → Store data in S3**
Copy code
Bash
cd consumer
pip install -r requirements.txt
python kafka_consumer_to_s3.py
4️⃣ **Run Glue Crawler**
AWS Glue crawler scans the S3 data
Creates a table in AWS Glue Data Catalog
5️⃣ **Query Data in Athena**
Example:
Sql
SELECT *
FROM stock_bigdata_db.stock_market_events
LIMIT 10;
6️⃣** QuickSight Dashboard**
Created a QuickSight dashboard with:
KPI cards (Total Records, Total Volume, Avg Close, Highest Price)
Stock closing price trend over time
Volume trend over time
Stock-wise comparisons

📌 **Dashboard Preview:**

📊 **Key Analytics Performed**
Total stock events ingested
Average closing price by stock symbol
Total traded volume by stock
High/Low volatility comparison
Time-series trends for stock movement
💰** Cost Note**
After pipeline completion, EC2 can be stopped to avoid additional costs.
S3 + Glue + Athena metadata will remain available for querying and dashboards.
