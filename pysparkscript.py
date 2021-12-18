import findspark
findspark.init()
import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext, types
import json
import requests
from pyspark.sql.functions import *
import datetime as dt
from pyspark.streaming import StreamingContext



# def getWebDate(url):
#          response = requests.get(url)
#          responseJson = json.loads(response.text)
#          return response.text, None
     
# res , resJson = getWebDate('http://localhost:8088/api/employees')

# json_object = json.dumps(res)
# with open("./dataset/out.json", "w") as outfile:
#     outfile.write(res)



# spark = SparkSession.builder.master("local").appName("JSON Data").getOrCreate()
# input_df=spark.read.json('./dataset/out.json', multiLine=True)

def main():
    sc = SparkContext(appName="PysparkStreaming")
    ssc = StreamingContext(sc, 3)   #Streaming will execute in each 3 seconds
    lines = ssc.textFileStream('./dataset/art.csv')  #'log/ mean directory name
    counts = lines.flatMap(lambda line: line.split(",")) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda a, b: a + b)
    counts.pprint()
    ssc.start()
    ssc.awaitTermination()
main()