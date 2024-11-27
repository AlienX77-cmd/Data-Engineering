from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

spark.sparkContext.getConf().getAll()