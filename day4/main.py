def is_roll(r, c, matrix):
    if r<0 or r>=len(matrix) or c<0 or c>=len(matrix[0]):
        return 0
    return  matrix[r][c] == "@"

def is_accessible(r, c, matrix):
    counter = is_roll(r-1, c, matrix) \
        + is_roll(r+1, c, matrix) \
        + is_roll(r, c+1, matrix) \
        + is_roll(r, c-1, matrix) \
        + is_roll(r-1, c+1, matrix) \
        + is_roll(r-1, c-1, matrix) \
        + is_roll(r+1, c+1, matrix) \
        + is_roll(r+1, c-1, matrix)
    return counter < 4

def read_file():
    matrix = []
    with open("data.txt") as file:
        for line in file.readlines():
            matrix.append(list(line.strip()))

    return matrix




def part1(matrix):
    answer = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "@" and is_accessible(r, c, matrix):
                answer += 1
    return answer

def part2(matrix):
    prev_answer = -1
    answer = 0
    while (prev_answer != answer):
        prev_answer = answer
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "@" and is_accessible(r, c, matrix):
                    matrix[r][c] = "."
                    answer += 1
        
    return answer


if __name__ == "__main__":
    matrix = read_file()
    
    print(f"Part1 Answer: {part1(matrix)}")
    print(f"Part2 Answer: {part2(matrix)}")

