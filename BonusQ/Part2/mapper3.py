#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
for entry in sys.stdin:
    zone, parking_ticket_proba = entry.split('\t')
    try:
        parking_ticket_proba = eval(parking_ticket_proba)
        if parking_ticket_proba[1] == 1 and parking_ticket_proba[0] == 0:
            continue
        else:
            parking_ticket_proba = parking_ticket_proba[0]/parking_ticket_proba[1]
    except:
        pass
    print(zone+'\t'+str(parking_ticket_proba))