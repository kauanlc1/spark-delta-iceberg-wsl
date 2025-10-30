import os
from pyspark.sql import SparkSession

MINIO_ENDPOINT = "http://127.0.0.1:9000"
MINIO_KEY = os.getenv("MINIO_KEY", "admin")
MINIO_SECRET = os.getenv("MINIO_SECRET", "admin12345")
WAREHOUSE = "s3a://datalake/warehouse"

# Dependências do Spark
DELTA_COORD = "io.delta:delta-spark_2.12:3.1.0"
ICEBERG_COORD = "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.2"
HADOOP_AWS = "org.apache.hadoop:hadoop-aws:3.3.4"
AWS_SDK = "com.amazonaws:aws-java-sdk-bundle:1.12.262"

def get_spark(app="spark-delta-iceberg"):
    builder = (
        SparkSession.builder.appName(app)
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
        )
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        # Jars necessários
        .config(
            "spark.jars.packages",
            f"{DELTA_COORD},{ICEBERG_COORD},{HADOOP_AWS},{AWS_SDK}",
        )
        # Config S3A (MinIO)
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.endpoint", MINIO_ENDPOINT)
        .config("spark.hadoop.fs.s3a.access.key", MINIO_KEY)
        .config("spark.hadoop.fs.s3a.secret.key", MINIO_SECRET)
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
        )
        # Diretório warehouse
        .config("spark.sql.warehouse.dir", WAREHOUSE)
        .config("spark.driver.memory", "4g")
        .config("spark.executor.memory", "4g")
    )
    return builder.getOrCreate()
