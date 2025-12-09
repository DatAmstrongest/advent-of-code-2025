def part1(matrix):
    counter = 0
    for r in range(1,len(matrix)):
        for c in range(0, len(matrix[0])):
            if matrix[r-1][c]=="S":
                matrix[r][c] = "|"
            if matrix[r][c] == "^" and matrix[r-1][c] == "|":
                counter +=1
                matrix[r][c-1] = "|"
                matrix[r][c+1] = "|"
            else: 
                if matrix[r-1][c] == "|":
                    matrix[r][c] = "|"
    return counter

def part2():
    return


def read_file():
    matrix = []
    with open("data.txt") as file:
        for line in file.readlines():
            matrix.append(list(line.strip()))
    return matrix


matrix = read_file()
print(f"Part1 answer: {part1(matrix)}")

