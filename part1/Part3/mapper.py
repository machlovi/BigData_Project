#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
rule = re.compile('[A-Za-z0-9|/|-]') 

for line in sys.stdin:
    line=line.strip(',')

    street= line.split(",")[25]
    match = rule.search(street)
    if  match:
      print('%s\t%s' % ( street, '1'))

    

  
    