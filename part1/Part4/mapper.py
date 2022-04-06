#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
rule = re.compile('[A-Za-z]')

for line in sys.stdin:
    line=line.strip(',')

    color= line.split(",")[34]
    match = rule.search(color)
    if  match:
      print('%s\t%s' % ( color, '1'))

    

  
    