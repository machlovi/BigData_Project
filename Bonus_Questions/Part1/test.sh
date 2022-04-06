#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/PVI2022.csv /Part1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../BonusQ/Part1/mapper1.py -mapper ../../BonusQ/Part1/mapper1.py \
-file ../../BonusQ/Part1/reducer1.py -reducer ../../BonusQ/Part1/reducer1.py \
-input /Part1/input/* -output /Part1/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../BonusQ/Part1/mapper2.py -mapper ../../BonusQ/Part1/mapper2.py \
-file ../../BonusQ/Part1/reducer2.py -reducer ../../BonusQ/Part1/reducer2.py \
-input /Part1/output/* -output /Part1-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part1-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1-2/output/
../../stop.sh