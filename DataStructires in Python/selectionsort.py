def selectionsort(l):
    for start in range(len(l)):
        
        for i in range(start,len(l)):
            minpos = start
            if l[i] < l[minpos]:
                minpos = i
                (l[start], l[minpos]) = (l[minpos], l[start])   
    return l
print(selectionsort([3,2,7,1,30,5,4]))      