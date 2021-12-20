f = open('/Users/moishe/src/aoc-21/day-20/input/input.txt')

generation = 0

def read_board():
  decode = [0 if c == '.' else 1 for c in f.readline().rstrip()]
  f.readline()

  board = []
  height = 0
  for l in f:
    width = len(l.rstrip())
    height += 1
    board.extend([0 if c == '.' else 1 for c in l.rstrip()])

  return (decode, board, width, height)

def print_board_with_highlight(board, width, height, path=[]):
  highlight = '\033[1m'
  endc = '\033[0m'
  for y in range(0, height):
    row = ''
    for x in range(0, width):
      val = str(get_at(board, width, height, (x,y)))
      if (x,y) in path:
        row += highlight + val + endc
      else:
        row += ' ' if val == '0' else 'X'
    print(row)

def idx_to_x_y(idx, width):
  return (idx % width, int(idx / width))

def x_y_to_idx(xy, width): #xy is a tuple
  return xy[1] * width + xy[0]

def get_at(board, width, height, xy):
  if xy[0] < 0 or xy[1] < 0 or xy[0] >= width or xy[1] >= height:
    return generation % 2
  else:
    return board[x_y_to_idx(xy, width)]

def set_at(board, width, height, xy, value):
  if xy[0] < 0 or xy[1] < 0 or xy[0] >= width or xy[1] >= height:
    pass
  else:
    board[x_y_to_idx(xy, width)] = value

def expand_board(board, width, height):
  expand_amount = 200
  new_board = [0] * ((width + expand_amount) * (height + expand_amount))
  for i in range(0, width):
    for j in range(0, height):
      xy_new = (i + int(expand_amount / 2), j + int(expand_amount / 2))
      xy_orig = (i, j)
      set_at(new_board, width + expand_amount, height + expand_amount, xy_new, get_at(board, width, height, xy_orig))
  return (new_board, width + expand_amount, height + expand_amount)

def get_surroundings(board, width, height, xy):
  digit = 0
  coordinates = []
  for j in range(-1, 2):
    for i in range(-1, 2):
      digit = (digit << 1) + get_at(board, width, height, (xy[0] + i, xy[1] + j))
      coordinates.append((xy[0] + i, xy[1] + j))

  return (digit, coordinates)

def decode_surroundings(value, decode):
  return decode[value]

def process_generation(board, width, height, decode):
  new_board = board.copy()

  for i in range(0, width):
    for j in range(0, height):
      (surroundings, coordinates) = get_surroundings(board, width, height, (i,j))
      set_at(new_board, width, height, (i, j), decode_surroundings(surroundings, decode))
      #print(i, j, surroundings, bin(surroundings), digitstr, ':')
      #print_board_with_highlight(board, width, height, coordinates)
      #print()

  board = new_board

  return (new_board, width, height)

(decode, board, width, height) = read_board()
(board, width, height) = expand_board(board, width, height)
print_board_with_highlight(board, width, height)
for i in range(0, 50):
  (board, width, height) = process_generation(board, width, height, decode)
  generation += 1
  print_board_with_highlight(board, width, height)
  print(i, sum(board))