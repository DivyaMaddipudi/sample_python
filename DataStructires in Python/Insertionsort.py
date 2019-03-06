def insertionsort(l):
    for start in range(len(l)):
        pos = start
        while pos > 0 and l[pos] < l[pos-1]:
            (l[pos-1],l[pos]) = (l[pos],l[pos-1])
            pos = pos - 1
    return l
l = list(range(200,0,-1))
print(insertionsort(l))