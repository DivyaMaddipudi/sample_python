l1 = ["java","r","python","firebase","swift","django","flask"]

rem = ["java","r"]
nl = []

for e in l1:
    

    if e not in rem:
        nl.append(e)
print(nl)