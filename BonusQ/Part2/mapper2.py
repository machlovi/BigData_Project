#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
southest_street = 51; northest_street = 71; Manhattan_precint = 20 # 0.5 miles radius
lincoln_center_rule = re.compile('w[5-7][0-9]') # 0.5 miles radius regex rules
time_rule = '10A' # for parking at 10:00 am
parking_tickets = re.compile('[A-Za-z0-9]*stand+[A-Za-z0-9]*|[A-Za-z0-9]*park+[A-Za-z0-9]*')

zones_mapper = sys.argv[1]
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

for line in sys.stdin:
    line = line.strip(',').split(',')
    line_len = len(line)
    if line_len == 43:
        try:
            street_code_1 = line[9]; street_code_2 = line[10]; street_code_3 = line[11]
            precint = eval(line[14].strip())
            violation_time = line[19].strip()
            violation_time = violation_time[:2]+violation_time[-1]
            street_name = line[24]
            street_name = re.sub('\W+','',street_name.strip()).lower()
            street_name = ''.join(street_name.split(' '))
            street_name = eval(''.join(lincoln_center_rule.findall(street_name))[1:])
            street_code_1 = float(street_code_1.strip())
            street_code_2 = float(street_code_2.strip())
            street_code_3 = float(street_code_3.strip())

            if violation_time == time_rule and precint == Manhattan_precint and street_name >= southest_street and street_name <= northest_street:
                # Regarding condition above: removing streets not in 0.5 miles Radius using streets from W 51 up to W 71, Precint 20
                # and taking observations at 10:00 am.
                data = [street_code_1, street_code_2, street_code_3]
                data_centroids_distances = {1: euclidean_distance(data, zones_mapper[1]),
                                            2: euclidean_distance(data, zones_mapper[2]),
                                            3: euclidean_distance(data, zones_mapper[3]),
                                            4: euclidean_distance(data, zones_mapper[4]),
                                            5: euclidean_distance(data, zones_mapper[5]),
                                            6: euclidean_distance(data, zones_mapper[6]),
                                            7: euclidean_distance(data, zones_mapper[7])}
                data_cluster_key = min(data_centroids_distances, key = data_centroids_distances.get) #argmin
                violation_description = re.sub('\W+','',line[39]).lower()
                parking = parking_tickets.search(violation_description)
                parking_infraction = '1' if parking else '0'

                print('{}\t{}'.format(data_cluster_key, parking_infraction))

        except:
            continue