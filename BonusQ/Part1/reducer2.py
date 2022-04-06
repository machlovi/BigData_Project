#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
stored_values = 1
for line in sys.stdin:
    key, value = line.strip().split('\t')
    stored_values = stored_values * eval(value)
    print(eval(value))
stored_values = round(stored_values* 100, 2)
print('Probability of black vehicle parking illegally at 34510, 10030, and 34050: '+ str(stored_values)+'%')