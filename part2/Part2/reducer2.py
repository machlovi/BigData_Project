#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

dict_score_count = {}
for line in sys.stdin:
    record = line.split('\t')
    data,count = record[0], record[1]
    try:
        count = int(count)
        dict_score_count[data] = [dict_score_count.get(data, [0,0])[0] + count, dict_score_count.get(data, [0,0])[1]+1]
    except ValueError:
        pass
for key, value in dict_score_count.items():
    print(key+'\t'+str(value))