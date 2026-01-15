**⚙️ How to Run the Project**

1️⃣ Start Kafka on EC2

Install Kafka on EC2
Start Zookeeper + Kafka Broker
Create Kafka topic

2️⃣ Run Producer (Local / Laptop)
Bash
cd producer
pip install -r requirements.txt
python kafka_producer_realtime.py

3️⃣ Run Consumer (EC2) → Store data in S3
Copy code
Bash
cd consumer
pip install -r requirements.txt
python kafka_consumer_to_s3.py

4️⃣ Run Glue Crawler
AWS Glue crawler scans the S3 data
Creates a table in AWS Glue Data Catalog
5️⃣ Query Data in Athena
Example:
Copy code
Sql
SELECT *
FROM stock_bigdata_db."1768239694912_json"
LIMIT 10;
6️⃣ QuickSight Dashboard
Created a QuickSight dashboard with:
KPI cards (Total Records, Total Volume, Avg Close, Highest Price)
Stock closing price trend over time
Volume trend over time
Stock-wise comparisons
📌 Dashboard Preview:
�
📊 Key Analytics Performed
Total stock events ingested
Average closing price by stock symbol
Total traded volume by stock
High/Low volatility comparison
Time-series trends for stock movement
💰 Cost Note
After pipeline completion, EC2 can be stopped to avoid additional costs.
S3 + Glue + Athena metadata will remain available for querying and dashboards.
