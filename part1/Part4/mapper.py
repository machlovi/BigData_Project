#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
rule = re.compile('[A-Za-z]')

for line in sys.stdin:
  line=line.strip(',').split(',')
  line_len = len(line)
  if line_len == 43:
    color= line[33]
    match = rule.search(color)
    if  match:
      print('%s\t%s' % ( color, '1'))
  else:
      continue 

    

  
    