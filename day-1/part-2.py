f = open('/Users/moishe/src/aoc-21/day-1/input/input2.txt')
prev = []
found = 0
for l in f:
    print(prev)
    i = int(l)
    prev.append(i)
    if len(prev) > 4:
        prev.pop(0)
    if (len(prev) == 4):
        print("%s: %d, %s: %d" % (prev[0:3], sum(prev[0:3]), prev[1:4], sum(prev[1:4])))
        if sum(prev[0:3]) < sum(prev[1:4]):
            found += 1

print(found)