import sys
import re
black_color = re.compile('[a-zA-Z]*[B|b][a-zA-Z]*[c|k]')
street_codes = ['34510', '10030', '34050']

parking_tickets = re.compile('[A-Za-z0-9]*stand+[A-Za-z0-9]*|[A-Za-z0-9]*park+[A-Za-z0-9]*')

for line in sys.stdin:
    line = line.strip(',').split(',')
    line_len = len(line)
    color = line[33].strip().strip('.'); color = ''.join(color.split(' ')).lower()
    color_val = black_color.search(color)
    street_code_1 = line[9]; street_code_2 = line[10]; street_code_3 = line[11]
    if color_val and line_len == 43 and (street_code_1 in street_codes or street_code_2 in street_codes or street_code_3 in street_codes):
        violation_description = re.sub('\W+','',line[39]).lower()
        parking = parking_tickets.search(violation_description)
        parking_infraction = 1 if parking else 0
        if street_code_1 in street_codes:
            street_code = street_code_1
        elif street_code_2 in street_codes:
            street_code = street_code_2
        else:
            street_code = street_code_3
        print('{}\t{}'.format(street_code, parking_infraction))
    else:
        continue
