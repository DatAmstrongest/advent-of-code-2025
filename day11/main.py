def part1(device_graph):
    counter = 0
    device_stack = ["you"]
    while len(device_stack)!=0:
        device = device_stack.pop()
        if device == "out":
            counter += 1
            continue
        else:
            for list_device in device_graph[device]:
                device_stack.append(list_device)

    return counter
def part2(device_graph, current_device, is_dac, is_fft, counter):
    if current_device == "out":
        if is_dac and is_fft:
            counter[0] += 1
        return
    if current_device == "dac":
        is_dac = True
    if current_device == "fft":
        is_fft = True
    for device in device_graph[current_device]:
        part2(device_graph, device, is_dac, is_fft, counter)
    return counter[0]
def read_file(filename):
    device_graph={}
    with open(filename) as file:
        for line in file.readlines():
            device_graph[line.strip().split(" ")[0][:-1]] = line.strip().split(" ")[1:]
    return device_graph

device_graph = read_file("data.txt")
#print(f"Part1 answer: {part1(device_graph)}")
print(f"Part2 answer: {part2(device_graph, 'svr', False, False, [0])}")

