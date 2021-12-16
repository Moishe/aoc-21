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

def parse_literal(bytes):
  value = 0
  offset = 6
  more_bit = 1
  while more_bit:
    more_bit = get_bits(bytes, offset, 1)
    value = (value << 4) | get_bits(bytes, offset + 1, 4)
    offset += 5

  return value

def parse_operator(bytes):
  pass

def parse_value(value):
  print(value)
  bytes = convert_hex_to_bytes(value)

  # first 3 bits are the version
  version = bytes[0] >> 5

  # next 3 bits are the type
  type = bytes[0] >> 2 & 7

  if type == 4:
    return ([version], parse_literal(bytes))
  else:
    (versions, result) = parse_operator(bytes)
    return (versions + [version], result)


