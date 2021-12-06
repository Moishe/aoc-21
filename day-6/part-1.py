f = open('/Users/moishe/src/aoc-21/day-6/input/input.txt')

fishes = [int(x) for x in f.readline().rstrip().split(",")]
print(fishes)

for i in range(0,80):
  new_fishes = [(x - 1) % 7 if x < 7 else x - 1 for x in fishes]
  for (fish, old_fish) in zip(new_fishes, fishes):
    if fish == 6 and old_fish == 0:
      new_fishes.append(8)
  fishes = new_fishes
  print(i, len(fishes))

print(len(fishes))