#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
zones_mapper = sys.argv[1]
southest_street = 51; northest_street = 71; Manhattan_precint = 20 # 0.5 miles radius
lincoln_center_rule = re.compile('w[5-7][0-9]') # 0.5 miles radius regex rules

zones_mapper = [eval(dp) for dp in zones_mapper.split('Z')[1].strip('_').split('_')]
zones_mapper = {1:[zones_mapper[0],zones_mapper[1],zones_mapper[2]],
                2:[zones_mapper[3],zones_mapper[4],zones_mapper[5]],
                3:[zones_mapper[6],zones_mapper[7],zones_mapper[8]],
                4:[zones_mapper[9],zones_mapper[10],zones_mapper[11]],
                5:[zones_mapper[12],zones_mapper[13],zones_mapper[14]],
                6:[zones_mapper[15],zones_mapper[16],zones_mapper[17]],
                7:[zones_mapper[18],zones_mapper[19],zones_mapper[20]]}

def euclidean_distance(A, B):
  return sum((a-b)**2 for a, b in zip(A[:], B[:])) ** (1/2)

mapper_1_output = {1:[0,[0,0,0]],
                  2:[0,[0,0,0]],
                  3:[0,[0,0,0]],
                  4:[0,[0,0,0]],
                  5:[0,[0,0,0]],
                  6:[0,[0,0,0]],
                  7:[0,[0,0,0]],}

for line in sys.stdin:
  line = line.strip(',').split(',')
  line_len = len(line)
  if line_len == 43:
    try:
      street_code_1 = line[9]; street_code_2 = line[10]; street_code_3 = line[11]
      precint = eval(line[14].strip())
      street_name = line[24]
      street_name = re.sub('\W+','',street_name.strip()).lower()
      street_name = ''.join(street_name.split(' '))
      street_name = eval(''.join(lincoln_center_rule.findall(street_name))[1:])
      street_code_1 = float(street_code_1.strip())
      street_code_2 = float(street_code_2.strip())
      street_code_3 = float(street_code_3.strip())
      if precint == Manhattan_precint and street_name >= southest_street and street_name <= northest_street: # removing streets not in 0.5 miles Radius
        data = [street_code_1, street_code_2, street_code_3]
        data_centroids_distances = {1: euclidean_distance(data, zones_mapper[1]),
                                    2: euclidean_distance(data, zones_mapper[2]),
                                    3: euclidean_distance(data, zones_mapper[3]),
                                    4: euclidean_distance(data, zones_mapper[4]),
                                    5: euclidean_distance(data, zones_mapper[5]),
                                    6: euclidean_distance(data, zones_mapper[6]),
                                    7: euclidean_distance(data, zones_mapper[7])}
        data_cluster_key = min(data_centroids_distances, key = data_centroids_distances.get) #argmin
        mapper_1_output[data_cluster_key][0] += 1 # counter
        mapper_1_output[data_cluster_key][1][0] += data[0] #sum all street_code_1
        mapper_1_output[data_cluster_key][1][1] += data[1] #sum all street_code_2
        mapper_1_output[data_cluster_key][1][2] += data[2] #sum all street_code_3
    except:
      continue

combiner_1_input = mapper_1_output
for key, values in combiner_1_input.items():
  print('{key}\t{values}'.format(key=key, values=values))