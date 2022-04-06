#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/example.csv /Part2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part1/Part2/mapper.py -mapper ../../part1/Part2/mapper.py \
-file ../../part1/Part2/reducer.py -reducer ../../part1/Part2/reducer.py \
-input /Part2/input/* -output /Part2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part2/output/part-00000 | head -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
../../stop.sh
