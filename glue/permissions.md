# IAM Permissions Used for Glue

## Glue Crawler Role
Example role name:
AWSGlueServiceRole-stock-crawler-role

## Permissions Required
- AmazonS3ReadOnlyAccess (or custom S3 read policy)
- AWSGlueServiceRole
- CloudWatchLogsFullAccess (optional for debugging)

## S3 Bucket Policy Note
Bucket should allow Glue to read objects.
