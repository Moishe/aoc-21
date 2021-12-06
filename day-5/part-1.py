f = open('/Users/moishe/src/aoc-21/day-5/input/input.txt')

lines = []
max_x = 0
max_y = 0
for l in f:  
  ((x1,y1),(x2,y2)) = [[int(i) for i in pair.split(',')] for pair in l.rstrip().split(' -> ')]
  max_x = max(max(max_x, x1), x2)
  max_y = max(max(max_y, y1), y2)
  lines.append(((x1,y1),(x2,y2)))

print(lines)
print("%d / %d" % (max_x, max_y))

board = []
for i in range(0, max_y + 1):
  row = []
  for j in range(0, max_x + 1):
    row.append(0)
  board.append(row)

for line in lines:
  ((x1, y1), (x2, y2)) = line
  if x1 == x2:
    start = min(y1, y2)
    end = max(y1, y2)
    for i in range(start, end + 1):
      board[i][x1] += 1
  elif y1 == y2:
    start = min(x1, x2)
    end = max(x1, x2)
    for i in range(start, end + 1):
      board[y1][i] += 1
  else:
    if (x1 < x2):
      startx = x1
      starty = y1
      endx = x2
      endy = y2
    else:
      startx = x2
      starty = y2
      endx = x1
      endy = y1

    if endy > starty:
      slope = 1
    else:
      slope = -1
    #print("%d, %d -> %d, %d" % (startx, starty, endx, endy))
    for i in range(0, endx - startx + 1):
      #print("%d, %d" % (i + startx, i * slope + starty))
      board[i * slope + starty][i + startx] += 1

total = 0
for row in board:
  total += len(list(filter(lambda x: x > 1, row)))
  #print("%s (%d)" % (' '.join([str(x) for x in row]), total))

print(total)
