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

mapper_1_output = {1:[0,[0,0,0]],
                  2:[0,[0,0,0]],
                  3:[0,[0,0,0]],
                  4:[0,[0,0,0]]}

for line in sys.stdin:
  line = line.strip(',').split(',')
  line_len = len(line)
  if line_len == 23:
    try:
      SHOT_DIST = float(line[12].strip('"'))
      CLOSE_DEF_DIST= float(line[-5].strip('"'))
      SHOT_CLOCK = float(line[9].strip('"'))
      if SHOT_DIST < 29 and CLOSE_DEF_DIST < 11 and SHOT_CLOCK < 26: # removing outliers
        data = [SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK]
        data_centroids_distances = {1: euclidean_distance(data, zones_mapper[1]),
                                    2: euclidean_distance(data, zones_mapper[2]),
                                    3: euclidean_distance(data, zones_mapper[3]),
                                    4: euclidean_distance(data, zones_mapper[4])}
        data_cluster_key = min(data_centroids_distances, key = data_centroids_distances.get) #argmin
        #data_cluster_distance = data_centroids_distances[data_cluster_key]
        mapper_1_output[data_cluster_key][0] += 1 # counter
        mapper_1_output[data_cluster_key][1][0] += data[0] #sum all SHOT_DIST
        mapper_1_output[data_cluster_key][1][1] += data[1] #sum all CLOSE_DEF_DIST
        mapper_1_output[data_cluster_key][1][2] += data[2] #sum all SHOT_CLOCK
        #mapper_1_output[data_cluster_key].append(data)
        #data.append({data_cluster_key:data_cluster_distance})                       
        #mapper1_output.append(data)
    except:
      continue

combiner_1_input = mapper_1_output
#combiner_1_output = []
for key, values in combiner_1_input.items():
  print('{key}\t{values}'.format(key=key, values=values))