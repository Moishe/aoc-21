from collections import defaultdict

f = open('/Users/moishe/src/aoc-21/day-10/input/input.txt')

xlat_closer = {
  '>': '<',
  ']': '[',
  '}': '{',
  ')': '('
}

score_lookup = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

counters = defaultdict(int)
score = 0
for l in f:
  l = l.rstrip()
  current_open = []
  for (idx, c) in enumerate(l):
    if c in ['(', '[', '<', '{']:
      current_open.append(c)
    else:
      last_open = current_open.pop()
      if last_open != xlat_closer[c]:
        score += score_lookup[c]
        print("corrupt closer: expected %c to be closed but found %c instead" % (last_open, c))

print(score)