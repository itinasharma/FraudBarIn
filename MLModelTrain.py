%spark.pyspark
# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline
from pyspark.sql.functions import col
from pyspark.sql.types import *

# Create SparkSession
spark = SparkSession.builder \
    .appName("FinancialAnomalyDetection") \
    .getOrCreate()

try:
    # Load the dataset
    df = spark.read.csv("/data/financial_anomaly_data.csv", header=True, inferSchema=True)

    # Display schema and first few rows of the DataFrame
    df.printSchema()
    df.show(5, truncate=False)

    # Data Cleaning and Preprocessing
    # Assuming 'Timestamp' is in string format, convert it to datetime
    df = df.withColumn("Timestamp", col("Timestamp").cast("timestamp"))

    # Filter out rows with null values in 'Amount'
    df_cleaned = df.filter(df["Amount"].isNotNull())

    # Assemble features for clustering (using 'Amount' only)
    assembler = VectorAssembler(inputCols=["Amount"], outputCol="features")

    # Define K-Means model
    kmeans = KMeans(featuresCol="features", k=3, seed=123)

    # Create pipeline
    pipeline = Pipeline(stages=[assembler, kmeans])

    # Fit the pipeline to the cleaned data
    model = pipeline.fit(df_cleaned)

    # Save the trained K-Means model with overwrite option
    model_path = "/tmp/models/kmeans_model"
    model.write().overwrite().save(model_path)

    print("K-Means model saved successfully.")

except Exception as e:
    # Handle any exception gracefully
    print("An error occurred:", str(e))

finally:
    # Stop the SparkSession
    spark.stop()
