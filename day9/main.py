def part1(red_tiles):
    max_area = 0
    for i in range(len(red_tiles)):
        for j in range(i, len(red_tiles)):
            current_area = abs(red_tiles[i][0]-red_tiles[j][0]+1)*abs(red_tiles[i][1]-red_tiles[j][1]+1)
            max_area = current_area if current_area > max_area else max_area
    return max_area


def part2(red_tiles):
    return

def read_file(filename):
    red_tiles = []
    with open(filename) as file:
        for line in file.readlines():
            red_tiles.append([int(num) for num in line.strip().split(",")])
    return red_tiles

red_tiles = read_file("data.txt")
print(f"Part1 answer: {part1(red_tiles)}")
