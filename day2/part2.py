def is_valid(num):
    is_valid = False
    str_int = str(num)
    if len(str_int) == 1:
        return True
    for i in range(1,len(str_int)//2+1):
        is_valid=False
        for k in range(i, len(str_int), i):
            if str_int[k-i:k] != str_int[k:k+i]:
                is_valid = True
        if is_valid == False:
            return is_valid
    return is_valid 

sum = 0
ranges = []
with open("data.txt") as file:
    for line in file.readlines():
        ranges = line.split(",")

for inverval in ranges:
    [start, end] = inverval.split("-")
    for i in range(int(start), int(end)+1):
        if not is_valid(i):
            sum += i
print(sum)