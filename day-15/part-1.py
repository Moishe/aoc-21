import heapq

f = open('/Users/moishe/src/aoc-21/day-15/input/input.txt')

width = 0
height = 0
board = []
queue = []
neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for l in f:
  width = len(l.rstrip())
  height += 1
  board.extend([int(c) for c in l.rstrip()])

def idx_to_x_y(idx):
  global width
  return (idx % width, int(idx / width))

def x_y_to_idx(xy): #xy is a tuple
  global width
  return xy[1] * width + xy[0]

def enqueue(xy, prev_cost, path):
  global queue
  if xy not in path:
    cost = prev_cost + float(board[x_y_to_idx(xy)]) / float(len(path) + 1)
    cost -= width - xy[0] + height - xy[1]
    path.append(xy)
    heapq.heappush(queue, (cost, xy, path))

# breadth first search the board
enqueue((0,0), 0, [])

found_path = False
iterations = 0
while not found_path and len(queue):
  (cost, xy, path) = heapq.heappop(queue)
  iterations += 1
  if (xy == (width - 1, height - 1)):
    found_path = True
  for neighbor in neighbors:
    (x1, y1) = (xy[0] + neighbor[0], xy[1] + neighbor[1])
    if x1 >= 0 and x1 < width and y1 >= 0 and y1 < height:
      enqueue((x1,y1), cost, path.copy())

if found_path:
  total_cost = -board[0]
  for xy in path:
    total_cost += board[x_y_to_idx(xy)]  
  print("Found it. Total cost is %d\n" % total_cost, iterations)
else:
  print(":shrug:")