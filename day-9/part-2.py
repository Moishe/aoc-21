from collections import defaultdict
from functools import reduce

f = open('/Users/moishe/src/aoc-21/day-9/input/input.txt')

board = []
board_states = []
max_height = 0
for l in f:
  row = [int(i) for i in l.rstrip()]
  board.append(row)
  max_height = max(max_height, max(row))
  board_states.append([0 for i in l.rstrip()])

def grow_basin(x, y, id):
  global board, board_states
  board_states[y][x] = id
  for (i,j) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
    i = x + i
    j = y + j
    if (i < 0 or j < 0 or j >= len(board) or i >= len(board[0])):
      continue
    if board[j][i] == 9:
      continue
    if board_states[j][i] == 0:
      grow_basin(i, j, id)

max_id = 0
for h in range(0, max_height):
  for (y, row) in enumerate(board):
    for (x, val) in enumerate(row):
      if board[y][x] == 9:
        continue
      if board_states[y][x] == 0:
        max_id += 1
        grow_basin(x, y, max_id)

sizes = defaultdict(int)
for row in board_states:
  for val in row:
    if val:
      sizes[val] += 1

largest = sorted(sizes.values())

print(reduce(lambda x, y: x * y, largest[-3:]))
