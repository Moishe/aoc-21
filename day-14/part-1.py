from collections import defaultdict
from collections import OrderedDict
f = open('/Users/moishe/src/aoc-21/day-14/input/input.txt')

start = f.readline().rstrip()
f.readline()

xlat = {}
for e in f:
  (pair, insertion) = e.rstrip().split(' -> ')
  xlat[pair] = insertion

state = start
for i in range(0, 40):
  new_state = ''
  for j in range(0, len(state) - 1):
    pair = state[j:j+2]
    if pair in xlat:
      new_state += pair[0] + xlat[pair]
    else:
      new_state += pair[0]
  state = new_state + state[-1]
  print(len(state))

freqs = defaultdict(int)
for c in state:
  freqs[c] += 1

freqs = sorted(freqs.items(), key=lambda item: item[1])

print(freqs[-1][1] - freqs[0][1])
