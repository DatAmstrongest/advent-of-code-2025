def part1(lines):
    total = 0
    for line in lines:
        biggest_digit = None
        biggest_voltage = 0
        for digit in line:
            if biggest_digit != None and int(biggest_digit+digit) > biggest_voltage:
                biggest_voltage = int(biggest_digit+digit)
            if biggest_digit == None or int(digit) > int(biggest_digit):
                biggest_digit = digit
        total += biggest_voltage
    return total
def part2():
    return

def read_data():
    lines = []
    with open("data.txt") as file:
        for line in file.readlines():
            lines.append(list(line.strip()))
    return lines

lines = read_data()
print(part1(lines))
