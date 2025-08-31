import sys, json, argparse
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ["JOB_NAME", "S3_BUCKET", "RAW_PREFIX", "CURATED_PREFIX"])
bucket = args["S3_BUCKET"]
raw = args["RAW_PREFIX"].rstrip("/")
curated = args["CURATED_PREFIX"].rstrip("/")

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext); job.init(args["JOB_NAME"], args)

# Read CSVs from S3 (with headers)
customers = spark.read.option("header", "true").csv(f"s3://credit-risk-data-dev/raw/customers/")
loans     = spark.read.option("header", "true").csv(f"s3://credit-risk-data-dev/raw/loans/")
bureau    = spark.read.option("header", "true").csv(f"s3://credit-risk-data-dev/raw/bureau/")

# Basic type casting
loans = loans.withColumn("loan_amount", F.col("loan_amount").cast("double"))
bureau = bureau.withColumn("bureau_score", F.col("bureau_score").cast("int"))

# Aggregate loan exposure per customer (simple sum)
loan_agg = loans.groupBy("customer_id").agg(F.sum("loan_amount").alias("total_loan_amount"))

# Join datasets
cust_bureau = customers.join(bureau, on="customer_id", how="left")
joined = cust_bureau.join(loan_agg, on="customer_id", how="left").fillna({"total_loan_amount": 0})

# Simple risk banding by bureau_score
def risk_band(score):
    if score is None:
        return "UNKNOWN"
    if score > 700:
        return "LOW"
    if 600 <= score <= 700:
        return "MEDIUM"
    return "HIGH"

risk_udf = F.udf(risk_band)
result = joined.withColumn("risk_category", risk_udf(F.col("bureau_score")))

# Write curated parquet (optionally partition by risk)
output_path = f"s3://credit-risk-data-dev/curated/"
(result.coalesce(1)
 .write.mode("overwrite")
 .format("parquet")
 .save(output_path))

job.commit()
