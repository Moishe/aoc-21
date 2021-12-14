import json
from collections import defaultdict

debug = False

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
for i in range(0, 40):
  if debug:
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
  for (pair, count) in pairs.items():
    new_pairs[pair[0] + xlat[pair]] += count
    new_pairs[xlat[pair] + pair[1]] += count
    new_pairs[pair] -= count
    if (new_pairs[pair] == 0):
      del(new_pairs[pair])
  pairs = new_pairs

  # check
  if debug:
    expected_pairs = defaultdict(int)
    for i in range(0, len(state) - 1):
      expected_pairs[state[i:i+2]] += 1

    for pair in expected_pairs:
      if expected_pairs[pair] != pairs[pair]:
        print("Mismatch %s %d %d" % (pair, expected_pairs[pair], pair[pair]))
        exit(1)

if debug:
  freqs = defaultdict(int)
  for c in state:
    freqs[c] += 1

  freqs = sorted(freqs.items(), key=lambda item: item[1])
  print(freqs[-1][1] - freqs[0][1])

new_freqs = defaultdict(int)
for (pair, count) in pairs.items():
  new_freqs[pair[0]] += count

new_freqs[start[-1]] += 1

new_freqs = sorted(new_freqs.items(), key=lambda item: item[1])

print(new_freqs[-1][1] - new_freqs[0][1])
