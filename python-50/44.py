old_dic = {'A':1,
           'B':2,
           'C':3,
           'D':4}
new_dic =  dict([(value,key) for key, value in old_dic.items()])

print(new_dic)