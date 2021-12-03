f = open('input/input2.txt')
prev = None
for l in f:
    i = int(l)
    if prev:
        if i > prev:
            print("%d %d %s" % (prev, i, "increased"))
        else:
            print("%d %d %s" % (prev, i, "decreased"))
        
#    if prev and i > prev:
#        print(i)
    prev = i
