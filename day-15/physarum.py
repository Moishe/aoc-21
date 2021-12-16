import os
import random
import sys

f = open('/Users/moishe/src/aoc-21/day-15/input/debug.txt')

highlight = '\033[1m'
endc = '\033[0m'

width = 0
height = 0
board = []
queue = []
neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def idx_to_x_y(idx):
  global width
  return (idx % width, int(idx / width))

def x_y_to_idx(xy): #xy is a tuple
  global width
  return xy[1] * width + xy[0]

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
     sys.stdout.flush()

def print_board_with_highlight(board, path):
  for y in range(0, height):
    for x in range(0, width):
      if board[x_y_to_idx((x,y))] < 0:
        val = '.'
      else:
        val = ' '

      #val = str(board[x_y_to_idx((x,y))])
      #if (x,y) in path:
      #  val = highlight + val + endc
      print_there(x, y, val)

for l in f:
  width = len(l.rstrip())
  height += 1
  board.extend([int(c) for c in l.rstrip()])

part2 = True
debug_print = False
if part2:
  if debug_print:
    for y in range(0, height):
      row = ''
      for x in range(0, width):
        row += str(board[x_y_to_idx((x,y))])
      print(row)

  new_board = [0] * len(board) * 25

  for x in range(0, 5):
    for y in range(0, 5):
      for (idx, cost) in enumerate(board):
        (bx,by) = idx_to_x_y(idx)
        newx = bx + x * width
        newy = by + y * height
        newidx = newx + newy * width * 5

        new_cost = (cost + x + y)
        new_cost = new_cost if new_cost <= 9 else new_cost % 10 + 1
        new_board[newidx] = new_cost

  width = width * 5
  height = height * 5
  board = new_board

board_pheromone = [0] * len(board)
actors = []
for i in range(0, len(board)):
  actor = (
    int(random.random() * 4),
    idx_to_x_y(i), # location
  )
  actors.append(actor)

directions = [
  (-1,  0),
  ( 0,  1),
  ( 1,  0),
  ( 0, -1)
]

os.system('clear')

for iteration in range(0,1000):
  for (idx, actor) in enumerate(actors):
    (dir, (x, y)) = actor

    min_value = 10 # highest value on the board + 1
    for i in range(0, 3):
      look_dir = (dir + i - 1) % 4
      look_x = x + directions[look_dir][0]
      look_y = y + directions[look_dir][1]

      if look_x >= 0 and look_y >= 0 and look_x < width and look_y < height:
        # seek lowest board value
        board_idx = x_y_to_idx((look_x, look_y))
        board_value = board[board_idx] * 100
        pheromone_value = board_pheromone[board_idx]

        look_value = board_value - pheromone_value

        if look_value < min_value:
          min_value = look_value
          dir = look_dir

    board_pheromone[x_y_to_idx((x,y))] -= 1
    x = x + directions[dir][0]
    y = y + directions[dir][1]

    if x < 0 or x >= width or y < 0 or y >= height:
      x = min(width - 1, max(0, x))
      y = min(height - 1, max(0, y))

      dir = (dir + 2) % 4

    actors[idx] = (dir, (x,y))

  board_pheromone = [x + 1 for x in board_pheromone]

  print_board_with_highlight(board_pheromone, [])
