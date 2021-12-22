class Cuboid:
  smallest: list
  biggest: list

  def __init__(p1:list, p2:list):
    assert(len(p1) == len(p2))
    for idx in range(0, len(p1)):
      (small, big) = sorted([p1[idx], p2[idx])
      smallest[idx] = small
      biggest[idx] = big

  def overlaps(other:Cuboid):
    pass



