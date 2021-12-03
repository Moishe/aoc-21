f = open('/Users/moishe/src/aoc-21/day-2/input/input.txt')

x = 0
y = 0
aim = 0

for l in f:
    (direction, scalar) = l.rstrip().split(' ')
    scalar = int(scalar)
    if direction == 'forward':
        x += scalar
        y += scalar * aim
    elif direction == 'down':
        aim += scalar
    elif direction == 'up':
        aim -= scalar
    else:
        print("weird: %s" % l)

print("x: %d, y: %d (%d)" % (x, y, x * y))