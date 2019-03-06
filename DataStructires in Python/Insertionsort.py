def insertionsort(l):
    for start in range(len(l)):
        pos = start
        while pos > 0 and l[pos] < l[pos-1]:
            (l[pos-1],l[pos]) = (l[pos],l[pos-1])
            pos = pos - 1
    return l
print(insertionsort([9,6,7,5,3,8]))