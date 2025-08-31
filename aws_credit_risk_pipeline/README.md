# AWS Credit Risk Pipeline 

## Architecture
S3 (raw) → Glue ETL (PySpark) → S3 (curated parquet) → Glue Catalog → Athena → QuickSight

## Quick start
1) Create S3 bucket and upload sample CSVs (see `data/sample`).
2) Run Glue job `credit-risk-batch-etl` with params in `config/env.dev.yaml`.
3) Run Glue crawlers for raw and curated.
4) Query Athena using `athena/queries/*.sql`.
5) Build QuickSight visuals (see `quicksight/README.md`).

## Repo layout
- `data/sample`: CSVs to upload to S3 raw paths
- `glue/jobs`: PySpark ETL script
- `athena/queries`: validation & reporting SQL
- `config`: environment config
- `infra/iam_policies`: example minimal policy
- `docs`: diagram + notes





## S3 bucket & folders (console) 

- Create bucket: 
- Folders inside the bucket:
- raw/customers/, raw/loans/, raw/bureau/
- curated/credit_risk/
- Upload the sample CSVs (below) to their respective raw/* folders.

## Commit sample data & config 

- data/sample/customers.csv
- data/sample/loans.csv
- data/sample/bureau.csv


- config/env.dev.yaml

- region: ap-south-1
- s3_bucket: s3:// 
- raw_prefix: raw
- curated_prefix: curated/credit_risk
- glue_database: credit_risk_dev
- curated_table: credit_risk_curated
- athena_output_s3: s3://

## Commit & push on feat/s3-glue-etl.

## Glue job (Studio Visual or Script) 

- Create IAM role for Glue with S3 read/write .
- Glue Studio → Jobs → Script editor (simpler than visual for copy/paste).
- Create job credit-risk-batch-etl (Glue 4.0, Python 3).
- write glue/jobs/credit_risk_batch_etl.py:


## Job parameters (Job → Advanced → Job parameters):

--S3_BUCKET  credit-risk-demo-<your-initials>-dev
--RAW_PREFIX raw
--CURATED_PREFIX curated/credit_risk

- Run the job and confirm files land in s3://.../curated/credit_risk/.
- Commit the script to glue/jobs/credit_risk_batch_etl.py and push.

## PR to main: Open PR 

