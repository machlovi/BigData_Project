#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

for line in sys.stdin:
    street_codes, street_violation_info = line.strip().split('\t')
    try:
        street_violation_info = eval(street_violation_info)
        street_violation_info = float(street_violation_info[0])/float(street_violation_info[1])
        print(street_codes+'\t'+str(street_violation_info))
    except:
        continue



