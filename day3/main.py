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

def part2(lines):
    total = 0
    for line in lines:
        voltage_array = []
        for i in range(len(line)):
            digit = line[i]
            discards = len(line) - i - (12 - len(voltage_array))
            if len(voltage_array) == 0 :
                voltage_array.append(digit)
            elif int(digit) >= int(voltage_array[-1]) and discards > 0:
                while len(voltage_array) > 0 and  int(digit) > int(voltage_array[-1]) and discards > 0:
                    voltage_array.pop()
                    discards -= 1
                if len(voltage_array) < 12:
                    voltage_array.append(digit)
            elif len(voltage_array) < 12:
                voltage_array.append(digit)
        total += int("".join(voltage_array))

    return total




def read_data():
    lines = []
    with open("data.txt") as file:
        for line in file.readlines():
            lines.append(list(line.strip()))
    return lines

lines = read_data()
print(f"Part1 answer: {part1(lines)}")
print(f"Part2 answer: {part2(lines)}")
