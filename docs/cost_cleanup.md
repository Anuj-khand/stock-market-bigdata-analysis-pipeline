# 💰 Cost Cleanup Guide (AWS)

## ✅ 1) Stop EC2 Instance (Kafka Broker)
*Recommended action:* Stop (not terminate)

Steps:
1. AWS Console → EC2 → Instances
2. Select your instance
3. Instance state → *Stop*

📌 Why: EC2 running continuously will incur hourly cost.

---

## ✅ 2) Delete EBS Volume (Optional)
If you are done permanently and don’t need EC2 disk:

Steps:
1. EC2 → Volumes
2. Select attached volume
3. Delete

📌 Note: EBS volumes can still cost money even after stopping EC2.

---

## ✅ 3) Delete S3 Data (Optional)
If you don’t need the stored stock data:

Steps:
1. S3 → Your bucket (example: stock-market-datalake-anuj)
2. Empty bucket (delete all objects)
3. Delete bucket

📌 Note: S3 storage cost is small, but it still accumulates over time.

---

## ✅ 4) Delete Athena Query Results (Recommended)
Athena stores query results in an S3 bucket.

Steps:
1. Go to Athena → Settings
2. Find query result bucket location
3. Open that S3 bucket
4. Delete old query results files

📌 Why: Query result files can slowly increase S3 usage.

---

## ✅ 5) Delete Glue Crawler (Optional)
Steps:
1. AWS Glue → Crawlers
2. Select crawler → Delete

📌 Note: Glue crawler itself doesn't cost unless it runs, but deleting keeps environment clean.

---

## ✅ 6) Delete Glue Tables / Database (Optional)
Steps:
1. AWS Glue → Data Catalog → Databases
2. Open database → delete tables
3. Delete database

📌 Why: Keeps Glue catalog clean (no direct cost, but good housekeeping).

---

## ✅ 7) QuickSight Subscription (IMPORTANT)
QuickSight can incur monthly charges depending on edition.

If you don’t need QuickSight after demo:
1. QuickSight → Manage QuickSight
2. Account settings / Subscription
3. Cancel subscription (if applicable)

📌 Note: If you keep QuickSight enabled, it may incur recurring cost.

---

## ✅ 8) IAM Roles and Policies (Optional)
Steps:
1. IAM → Roles
2. Remove unused roles created for Glue/EC2 access (optional)

📌 Note: IAM has no cost, but keep it clean.

---

## ✅ Final Recommended Cleanup (Minimum)
To reduce cost but keep project ready:
✅ Stop EC2  
✅ Keep S3 data + Glue tables + Athena  
(Optional: clean Athena query results bucket)
