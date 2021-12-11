from collections import defaultdict
f = open('/Users/moishe/src/aoc-21/day-11/input/input.txt')

width = 0
height = 0
board = []
flashes = []

def idx_to_x_y(idx):
  global width
  return (idx % width, int(idx / width))

def x_y_to_idx(xy): #xy is a tuple
  global width
  return xy[1] * width + xy[0]

def print_board(board):
  for row in range(0, height):
    start = row * width
    end = start + width
    print(' '.join([str(i).zfill(2) for i in board[start:end]]))

for l in f:
  width = len(l.rstrip())
  height += 1
  board.extend([int(c) for c in l.rstrip()])

print(width, height)
total_flashes = 0
gen = 0
for gen in range(0, 19600):
  # first increase the energy levels
  board = [x + 1 for x in board]

  # now calculate the flashes
  flashes = defaultdict(bool)
  were_flashes = True
  while were_flashes:
    were_flashes = False
    for (i, val) in enumerate(board):
      if val > 9 and i not in flashes:
        flashes[i] = True
        were_flashes = True
        # increment around val
        (x, y) = idx_to_x_y(i)
        for x1 in range(max(0, x - 1), min(width, x + 2)):
          for y1 in range(max(0, y - 1), min(width, y + 2)):
            board[x_y_to_idx((x1,y1))] += 1

  # now reset everything greater than 9 to 0
  board = [x if x <= 9 else 0 for x in board]
  num_flashes = board.count(0)
  total_flashes += num_flashes
  if num_flashes == len(board):
    print("Found it! %d" % (gen + 1))
    print_board(board)
    exit(0)
  #print(gen, total_flashes)
