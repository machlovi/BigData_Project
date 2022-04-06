#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

reducer_1_output = {}

for line in sys.stdin:
    key, values = line.split('\t')
    values = eval(values)
    count = values[0]
    sum_street_code_1 = values[1][0]
    sum_street_code_2 = values[1][1]
    sum_street_code_3 = values[1][2]
    reducer_1_output[int(key)] = [sum_street_code_1/count, sum_street_code_2/count, sum_street_code_3/count]

output = ''
for key, values in reducer_1_output.items():
  for value in values:
    output = output + '_' +str(value)
output = 'ClusterZ' + output[1:]
print(output)