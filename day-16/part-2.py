import parser

f = open('/Users/moishe/src/aoc-21/day-16/input/input.txt')

s = f.readline().rstrip()
bytes = parser.convert_hex_to_bytes(s)
(versions, new_offset, result) = parser.parse_value(bytes)

print(result)
