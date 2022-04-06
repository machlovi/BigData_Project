#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
from operator import itemgetter
dic_street_count = {}
for line in sys.stdin:
    street, count = line.split('\t',1)
    try:
        count = int(count)
        dic_street_count [street] = dic_street_count .get(street, 0) + count
          
    except ValueError:
        pass
        
sorted_dict_vtime_count = sorted(dic_street_count .items(), key=itemgetter(1))[::-1]

for street, count in sorted_dict_vtime_count:
    print ('%s\t%s' % (street, count))
