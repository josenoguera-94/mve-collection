import os
from pyspark.sql import SparkSession

def get_spark_session(app_name="DatabricksLocal"):
    """
    Returns a SparkSession configured for the current environment.
    If APP_ENV is 'local', it configures MinIO, Delta Lake and Hive Metastore.
    """
    env = os.getenv("APP_ENV", "cloud")
    
    if env != "local":
        return SparkSession.builder.appName(app_name).getOrCreate()

    print("⚡ Initializing Local Spark Session with Databricks Emulation...")
    
    builder = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.hadoop.fs.s3a.endpoint", os.getenv("AWS_ENDPOINT_URL")) \
        .config("spark.hadoop.fs.s3a.access.key", os.getenv("AWS_ACCESS_KEY_ID")) \
        .config("spark.hadoop.fs.s3a.secret.key", os.getenv("AWS_SECRET_ACCESS_KEY")) \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.jars", "/opt/spark/jars/delta-spark_2.12-3.2.0.jar,"
                              "/opt/spark/jars/delta-storage-3.2.0.jar,"
                              "/opt/spark/jars/hadoop-aws-3.3.4.jar,"
                              "/opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar,"
                              "/opt/spark/jars/postgresql-42.6.0.jar") \
        .config("spark.sql.warehouse.dir", "s3a://demo-bucket/warehouse") \
        .config("javax.jdo.option.ConnectionURL", 
                f"jdbc:postgresql://{os.getenv('POSTGRES_HOST')}:5432/{os.getenv('POSTGRES_DB')}") \
        .config("javax.jdo.option.ConnectionDriverName", "org.postgresql.Driver") \
        .config("javax.jdo.option.ConnectionUserName", os.getenv("POSTGRES_USER")) \
        .config("javax.jdo.option.ConnectionPassword", os.getenv("POSTGRES_PASSWORD"))

    return builder.getOrCreate()
