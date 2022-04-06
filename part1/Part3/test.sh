#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/example.csv /Part3/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part1/Part3/mapper.py -mapper ../../part1/Part3/mapper.py \
-file ../../part1/Part3/reducer.py -reducer ../../part1/Part3/reducer.py \
-input /Part3/input/* -output /Part3/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part3/output/part-00000 | head -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part3/output/
../../stop.sh
