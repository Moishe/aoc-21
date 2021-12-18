def add_leftmost(number, val):
  if type(number) == int:
    return number + val
  else:
    if len(number) != 2:
      print("nope")
      exit(1)
    return [add_leftmost(number[0], val), number[1]]

def add_rightmost(number, val):
  if type(number) == int:
    return number + val
  else:
    if len(number) != 2:
      print("nope")
      exit(1)
    return [number[0], add_rightmost(number[1], val)]

def explode(number, depth=0):
  if type(number) == int:
    return (0, 0, number)

  if len(number) != 2:
    print("nope")
    exit(1)

  if (depth == 4):
    return (number[0], number[1], 0)
  else:
    (ll, lr, vl) = explode(number[0], depth + 1)
    (rl, rr, vr) = explode(number[1], depth + 1)
    if lr:
      number[1] = add_leftmost(number[1], lr)
    if rl:
      number[0] = add_rightmost(number[0], rl)
    return (ll, rr, (vl, vr))

def split(number):
  pass

def reduce(number):
  if len(number) != 2:
    print("nope")
    exit(1)

  left = number[0]
  right = number[1]

  (ll, lr, lremain) = explode(left)
  (rl, rr, rremain) = explode(right)

  return (lremain, rremain)

def magnitude(number):
  if type(number[0]) is int:
    l = number[0]
  else:
    l = magnitude(number[0])

  if type(number[1]) is int:
    r = number[1]
  else:
    r = magnitude(number[1])

  return 3 * l + 2 * r