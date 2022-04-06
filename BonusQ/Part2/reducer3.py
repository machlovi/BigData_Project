#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

reducer_3_proba_output = 100
reducer_3_zone_output = ''
for entry in sys.stdin:

    zone, ticket_proba = entry.split('\t')
    ticket_proba = float(ticket_proba) # turn probability into float number

    if ticket_proba < reducer_3_proba_output:
        reducer_3_proba_output = ticket_proba # store lowest probability of getting a parking ticket
        reducer_3_zone_output = zone # store new zone
    else:
        continue

print('At 10 am, we should park at zone '+str(reducer_3_zone_output)+'\t'+str(round(reducer_3_proba_output*100,2))+'%') # Lowest probability to get a parking ticket at a 0.5 radius of Lincoln Center