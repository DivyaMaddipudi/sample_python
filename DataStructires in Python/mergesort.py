def merge(a,b):
    (C,m,n) = ([],len(a),len(b))
    i,j = 0, 0
    while i+j < m+n:

        if j == n:
            C.append(a[i])
            i = i + 1

        elif i == m:
            C.append(b[j])
            j = j + 1

   
        elif a[i] <= b[j]:
            C.append(a[i])
            i = i + 1      

        elif a[i] > b[j]:
            C.append(b[j])
            j = j + 1        

    return C
l = list(range(1,75,2))
m = list(range(1,100,3))
print(merge(l,m))