#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

reducer_1_output = {}

for line in sys.stdin:
    key, values = line.split('\t')
    values = eval(values)
    count = values[0]
    sum_SHOT_DIST = values[1][0]
    sum_CLOSE_DEF_DIST = values[1][1]
    sum_SHOT_CLOCK = values[1][2]
    reducer_1_output[int(key)] = [sum_SHOT_DIST/count, sum_CLOSE_DEF_DIST/count, sum_SHOT_CLOCK/count]


output = ''
for key, values in reducer_1_output.items():
  for value in values:
    output = output + '_' +str(value)
output = 'ClusterZ' + output[1:]
print(output)