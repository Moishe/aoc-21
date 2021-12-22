import re
from typing import NamedTuple

f = open('/Users/moishe/src/aoc-21/day-22/input/debug.txt')

on_cubes = 0

cubes = {
  'on': [],
  'off': []
}

class Point(NamedTuple):
    x: int
    y: int
    z: int

class Rect(NamedTuple):
  a: Point
  b: Point

for l in f:
  l = l.rstrip()
  (state,x1,x2,y1,y2,z1,z2) =  re.match('(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', l).groups()
  print(state,x1,x2,y1,y2,z1,z2)

  (x1, x2, y1, y2, z1, z2) = [int(v) for v in [x1, x2, y1, y2, z1, z2]]

  (x1, x2) = sorted([x1,x2])
  (y1, y2) = sorted([y1,y2])
  (z1, z2) = sorted([z1,z2])

  r = Rect(a=Point(x=x1, y=y1, z=z1), b=Point(x=x2, y=y2, z=z2))

  cubes[state].append(r)

print(cubes)

def split_cube(cube, remove):
  pass

def overlap(a, b):
  if cube.b.x >= remove.a.x:
    if cube.b.y >= remove.a.y:
      if cube.b.z >= remove.a.z:
        return True
  pass

def remove_cube(on_cubes, off_cube):
  for cube in on_cubes:
    if overlap(cube, off_cube):
      new_cubes = split_cube(cube, off_cube)