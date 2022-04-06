#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
for line in sys.stdin:
  players_pairs, result_shots = line.split('\t')
  attacker, defender = players_pairs.strip().split(',')
  attacker = attacker.strip(); defender = defender.strip()
  try:
    result_shots = eval(result_shots)
    if result_shots[1] == 1 and result_shots[0] == 0:
      continue
    else:
      result_shots = result_shots[0]/result_shots[1]
  except:
    pass
  print(attacker+'\t'+defender+','+str(result_shots))