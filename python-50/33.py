input_str = input("enter string:")
count = int(input("enter the number of zeros:"))

total_count = len(input_str) + count

print("final string", input_str.zfill(total_count))
