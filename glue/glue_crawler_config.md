# Glue Crawler Configuration

## Crawler Name
big_data_stock

## Glue Database
stock_bigdata_db

## Data Store
Amazon S3

## S3 Target Path
Example:
s3://stock-market-datalake-anuj/stock_data/

(Your exact folder path may vary)

## Output
Creates a Glue table in database stock_bigdata_db

## Crawler Run
- Run manually after data is uploaded to S3
- Output table is used in Athena
