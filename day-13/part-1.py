from collections import defaultdict

f = open('/Users/moishe/src/aoc-21/day-13/input/input.txt')

locations = defaultdict(int)
folds = []
width = 0
height = 0

def print_locations():
  global locations
  for y in range(0, height + 1):
    row = ''
    for x in range(0, width + 1):
      if (x,y) in locations:
        row += 'X'
      else:
        row += ' '
    print(row)

for l in f:
  if l.startswith('fold along'):
    (axis, coordinate) = l.rstrip().split(' ')[2].split('=')
    folds.append((axis,int(coordinate)))
  elif ',' in l:
    (x,y) = [int(x) for x in l.rstrip().split(',')]
    width = max(x, width)
    height = max(y, height)
    locations[(x,y)] += 1

for (idx, fold) in enumerate(folds):
  (axis, coordinate) = fold
  new_locations = defaultdict(int)
  for location in locations:
    (x,y) = location
    if (axis == 'y'):
      if y >= coordinate:
        y = coordinate - (y - coordinate)
    else:
      if x >= coordinate:
        x = coordinate - (x - coordinate)
    new_locations[(x,y)] += 1
  locations = new_locations
  if (axis == 'y'):
    height = coordinate - 1
  else:
    width = coordinate - 1

  if idx == 1:
    print(len(locations.keys()))

print_locations()
