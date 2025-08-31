Credit Risk Analytics Pipeline (AWS)

📌 Overview

This project demonstrates an end-to-end AWS data pipeline for credit risk analytics.
Customer, loan, and bureau data are ingested into Amazon S3 (Raw Zone), transformed using AWS Glue, queried via Amazon Athena, and visualized in Amazon QuickSight.

The pipeline simulates how banks assess customer risk categories (Low / Medium / High) based on credit history and loan exposure.

🏗️ Architecture

S3 (Raw Zone) → AWS Glue (ETL) → S3 (Curated Zone) → Glue Data Catalog → Athena → QuickSight Dashboard

<img width="800" height="399" alt="credit_risk_pipeline_architecture" src="https://github.com/user-attachments/assets/45d4c196-482f-4a4f-ae0e-8a8b1f2b883a" />


⚙️ Tech Stack
--AWS S3 – Data lake (raw & curated zones)
--AWS Glue – ETL jobs + Data Catalog crawlers
--AWS Athena – SQL queries on curated data
--AWS IAM – Access and role policies
--Amazon QuickSight – BI dashboard

📂 Repository Structure

aws_credit_risk_pipeline
 ├── data/                  # Sample CSVs (customers, loans, bureau)
 ├── glue_jobs/             # Glue ETL scripts
 ├── athena/queries/        # Athena validation & reporting SQL
 ├── infra/iam_policies/    # IAM JSON policies
 ├── architecture-draft.drawio   # Editable architecture diagram
 ├── architecture-draft.png      # Exported architecture diagram
 └── README.md              # Project documentation

🚀 Steps Implemented

--Data Ingestion – Uploaded raw CSV files into S3 (/raw/).
--Glue Data Catalog – Crawlers created metadata tables for raw and curated zones.
--Glue ETL – Transformations applied to classify customers into risk categories.
--Athena Queries –
    -Count by risk bucket
    -Portfolio exposure by risk band
    -High-risk customer sample
    -QuickSight Dashboard – Visuals created for credit risk snapshot.

📊 Sample Dashboard

--Pie Chart – Risk category distribution
--Table – High-risk customers with exposure
--Bar Chart – Portfolio exposure by risk band

🔑 Key Learnings

--Setting up S3 data lake zones (raw/curated)
--Using Glue ETL & Crawlers with IAM roles
--Running Athena queries on transformed datasets
--Building a QuickSight dashboard on top of curated data

🛠️ Getting Started (Reproduce the Pipeline)
1️⃣ Setup S3 Buckets
    --Create an S3 bucket
         credit-risk-demo-<your-initials>-dev
                 Inside it, create folders:
                     /raw/ → upload sample CSVs (customers.csv, loans.csv, bureau.csv)
                    /curated/ → Glue job will output curated results
                   /athena_results/ → Athena query outputs
                   
2️⃣ IAM Role & Policy

--Create a Glue service role with:
--S3 read/write permissions
--Glue full access
   --Example minimal inline policy:
   --infra/iam_policies/glue_s3_min_policy.json
   
3️⃣ Glue Data Catalog

--Create a Glue Database: credit_risk_dev
--Add Crawler for raw data (crw-raw-credit-risk) → points to /raw/
--Run crawler → should create customers, loans, bureau tables

4️⃣ Glue ETL Job

--Use the script in glue_jobs/credit_risk_etl.py
--Input: raw tables
--Output: /curated/credit_risk/
--Run the job → produces curated dataset with risk categories

5️⃣ Glue Crawler for Curated Data

--Create Crawler crw-curated-credit-risk → points to /curated/credit_risk/
--Run crawler → creates table credit_risk_curated

6️⃣ Athena Queries

In Athena console:
  --Set result location → s3://credit-risk-demo-<your-initials>-dev/athena_results/
  --Choose database: credit_risk_dev
- --Run queries from athena/queries/
      --  Count By Risk ::
            ![count_by_risk](https://github.com/user-attachments/assets/cdcb5aa8-7899-4634-88a4-d106f517ecde)
      --  High Risk Customers :: 
           <img width="949" height="399" alt="Sample_high_risk_customers" src="https://github.com/user-attachments/assets/156a94df-3019-421c-8d7d-7290cc71951b" />
      --  Portfolio exposure by risk band ::
              ![Portfolio exposure by risk band](https://github.com/user-attachments/assets/d60054a3-e530-447d-9e10-074a3ed99db8)

7️⃣ QuickSight Dashboard

Connect to Athena → database credit_risk_dev → table credit_risk_curated
Create visuals:
   --Pie: risk category distribution
   --Table: high-risk customers
   --Bar: portfolio exposure by risk band
Save as dashboard: Credit Risk Snapshot
