from collections import defaultdict
frequencies = defaultdict(int)

f = open('/Users/moishe/src/aoc-21/day-3/input/input.txt')

total = 0
for l in f:
  l = l.rstrip();
  for b in range(0, len(l)):
    if l[b] == '1':
      frequencies[b] += 1
  total += 1

print(total)
vale = 0
valg = 0
for b in sorted(frequencies.keys()):
  vale = vale << 1
  valg = valg << 1
  if frequencies[b] < total / 2:
    vale |= 1
  else:
    valg |= 1
  print("%d: %d (%d / %d)" % (b, frequencies[b], vale, valg))

print(vale * valg)