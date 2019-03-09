import pathlib
file = pathlib.Path("E:\samples\sample1.txt")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")