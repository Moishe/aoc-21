import json
from collections import defaultdict

f = open('/Users/moishe/src/aoc-21/day-8/input/debug.txt')

def get_substrings(s):
  return list(filter(None, s.split(' ')))

def set_from_item(items, idx):
  return set([c for c in list(items)[idx]])

def list_from_item(items, idx):
  return list(items)[idx]

def decode_digit(s):
  m = {
    'd': 'a',
    'e': 'b',
    'a': 'c',
    'f': 'd',
    'g': 'e',
    'b': 'f',
    'c': 'g'
  }


instances = defaultdict(list)

known_segment_list = [
  ['a', 'b', 'c',      'e', 'f', 'g'], # 0, 6
  [          'c',      'f'          ], # 1, 2
  ['a',      'c', 'd', 'e',      'g'], # 2, 5
  ['a',      'c', 'd',      'f', 'g'], # 3, 5
  [     'b', 'c', 'd',      'f'     ], # 4, 4
  ['a', 'b',      'd',      'f', 'g'], # 5, 5
  ['a', 'b',      'd', 'e', 'f', 'g'], # 6, 6
  ['a',      'c',           'f'     ], # 7, 3
  ['a', 'b', 'c', 'd', 'e', 'f', 'g'], # 8, 7
  ['a', 'b', 'c', 'd',      'f', 'g'], # 9, 6
]

known_segment_map = {}
for s in known_segment_list:
  known_segment_map[len(s)] = s

segment_lists_by_length = defaultdict(set)

for l in f:
  (input, output) = l.rstrip().split("|")

  input_digits = get_substrings(input)
  output_digits = get_substrings(output)

  for s in input_digits + output_digits:
    segment_lists_by_length[len(s)].add(''.join(sorted(s)))
  print(segment_lists_by_length)

  # deduction rules:

  # between a 1 and a 7, 
  #   the segment not in the 1 maps to 'a'
  #   the other two map to 'c' or 'f'
  # between a 4 and a 1/7
  #   the two that aren't in the 1 & 7 are 'b' or 'd'
  # if you see an element with 6 elements
  #   it's either a 6, 9 or a 0
  #   if it doesn't have one of the 'other two' from 1 & 7 then it's a 6 or a 9
  #   otherwise it's a zero
  segment_map = {}
  number_map = {}

  number_map[1] = list_from_item(segment_lists_by_length[4], 0)
  number_map[4] = list_from_item(segment_lists_by_length[4], 0)
  number_map[7] = list_from_item(segment_lists_by_length[3], 0)
  number_map[8] = list_from_item(segment_lists_by_length[7], 0)

  segment_map['a'] = list(set_from_item(segment_lists_by_length[3], 0) - set_from_item(segment_lists_by_length[2], 0))
  
  maybe_six_or_zero = [set([c for c in x]) for x in list(segment_lists_by_length[6])]
  for i in maybe_six_or_zero:
    print(''.join(sorted(list(i))))
  print(json.dumps(segment_map))
  print(json.dumps(number_map))
  exit(0)
