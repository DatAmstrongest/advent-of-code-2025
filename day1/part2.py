sequence = []
with open("data.txt") as file:
    for line in file.readlines():
        sequence.append(line.strip())
zero_counter = 0
starting_point = 50
for char in sequence:
    value = int(char[1:])
    zero_counter += value//100
    value = value % 100

    if char[0] == "L":
        if starting_point - value <= 0 and starting_point != 0:
            zero_counter += 1
        starting_point = (starting_point - value)%100
    else:
        if starting_point + value >= 100 and starting_point != 0:
            zero_counter += 1
        starting_point = (starting_point + value)%100

print(zero_counter)
