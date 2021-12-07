f = open('/Users/moishe/src/aoc-21/day-7/input/input.txt')

crabs = [int(x) for x in f.readline().rstrip().split(",")]
print(crabs, min(crabs), max(crabs))

# brute force
start = min(crabs)
end = max(crabs)

def sum_of_all(n):
  n = abs(n)
  return int((n * n + n) / 2)

min_sum = None
min_loc = 0
for i in range(start, end + 1):
  sum = 0
  for crab in crabs:
    sum += sum_of_all(crab - i)

  if not min_sum or sum < min_sum:
    min_sum = sum
    min_loc = i

print("%d, %d" % (min_sum, min_loc))