#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

#mapper_3_output = []
for entry in sys.stdin:
    player_cluster, result_shots = entry.split('\t')
    try:
        result_shots = eval(result_shots)
        if result_shots[1] == 1 and result_shots[0] == 0:
            continue
        else:
            hit_rate = result_shots[0]/result_shots[1]
    except:
        pass
    print(player_cluster+'\t'+str(hit_rate))