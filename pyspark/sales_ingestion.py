from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sales_ingestion").getOrCreate()

df = spark.read.option("header", "true").csv(
    "gs://demo-bucket/raw/sales.csv"
)

df.write.mode("overwrite").format("bigquery") \
    .option("table", "project.bronze.sales") \
    .save()

spark.stop()

#made chqanges
