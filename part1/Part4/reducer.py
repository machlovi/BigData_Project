#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
from operator import itemgetter
dic_color_count = {}
total_count=0
for line in sys.stdin:
    color, count = line.split('\t',1)
    try:
        count = int(count)
        dic_color_count [color] = dic_color_count .get(color, 0) + count
        total_count+=count
          
    except ValueError:
        pass
        
sorted_dict_color_count = sorted(dic_color_count .items(), key=itemgetter(1))[::-1]

for color, count in sorted_dict_color_count:
    print ('%s\t%s' % (color, count))
