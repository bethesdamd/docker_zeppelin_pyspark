%pyspark
from pyspark import SparkFiles

# big_list = range(10000)
# rdd = sc.parallelize(big_list, 2)
# odds = rdd.filter(lambda x: x % 2 != 0)
# odds.take(15)


url = "https://raw.githubusercontent.com/bethesdamd/mc_interview_exercise/master/master_list"
spark.sparkContext.addFile(url)
df = spark.read.option("delimiter", "\t").csv("file://"+SparkFiles.get("master_list"), header=True, inferSchema=True)
# df.columns
# df['Title']
# df.printSchema()
countsByAuthor = df.groupBy("Author").count()
countsByAuthor.show()


