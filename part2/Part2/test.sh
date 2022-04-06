#!/bin/sh

# starting_zones={1:[[$(( $RANDOM % 29 + 0 )),$(( $RANDOM % 11 + 0 )),$(( $RANDOM % 26 + 0 ))]],2:[$(( $RANDOM % 29 + 0 )),$(( $RANDOM % 11 + 0 )),$(( $RANDOM % 26 + 0 ))],3:[$(( $RANDOM % 29 + 0 )),$(( $RANDOM % 11 + 0 )),$(( $RANDOM % 26 + 0 ))],4:[$(( $RANDOM % 29 + 0 )),$(( $RANDOM % 11 + 0 )),$(( $RANDOM % 26 + 0 ))]}
# Y=\'$(echo "$starting_zones" | sed "s/\[//; s/]//; s/'//g")\'
starting_zones=ClusterZ6_3_26_15_8_1_2_5_10_26_4_5
# $Y

zones="0"
new_zones=""

# ../../start.sh

for i in {0..5}; do
    if [[ $zones == $new_zones ]]; then
        break
    elif [[ $new_zones != "" ]]; then
        zones=$new_zones
    else
        zones=$starting_zones
    fi

    new_zones=`cat /BigData_Project/test-data\/shot_logs.csv | python3 /BigData_Project/part2/Part2/mapper1.py "$zones" | python3 /BigData_Project/part2/Part2/reducer1.py`
done

../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/shot_logs.csv /Part2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part2/Part2/mapper2.py -mapper "../../part2/Part2/mapper2.py $zones" \
-file ../../part2/Part2/reducer2.py -reducer ../../part2/Part2/reducer2.py \
-input /Part2/input/* -output /Part2/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../part2/Part2/mapper3.py -mapper ../../part2/Part2/mapper3.py \
-file ../../part2/Part2/reducer3.py -reducer ../../part2/Part2/reducer3.py \
-input /Part2/output/* -output /Part2-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part2-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2-2/output/
../../stop.sh