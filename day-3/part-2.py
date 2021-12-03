from collections import defaultdict

f = open('/Users/moishe/src/aoc-21/day-3/input/input.txt')
pos = f.tell()

bitcount = len(f.readline().rstrip())

f.seek(pos)

orig_values = [l.rstrip() for l in f]
results = [0,0]
for i in range(0,2): # greater than, then less than
  # walk through each bit from highest to lowest until we find only one remaining value
  values = orig_values.copy()
  for b in range(0, bitcount):
    # count the number on & off
    new_v = ([], [])
    for v in values:
      new_v[int(v[b])].append(v)

    if (len(new_v[1]) < len(new_v[0]) and i == 1) or (len(new_v[1]) >= len(new_v[0]) and i ==0 ):
      values = new_v[1]
    else:
      values = new_v[0]

    print(values)
    if len(values) == 1:
      break

  results[i] = int(values[0],2)

print(results[0] * results[1])