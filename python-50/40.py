import operator

d = {'java':10,
        'r':6,
        'python':18,
        'firebase':16
}

print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)