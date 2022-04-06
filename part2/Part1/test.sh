#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/shot_logs.csv /Part1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part2/Part1/mapper1.py -mapper ../../part2/Part1/mapper1.py \
-file ../../part2/Part1/reducer1.py -reducer ../../part2/Part1/reducer1.py \
-input /Part1/input/* -output /Part1/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part2/Part1/mapper2.py -mapper ../../part2/Part1/mapper2.py \
-file ../../part2/Part1/reducer2.py -reducer ../../part2/Part1/reducer2.py \
-input /Part1/output/* -output /Part1-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part1-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1-2/output/
../../stop.sh