import json
from collections import defaultdict

f = open('/Users/moishe/src/aoc-21/day-8/input/input.txt')

def get_substrings(s):
  return list(filter(None, s.split(' ')))

def set_from_item(items, idx):
  return set([c for c in list(items)[idx]])

def list_from_item(items, idx):
  return list(items)[idx]

instances = defaultdict(list)

total_sum = 0
for l in f:
  segment_lists_by_length = defaultdict(set)
  (input, output) = l.rstrip().split("|")

  input_digits = get_substrings(input)
  output_digits = get_substrings(output)

  for s in input_digits + output_digits:
    segment_lists_by_length[len(s)].add(''.join(sorted(s)))
  #print(segment_lists_by_length)

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

  number_map[1] = set_from_item(segment_lists_by_length[2], 0)
  number_map[4] = set_from_item(segment_lists_by_length[4], 0)
  number_map[7] = set_from_item(segment_lists_by_length[3], 0)
  number_map[8] = set_from_item(segment_lists_by_length[7], 0)

  segment_map['a'] = list(set_from_item(segment_lists_by_length[3], 0) - set_from_item(segment_lists_by_length[2], 0))
  
  maybe_six_or_zero_or_nine = [set([c for c in x]) for x in list(segment_lists_by_length[6])]
  #print(''.join(sorted(list(number_map[1]))))
  maybe_zero_or_nine = []
  for i in maybe_six_or_zero_or_nine:
    if len(list(number_map[1].intersection(i))) == 1:
      number_map[6] = i
    else:
      maybe_zero_or_nine.append(i)

  maybe_five = [set([c for c in x]) for x in list(segment_lists_by_length[5])]
  for i in maybe_five:
    if len(list(number_map[6].intersection(i).intersection(number_map[1]))) == 0:
      number_map[2] = i
    elif len(list(number_map[1].intersection(i))) == 2:
      number_map[3] = i
    else:
      number_map[5] = i

  middle_line = number_map[2].intersection(number_map[4])
  middle_line = number_map[5].intersection(middle_line)
  #print("middle line ", list(middle_line))
  for i in maybe_zero_or_nine:
    if len(list(middle_line.intersection(i))) == 0:
      number_map[0] = i
    else:
      number_map[9] = i

  map_to_number = {}
  #print(json.dumps(segment_map))
  for k in sorted(number_map.keys()):
    #print("%s: %s" % (str(k), list(number_map[k])))
    map_to_number[''.join(sorted(list(number_map[k])))] = k

  #print(json.dumps(map_to_number, indent = 2))

  total_digit = ''
  for digit in output_digits:
    sorted_digit = ''.join(sorted([c for c in digit]))
    total_digit += str(map_to_number[sorted_digit])

  print("%s: %d" % (total_digit, int(total_digit)))
  total_sum += int(total_digit)

print("sum: %d" % total_sum)
