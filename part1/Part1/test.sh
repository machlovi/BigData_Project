#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/PVI2022.csv /Part1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part1/Part1/mapper.py -mapper ../../part1/Part1/mapper.py \
-file ../../part1/Part1/reducer.py -reducer ../../part1/Part1/reducer.py \
-input /Part1/input/* -output /Part1/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part1/output/part-00000 | head -1
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
../../stop.sh

