from functools import reduce

def part1(nums, operations):
    total_sum = 0
    for i in range(len(operations)):
        local_sum = 0
        operation = operations[i]

        if operation == "+":
            for k in range(len(nums)):
                local_sum += nums[k][i]

        elif operation == "*":
            for k in range(len(nums)):
                if local_sum == 0:
                    local_sum = nums[k][i]
                else:
                    local_sum *= nums[k][i]
        total_sum += local_sum
    return total_sum

def part2(lines):
    total_sum = 0
    nums = []
    pass_next = False
    for c in range(len(lines[0])-1,-1,-1):
        str_num = ""
        if pass_next:
            pass_next = False
            continue
        for r in range(len(lines)):
            if r == len(lines)-1:
                if r!="":
                    nums.append(int(str_num))
                    if lines[r][c]=="*":
                        total_sum += reduce(lambda x, y: x*y, nums)
                        pass_next = True
                        nums = []
                    if lines[r][c]=="+":
                        total_sum += reduce(lambda x, y: x+y, nums)
                        pass_next = True
                        nums = []
            else:
                if lines[r][c] == " ":
                    str_num += ""
                else:
                    str_num += lines[r][c]

    return total_sum

            


def read_file(file_name):
    nums = []
    operations = []
    lines = []

    with open(file_name) as file:
        for line in file.readlines():
            lines.append(line.strip("\n"))
            line = line.strip()
            if (line[0].isdigit()):
                nums.append([int(num) for num in line.split(" ") if num.isdigit()])
            else:
                operations = [operation for operation in line.strip().split(" ") if operation!='']
    return nums, operations, lines


if __name__ == "__main__":
    nums, operations, lines = read_file("data.txt")
    print(f"Part1 Answer: {part1(nums, operations)}")
    print(f"Part2 Answer: {part2(lines)}")

    