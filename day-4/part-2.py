import functools
import copy

def print_board(number, board):
  sum = 0
  for row in board:
    els = [x[0] for x in filter(lambda x: not x[1], row)]
    if els:
      sum += functools.reduce(lambda x, y: x + y, els)
    print(" ". join("%s: %s" % (str(x[0]).rjust(3, ' '), 'X' if x[1] else '0') for x in row))

  print("Solution: %d" % (sum * number))

f = open('/Users/moishe/src/aoc-21/day-4/input/input.txt')

# first line is the random numbers

numbers = [int(x) for x in f.readline().rstrip().split(',')]

boards = []
current_board = []
for l in f:
  if not len(l.rstrip()):
    if current_board:
      boards.append(current_board)
    current_board = []
    continue
  current_board.append([(int(x), False) for x in filter(None, l.rstrip().split(' '))])

boards.append(current_board)

last_winning_board = None
for number in numbers:
  print("Evaluating: %d" % number)
  for board in boards:
    for row in board:
      for i in range(0, len(row)):
        if row[i][0] == number:
          row[i] = (number, True)

  # check for winners
  for board in boards:
    # first by row
    for row in board:
      all_true = functools.reduce(lambda x, y: x and y, [x[1] for x in row])
      if all_true:
        if board in boards:
          last_winning_board = (number, copy.deepcopy(board))
          boards.remove(board)
        print("found last winning board")
        break

    # then by column
    for i in range(0, len(board[0])):
      all_true = functools.reduce(lambda x, y: x and y, [x[i][1] for x in board])
      if all_true:
        if board in boards:
          boards.remove(board)
          last_winning_board = (number, copy.deepcopy(board))
        break

print("Last Winning board:")
print_board(last_winning_board[0], last_winning_board[1])
exit(0)
