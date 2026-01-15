1) Kafka Producer not sending messages:
Check Kafka is running on EC2. Run code jps

Expected outcome:
Kafka,
QuorumPeerMain (or Zookeeper)

Check topic exists

Run code

Bash

bin/kafka-topics.sh --list --bootstrap-server localhost:9092
2) Kafka Consumer not receiving messages

✅ Ensure consumer uses correct broker:
EC2_PUBLIC_IP:9092

❌ Don’t use localhost:9092 from your laptop.
Also confirm topic name is same in producer and consumer (example: stock-topic).

3) Kafka connection error: NoBrokersAvailable

Fix EC2 Security Group Allow inbound:
9092 (Kafka) from your IP
22 (SSH) from your IP
Fix Kafka advertised listeners (on EC2) 

Edit:
config/server.properties
Update:
Properties

advertised.listeners=PLAINTEXT://<EC2_PUBLIC_IP>:9092

listeners=PLAINTEXT://0.0.0.0:9092

Restart Kafka after changes.
5) Glue crawler table not created

Common causes

Wrong S3 path selected in crawler

No readable files at crawl location

Fix Crawler should point to root path: s3://<bucket-name>/stock_data/

Also upload a sample file at root: s3://<bucket-name>/stock_data/sample.json

Then rerun crawler.
6) Glue crawler error: AccessDenied (403)

Cause: Glue crawler IAM role does not have S3 read permissions.

Fix Attach to Glue crawler role:

AWSGlueServiceRole

AmazonS3ReadOnlyAccess

Also ensure bucket policy doesn’t block Glue.

7) Athena error: HIVE_INVALID_METADATA (duplicate columns)

Cause: Partition columns like year/month/day are duplicated as normal columns.

Fix Ignore/delete wrong table created by crawler (example: year_2026) and query the correct JSON table:

Sql
SELECT *
FROM stock_bigdata_db."1768239694912_json"
LIMIT 10;

9) QuickSight chart is faint

Cause: Aggregation becomes too large (Sum(close) / Sum(volume)).

Fix Change aggregation:

Sum(close) → Avg(close)

Sum(volume) → Avg(volume) (for trend charts)

Also:
Increase line width
Enable markers

11) QuickSight “Access Denied” for Athena/S3

Fix QuickSight → Manage QuickSight → Security & permissions Enable:
Amazon Athena,
Amazon S3

Select required S3 buckets

13) EC2 auto logout / session disconnect

Use tmux so Kafka/consumer keeps running even if SSH disconnects.
Run code

Bash

tmux new -s kafka
Detach:

Run code

Bash

Ctrl + B then D

Reattach:

Run code

Bash
tmux attach -t kafka

15) Cost Control Reminder 💰

To avoid AWS charges:

Stop EC2 when not streaming

Keep S3 + Glue + Athena metadata for analysis and QuickSight

Clean Athena query results bucket if needed
