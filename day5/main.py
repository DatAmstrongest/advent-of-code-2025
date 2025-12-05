def part1(intervals, items):
    counter = 0
    for item in items:
        for interval in intervals:
            if interval[0]<=item and interval[1]>=item:
                counter += 1
    return counter

def part2(intervals, items):
    total = 0
    for interval in intervals:
        total += interval[1] - interval[0] + 1
    return total

def combine_intervals(intervals):
    intervals.sort()
    new_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        new_interval = new_intervals[-1]
        current_interval = intervals[i]
        if current_interval[0] <= new_interval[1]:
            new_intervals[-1][1] = max(current_interval[1], new_interval[1])
        else:
            new_intervals.append(current_interval)
    return new_intervals
            

def read_data():
    items = []
    intervals = []
    with open("data.txt") as file:
        is_item = False
        for line in file.readlines():
            if line == "\n":
                is_item=True
                continue
            if is_item:
                items.append(int(line.strip()))
            else:
                intervals.append([int(line.strip().split("-")[0]), int(line.strip().split("-")[1])])
    intervals = combine_intervals(intervals)
    return items, intervals


if __name__ == "__main__":
    items, intervals = read_data()
    print(f"Part1 Answer: {part1(intervals, items)}")
    print(f"Part2 Answer: {part2(intervals, items)}")
    
