import json
from collections import defaultdict

f = open('/Users/moishe/src/aoc-21/day-14/input/input.txt')

start = f.readline().rstrip()
f.readline()

xlat = {}
for e in f:
  (pair, insertion) = e.rstrip().split(' -> ')
  xlat[pair] = insertion

pairs = defaultdict(int)
for i in range(0, len(start) - 1):
  pairs[start[i:i+2]] += 1

state = start
for i in range(0, 3):
  new_state = ''
  # method 1
  for j in range(0, len(state) - 1):
    pair = state[j:j+2]
    if pair in xlat:
      new_state += pair[0] + xlat[pair]
    else:
      new_state += pair[0]
  state = new_state + state[-1]
  
  # method 2
  new_pairs = pairs.copy()
  for pair in pairs:
    new_pairs[pair[0] + xlat[pair]] += 1
    new_pairs[xlat[pair] + pair[1]] += 1
    new_pairs[pair] -= 1
  pairs = new_pairs

  # check
  expected_pairs = defaultdict(int)
  for i in range(0, len(start) - 1):
    expected_pairs[start[i:i+2]] += 1

  print(json.dumps(pairs, indent=2))
  print(json.dumps(expected_pairs, indent=2))


freqs = defaultdict(int)
for c in state:
  freqs[c] += 1

freqs = sorted(freqs.items(), key=lambda item: item[1])

print(freqs[-1][1] - freqs[0][1])
