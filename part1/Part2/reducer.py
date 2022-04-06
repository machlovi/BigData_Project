#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
from operator import itemgetter
dic_car_count = {}
for line in sys.stdin:
    car_descp, count = line.split('\t',1)
    try:
        count = int(count)
        dic_car_count [car_descp] = dic_car_count .get(car_descp, 0) + count
          
    except ValueError:
        pass
        
sorted_dict_vtime_count = sorted(dic_car_count .items(), key=itemgetter(1))[::-1]

for car_descp, count in sorted_dict_vtime_count:
    print ('%s\t%s' % (car_descp, count))
