from collections import defaultdict

f = open('/Users/moishe/src/aoc-21/day-10/input/input.txt')

xlat_closer = {
  '>': '<',
  ']': '[',
  '}': '{',
  ')': '('
}

xlat_opener = {v: k for (k,v) in xlat_closer.items()}

score_table = {
  ')': 1,
  ']': 2, 
  '}': 3,
  '>': 4
}

counters = defaultdict(int)
scores = []
for l in f:
  l = l.rstrip()
  current_open = []
  corrupt = False
  for (idx, c) in enumerate(l):
    if c in ['(', '[', '<', '{']:
      current_open.append(c)
    else:
      last_open = current_open.pop()
      if last_open != xlat_closer[c]:
        corrupt = True

  if current_open and not corrupt:
    expected = list(reversed([xlat_opener[c] for c in current_open]))
    score = 0
    for c in expected:
      score *= 5
      score += score_table[c]
    scores.append(score)

scores.sort()
midpoint = int(len(scores) / 2)
print(scores[midpoint])
