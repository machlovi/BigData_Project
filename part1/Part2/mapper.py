#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
rule = re.compile('[^\s]{4}[A|P]')

for line in sys.stdin:
  line=line.strip(',').split(',')
  line_len = len(line)
  if line_len ==43:
    vtime = line[19]
    match = rule.search(vtime)
    if match:
      vtime=vtime[:2]+vtime[-1:]# Only printing the Violation time
      print('%s\t%s' % (vtime, '1'))
  else:
      continue
