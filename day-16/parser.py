def get_bits(bytes, offset, count):
  start_byte = int(offset / 8)
  end_byte = int((offset + count) / 8)

  start_bit = offset % 8
  end_bit = (offset + count) % 8

  if start_byte == end_byte:
    mask = pow(2, end_bit - start_bit) - 1 << (8 - end_bit)
    shift = 8 - end_bit

    return (bytes[start_byte] & mask) >> shift
  else:
    start_value = (bytes[start_byte] & (pow(2, 8 - start_bit) - 1))
    end_value = ((bytes[end_byte] & ((pow(2, end_bit) - 1)) << (8 - end_bit))) >> (8 - end_bit)    

    value = start_value
    for i in range(start_byte + 1, end_byte):
      value = value << 8 + bytes[i]
    return (value << end_bit) + end_value

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

  return (offset, value)

def parse_operator(bytes, start_bit):
  all_versions = []
  all_results = []
  length_type = get_bits(bytes, start_bit, 1)
  if length_type == 0:
    length = get_bits(bytes, start_bit + 1, 15)
    offset = start_bit + 16
    while offset < start_bit + 16 + length:
      (versions, offset, results) = parse_value(bytes, offset)
      all_versions.extend(versions)
      all_results.extend(results)
  return (all_versions, offset, all_results)

def parse_value(bytes, start_bit=0):
  versions = []
  results = []

  # first 3 bits are the version
  version = get_bits(bytes, start_bit, 3)

  # next 3 bits are the type
  type = get_bits(bytes, start_bit + 3, 3)

  if type == 4:
    (new_offset, result) = parse_literal(bytes, start_bit + 6)
    versions = [version]
    results = [result]
  else:
    (versions, new_offset, results) = parse_operator(bytes, start_bit + 6)
    versions = [version] + versions

  return (versions, new_offset, results)


