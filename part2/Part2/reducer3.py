#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

reducer_3_output = {}
for entry in sys.stdin:

    player_cluster, hit_rate = entry.split('\t')
    player, cluster = player_cluster.split('_')
    hit_rate = float(hit_rate)

    if player not in reducer_3_output:
        reducer_3_output[player] = [cluster, hit_rate]
    elif hit_rate > reducer_3_output[player][1]:
        reducer_3_output[player] = [cluster, hit_rate]
    else:
        continue

for key, value in reducer_3_output.items():
    print(key+'\t'+'Cluster: '+str(value[0])+' | Hit Rate: '+str(value[1]))