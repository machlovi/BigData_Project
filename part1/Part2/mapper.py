#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
rule = re.compile('[A-Z]\s[^\s]{3}')

for line in sys.stdin:
    line=line.strip(',').split(',')
    line_len = len(line)
    if line_len ==43:

      car_type= line[6]
      year= line[35]
      car_descrp=car_type+' '+year
      match = rule.search(car_descrp)
      if match:
        print('%s\t%s' % (car_descrp, '1'))
      else:
        continue