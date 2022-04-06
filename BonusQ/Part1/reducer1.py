import sys
dict_parking_violations = {}

for line in sys.stdin:
    line = line.strip().split('\t')
    key, value = line[0], line[1]
    try:
        value = int(value)
        dict_parking_violations[key] = [dict_parking_violations.get(key, [0,0])[0] + value, dict_parking_violations.get(key, [0,0])[1]+1]
    except ValueError:
        pass
for key, value in dict_parking_violations.items():
    print(key+'\t'+str(value))