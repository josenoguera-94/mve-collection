from src.databricks_shim.connect import get_spark_session
from src.databricks_shim.utils import get_dbutils
from pyspark.sql.functions import col, current_timestamp

def run_etl():
    spark = get_spark_session("ETL_Sample_Job")
    dbutils = get_dbutils(spark)

    print("🚀 Starting ETL Job...")

    # 1. Generate Raw Data (Simulation)
    data = [
        (1, "Product A", 100.0, "2024-01-01"),
        (2, "Product B", 200.0, "2024-01-02"),
        (3, "Product C", 150.0, "2024-01-03")
    ]
    columns = ["id", "name", "price", "date"]
    
    df_raw = spark.createDataFrame(data, columns)
    
    # 2. Write to Bronze (Delta)
    bronze_path = "s3a://demo-bucket/bronze/products"
    print(f"💾 Writing Bronze Layer to {bronze_path}...")
    
    df_raw.write.format("delta").mode("overwrite").save(bronze_path)
    
    # 3. Read Bronze & Transform (Silver)
    print("🔄 transforming to Silver...")
    df_bronze = spark.read.format("delta").load(bronze_path)
    
    df_silver = df_bronze.withColumn("ingestion_time", current_timestamp()) \
                         .withColumn("price_with_tax", col("price") * 1.21)
    
    # 4. Write to Silver (Managed Table in Metastore)
    table_name = "products_silver"
    print(f"💾 Writing Silver Layer to Table '{table_name}'...")
    
    # Ensure database exists
    spark.sql("CREATE DATABASE IF NOT EXISTS sales")
    
    # Save as Table (Registers in Hive Metastore backed by Postgres)
    df_silver.write.format("delta") \
        .mode("overwrite") \
        .option("path", "s3a://demo-bucket/silver/products") \
        .saveAsTable(f"sales.{table_name}")
        
    print("✅ ETL Job Completed Successfully!")
    
    # 5. Verification
    print("\n📊 Verification Query:")
    spark.sql(f"SELECT * FROM sales.{table_name}").show()

    # 6. Cleanup
    spark.stop()

if __name__ == "__main__":
    run_etl()
