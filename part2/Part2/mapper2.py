#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

zones_mapper = sys.argv[1]
zones_mapper = [eval(dp) for dp in zones_mapper.split('Z')[1].strip('_').split('_')]
zones_mapper = {1:[zones_mapper[0],zones_mapper[1],zones_mapper[2]],
                2:[zones_mapper[3],zones_mapper[4],zones_mapper[5]],
                3:[zones_mapper[6],zones_mapper[7],zones_mapper[8]],
                4:[zones_mapper[9],zones_mapper[10],zones_mapper[11]]}

def euclidean_distance(A, B):
    return sum((a-b)**2 for a, b in zip(A[:], B[:])) ** (1/2)


players = ['stephen curry', 'james harden', 'chris paul','lebron james']

for line in sys.stdin:
    line = line.strip(',').split(',')
    line_len = len(line)
    player = line[-2]
    if line_len == 23 and player in players:
        try:
            player = player.split(' ')
            player = player[0]+player[1]
            shot = 1 if line[14] == 'made' else 0
            SHOT_DIST = float(line[12].strip('"'))
            CLOSE_DEF_DIST = float(line[-5].strip('"'))
            SHOT_CLOCK = float(line[9].strip('"'))

            data = [SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK]
            data_centroids_distances = {1: euclidean_distance(data, zones_mapper[1]),
                                        2: euclidean_distance(data, zones_mapper[2]),
                                        3: euclidean_distance(data, zones_mapper[3]),
                                        4: euclidean_distance(data, zones_mapper[4])}
            data_cluster_key = min(data_centroids_distances, key = data_centroids_distances.get) #argmin
            print(player +"_"+str(data_cluster_key)+"\t"+str(shot))

        except:
            continue