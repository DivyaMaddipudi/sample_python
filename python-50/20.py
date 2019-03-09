dic = {"name":"divya",
        "dept":"cse",
        "year":3
}
new_key = input("enter key:")

if new_key in dic:
    print("key is present")
    print("value is",dic[new_key])
else:
    print("key is not present")