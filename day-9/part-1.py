f = open('/Users/moishe/src/aoc-21/day-9/input/input.txt')

board = []
for l in f:
  board.append([int(i) for i in l.rstrip()])

# find low points
low_points = []
for (y, row) in enumerate(board):
  for (x, val) in enumerate(row):
    all_greater = True
    for i in range(max(x - 1, 0), min(x + 2, len(row))):
      for j in range(max(y - 1, 0), min(y + 2, len(board))):
        if (i != x or j != y):
          all_greater = all_greater and board[j][i] > val
    if all_greater:
      low_points.append(val)

print(sum(low_points) + len(low_points))

