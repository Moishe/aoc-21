from collections import defaultdict
import json
f = open('/Users/moishe/src/aoc-21/day-6/input/input.txt')

states = {}
for i in range(0,9):
  states[(i, i + 1 if i < 8 else None)] = 0

states[(6, 0)] = 0

initial_items = [int(x) for x in f.readline().rstrip().split(",")]

for i in initial_items:
  states[(i, i + 1)] += 1

for i in range(0,256):
  new_states = defaultdict(int)
  for t,v in states.items():
    t = t[0]
    new_value = (t - 1) % 7 if t < 7 else t - 1
    prev_value = t
    if new_value == 6 and prev_value == 0:
      new_states[(8, None)] += v
    new_states[(new_value, prev_value)] += v
  states = new_states

  print(sum(states.values()))