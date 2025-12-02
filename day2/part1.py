def is_valid(num):
    str_int = str(num)
    if len(str_int) == 1 or len(str_int)%2==1:
        return True
    first_part = str_int[:len(str_int)//2]
    second_part = str_int[len(str_int)//2:]
    return first_part != second_part

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

