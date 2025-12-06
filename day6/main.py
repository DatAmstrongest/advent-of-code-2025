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

def part2():
    return

def read_file(file_name):
    nums = []
    operations = []

    with open(file_name) as file:
        for line in file.readlines():
            line = line.strip()
            if (line[0].isdigit()):
                nums.append([int(num) for num in line.split(" ") if num.isdigit()])
            else:
                operations = [operation for operation in line.strip().split(" ") if operation!='']
    return nums, operations


if __name__ == "__main__":
    nums, operations = read_file("data.txt")

    print(f"Part1 Answer: {part1(nums, operations)}")

    