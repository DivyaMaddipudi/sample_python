def del_key(n):
        
    dic = {"r":1,
        "python":5,
        "java":3,
        "swift":4,
        "flutter":2}

    del dic[n]

    return dic
l = input("eneter one key value:")
print(del_key(l))