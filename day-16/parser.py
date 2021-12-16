import functools

highlight = '\033[1m'
endc = '\033[0m'

debug_output = False

def print_highlight(bytes, start, end, context=''):
  if debug_output:
    s = ''.join([format(byte, '08b') for byte in bytes])
    print("%s (%s)" % (s[:start] + highlight + s[start:end] + endc + s[end:], context))

def get_bits(bytes, offset, count):
  # gonna stop being clever
  s = ''.join([format(byte, '08b') for byte in bytes])
  bits = s[offset:offset+count]
  return int(bits, 2)

def convert_hex_to_bytes(value):
  bytes = []
  for i in range(0, len(value) - 1, 2):
    byte = int(value[i:i+2], 16)
    bytes.append(byte)
  return bytes

def parse_literal(bytes, start_bit):
  value = 0
  offset = start_bit
  more_bit = 1
  while more_bit:
    more_bit = get_bits(bytes, offset, 1)
    value = (value << 4) | get_bits(bytes, offset + 1, 4)
    offset += 5

  print_highlight(bytes, start_bit, offset, "Parsed literal %s" % value)

  return (offset, value)

def parse_operator(bytes, start_bit):
  all_versions = []
  all_results = []
  length_type = get_bits(bytes, start_bit, 1)
  if length_type == 0:
    length = get_bits(bytes, start_bit + 1, 15)
    print_highlight(bytes, start_bit, start_bit + 15, "Parsing length operator %d, %d" % (length_type, length))
    offset = start_bit + 16
    while offset < start_bit + 16 + length:
      (versions, offset, results) = parse_value(bytes, offset)
      all_versions.extend(versions)
      all_results.append(results)
  else:
    count = get_bits(bytes, start_bit + 1, 11)
    print_highlight(bytes, start_bit + 1, start_bit + 12, "Parsing count operator %d" % count)
    current = 0
    offset = start_bit + 12
    while current < count:
      (versions, offset, results) = parse_value(bytes, offset)
      all_versions.extend(versions)
      all_results.append(results)
      current += 1

  return (all_versions, offset, all_results)

def parse_value(bytes, start_bit=0):
  versions = []

  # first 3 bits are the version
  version = get_bits(bytes, start_bit, 3)
  print_highlight(bytes, start_bit, start_bit + 3, "Version: %d" % version)

  # next 3 bits are the type
  type = get_bits(bytes, start_bit + 3, 3)
  print_highlight(bytes, start_bit + 3, start_bit + 6, "Type: %d" % type)

  if type == 4:
    (new_offset, result) = parse_literal(bytes, start_bit + 6)
    versions = [version]
  else:
    (versions, new_offset, results) = parse_operator(bytes, start_bit + 6)
    if type == 0: # sum
      result = sum(results)
    elif type == 1: # product
      result = functools.reduce(lambda x,y: x * y, results)
    elif type == 2: # min
      result = min(results)
    elif type == 3: # max
      result = max(results)
    elif type == 5: # greater than
      result = 1 if results[0] > results[1] else 0
    elif type == 6: # less than
      result = 1 if results[0] < results[1] else 0
    elif type == 7: # equal to
      result = 1 if results[0] == results[1] else 0
    versions = [version] + versions

  return (versions, new_offset, result)


