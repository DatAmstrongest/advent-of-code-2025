sequence = []
with open("data.txt") as file:
    for line in file.readlines():
        sequence.append(line.strip())
zero_counter = 0
starting_point = 50
for char in sequence:
    if starting_point == 0:
        zero_counter += 1
    value = int(char[1:])
    if char[0] == "L":
        starting_point = (starting_point - value)%100
    else:
        starting_point = (starting_point + value)%100

print(zero_counter)


    