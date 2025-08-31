A1) S3 bucket & folders (console) 

Create bucket: credit-risk-demo-<your-initials>-dev
Folders inside the bucket:
raw/customers/, raw/loans/, raw/bureau/
curated/credit_risk/
Upload the sample CSVs (below) to their respective raw/* folders.

A2) Commit sample data & config 

data/sample/customers.csv
data/sample/loans.csv
data/sample/bureau.csv


config/env.dev.yaml

region: ap-south-1
s3_bucket: credit-risk-demo-<your-initials>-dev
raw_prefix: raw
curated_prefix: curated/credit_risk
glue_database: credit_risk_dev
curated_table: credit_risk_curated
athena_output_s3: s3://credit-risk-demo-<your-initials>-dev/athena_results/

Commit & push on feat/s3-glue-etl.

A3) Glue job (Studio Visual or Script) – 

Create IAM role for Glue with S3 read/write .
Glue Studio → Jobs → Script editor (simpler than visual for copy/paste).
Create job credit-risk-batch-etl (Glue 4.0, Python 3).
write glue/jobs/credit_risk_batch_etl.py:


Job parameters (Job → Advanced → Job parameters):

--S3_BUCKET  credit-risk-demo-<your-initials>-dev
--RAW_PREFIX raw
--CURATED_PREFIX curated/credit_risk

Run the job and confirm files land in s3://.../curated/credit_risk/.
Commit the script to glue/jobs/credit_risk_batch_etl.py and push.

A4) PR to main: Open PR feat/s3-glue-etl → main.

Title: “S3 structure + sample data + Glue ETL”