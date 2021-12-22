import re

f = open('/Users/moishe/src/aoc-21/day-22/input/input.txt')

on_cubes = set()

bounds = [-50, 50]

for l in f:
  l = l.rstrip()
  (state,x1,x2,y1,y2,z1,z2) =  re.match('(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', l).groups()
  print(state,x1,x2,y1,y2,z1,z2)

  (x1, x2, y1, y2, z1, z2) = [int(v) for v in [x1, x2, y1, y2, z1, z2]]

  for x in range(max(x1, bounds[0]), min(x2, bounds[1]) + 1):
    for y in range(max(y1, bounds[0]), min(y2, bounds[1]) + 1):
      for z in range(max(z1, bounds[0]), min(z2, bounds[1]) + 1):
        if state == 'on':
          on_cubes.add((x,y,z))
        else:
          on_cubes.discard((x,y,z))
        
print(len(list(on_cubes)))