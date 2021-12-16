import parser

f = open('/Users/moishe/src/aoc-21/day-16/input/input.txt')

version_sum = 0
for l in f:
  s = l.rstrip()
  bytes = parser.convert_hex_to_bytes(s)
  (versions, new_offset, results) = parser.parse_value(bytes)
  version_sum += sum(versions)

print(version_sum)
