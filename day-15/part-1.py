import heapq
import sys

f = open('/Users/moishe/src/aoc-21/day-15/input/input.txt')

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

def print_board_with_highlight(path):
  for y in range(0, height):
    row = ''
    for x in range(0, width):
      val = str(board[x_y_to_idx((x,y))])
      if (x,y) in path:
        row += highlight + val + endc
      else:
        row += val
    print(row)

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

# lowest cost to get to each node
board_costs = [sys.maxsize] * len(board)
board_paths = [[]] * len(board)

unvisited_nodes = set()
for i in range(0, len(board)):
  unvisited_nodes.add(idx_to_x_y(i))

found = False

# start at 0,0
board_costs[0] = 0
queue = []
heapq.heappush(queue, (0, (0,0), []))

while not found:
  (cost, xy, path) = heapq.heappop(queue)
  unvisited_nodes.remove(xy)
  if (xy == (width - 1, height - 1)):
    print("Found it")
    print(highlight + str(cost) + endc)
    if debug_print:
      print_board_with_highlight(path)
    found = True
  else:
    changed = []
    for neighbor in neighbors:
      (x1, y1) = (xy[0] + neighbor[0], xy[1] + neighbor[1])
      if x1 >= 0 and x1 < width and y1 >= 0 and y1 < height:
        if (x1,y1) in unvisited_nodes:
          idx = x_y_to_idx((x1,y1))
          tentative_cost = cost + board[idx]
          if tentative_cost < board_costs[idx]:
            was_infinite = board_costs[idx] == sys.maxsize
            board_costs[idx] = tentative_cost
            board_paths[idx] = path + [xy]
            if (was_infinite):
              heapq.heappush(queue, (board_costs[idx], (x1, y1), board_paths[idx]))
            else:
              changed.append((x1,y1))
    if changed:
      for (idx, (cost, xy, path)) in enumerate(queue):
        if xy in changed:
          board_idx = x_y_to_idx(xy)
          queue[idx] = (board_costs[board_idx], xy, board_paths[board_idx])
      heapq.heapify(queue)
