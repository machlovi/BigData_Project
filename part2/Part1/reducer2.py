#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

reducer_2_output = {}
for entry in sys.stdin:
    attacker, defender_score = entry.split('\t')
    defender, score = defender_score.split(',')
    score = float(score)
    
    if attacker not in reducer_2_output:
      reducer_2_output[attacker] = [(defender, score)]
    else:
      reducer_2_output[attacker].append((defender, score))

for player, defender_score in reducer_2_output.items():
  reducer_2_output[player] = sorted(reducer_2_output[player], key=lambda x: x[1])[0]

print(reducer_2_output)