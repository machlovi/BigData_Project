#!/bin/sh
starting_zones=ClusterZ34930_11110_0_35170_13610_10910_35290_11710_10810_34810_14510_15710_34890_10810_44990_34790_4081_14510_35230_14190_11110

zones="0"
new_zones=""

for i in {0..10}; do
    if [[ $zones == $new_zones ]]; then
        break
    elif [[ $new_zones != "" ]]; then
        zones=$new_zones
    else
        zones=$starting_zones
    fi
        
    new_zones=`cat /BigData_Project/test-data\/PVI2022.csv | python3 mapper1.py "$zones" | python3 reducer1.py`
done

# echo $zones # delete this

../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/PVI2022.csv /Part2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../BonusQ/Part2/mapper2.py -mapper "../../BonusQ/Part2/mapper2.py $zones" \
-file ../../BonusQ/Part2/reducer2.py -reducer ../../BonusQ/Part2/reducer2.py \
-input /Part2/input/* -output /Part2/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../BonusQ/Part2/mapper3.py -mapper ../../BonusQ/Part2/mapper3.py \
-file ../../BonusQ/Part2/reducer3.py -reducer ../../BonusQ/Part2/reducer3.py \
-input /Part2/output/* -output /Part2-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part2-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2-2/output/
../../stop.sh