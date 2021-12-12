import json
from copy import copy
from collections import defaultdict
f = open('/Users/moishe/src/aoc-21/day-12/input/input.txt')

edges = defaultdict(list)

for l in f:
  (node1, node2) = l.rstrip().split('-')
  edges[node1].append(node2)
  edges[node2].append(node1)

visited = []
paths = []
def to_end(node, path):
  global paths
  global visited

  print(node, path)
  if not node.isupper():
    if node in path:
      return

  path += [node]

  if node == 'end':
    paths.append(path)
    return

  for node in edges[node]:
    to_end(node, copy(path))

to_end('start', [])
print('\n'.join([str(x) for x in paths]))
print(len(paths))