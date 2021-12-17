from os import DirEntry
import re
f = open('/Users/moishe/src/aoc-21/day-17/input/input.txt')

s = f.readline().rstrip()

matches = re.match("target area: x=(\\d+)..(\\d+), y=(-\\d+)..(-\\d+)", s)

(x1, x2, y1, y2) = [int(i) for i in matches.groups()]

x = 0
y = 0

dx = 0
dy = 0

highest = 0

def step():
  global x, y, dx, dy, x1, y1, x2, y2, highest

  x += dx
  y += dy

  dy -= 1
  if dx > 0:
    dx -= 1
  elif dx < 0:
    dx += 1

  highest = max(highest, y)

  hit = x >= x1 and x <= x2 and y >= y1 and y <= y2
  should_continue = not (x > x2 or (y < y1 and dy <= 0))

  return (should_continue, hit)

highest_success = 0
successes = []
for candidate_dx in range(-10, 1000):
  for candidate_dy in range(-300, 1000):
    x = 0
    y = 0
    dx = candidate_dx
    dy = candidate_dy
    highest = 0
    should_continue = True
    steps = 0
    while should_continue:
      steps += 1
      (should_continue, hit) = step()
      if hit:
        print("Success: %d, %d" % (candidate_dx, candidate_dy))
        successes.append((candidate_dx, candidate_dy, steps))
        if highest > highest_success:
          print("Success with %d %d" % (candidate_dx, candidate_dy))
          highest_success = highest
          print("New highest success %d" % highest_success)
        break

print("Highest success: %d" % highest_success)
print("Total successes %d" % len(successes))

f = open('results.csv', 'w')
for success in successes:
  f.write(','.join([str(x) for x in list(success)]))
  f.write('\n')
