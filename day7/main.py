from collections import defaultdict
import sys
import copy

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


def part2(matrix):
    path_count = {}
    for j, c in enumerate(matrix[0]):
        if c == "S":
            path_count[j] = 1
            break
    for i in range(len(matrix) - 1):
        next_count = defaultdict(int)
        for pos, count in path_count.items():
            next_char = matrix[i+1][pos]
            if next_char == "^":
                next_count[pos-1] += count
                next_count[pos+1] += count
            else:
                next_count[pos] += count
        path_count = next_count
    return sum(path_count.values())
    
    


def read_file():
    matrix = []
    with open("data.txt") as file:
        for line in file.readlines():
            matrix.append(list(line.strip()))
    return matrix


matrix = read_file()
print(f"Part1 answer: {part1(copy.deepcopy(matrix))}")
print(f"Part2 answer: {part2(copy.deepcopy(matrix))} ")

