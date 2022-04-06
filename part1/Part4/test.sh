#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part4/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part4/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part4/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/example.csv /Part4/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part1/Part4/mapper.py -mapper ../../part1/Part4/mapper.py \
-file ../../part1/Part4/reducer.py -reducer ../../part1/Part4/reducer.py \
-input /Part4/input/* -output /Part4/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part4/output/part-00000 | head -5
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part4/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part4/output/
../../stop.sh
