import json
from collections import defaultdict

positions = (4,8)
scores = (0,0)

move_map = defaultdict(int)
for d1 in range(1,4):
  for d2 in range(1,4):
    for d3 in range(1,4):
      move_map[d1 + d2 + d3] += 1

print(len(move_map.values()), sum(move_map.values()))

# will contain:
# positions
# scores
# paths to get here
results = defaultdict(lambda: defaultdict(int))

wins = [0,0]

# let's just start a simulation?
def split_universe(positions, scores, turn, instances):
  global wins
  for (result, times) in move_map.items():
    # i'm sure there's a less ugly way to do this
    if turn == 0:
      new_positions = ((positions[0] + result) % 10, positions[1])
      new_scores = (scores[0] + (new_positions[0] - 1) % 10 + 1, scores[1])
    else:
      new_positions = (positions[0], (positions[1] + result) % 10)
      new_scores = (scores[0], scores[1] + (new_positions[1] - 1) % 10 + 1)

    if (new_scores[turn] >= 21):
      wins[turn] += instances * times
    else:
      split_universe(new_positions, new_scores, (turn + 1) % 2, instances * times)

split_universe((4,8), (0,0), 0, 1)
print(wins)