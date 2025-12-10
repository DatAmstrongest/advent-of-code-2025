from queue import Queue

def part1(target_states, all_buttons):
    total = 0
    for i in range(len(target_states)):
        target_state = target_states[i]
        buttons = all_buttons[i]
        counter = 0
        state_queue = Queue()
        state_queue.put(["."*len(target_state), counter])
        while(not state_queue.empty()):
            current_state, counter = state_queue.get()
            if current_state == target_state:
                break
            for button in buttons:
                temp_state = list(current_state)
                for change in button:
                    temp_state[change] = "." if temp_state[change] == "#" else "#"
                state_queue.put(["".join(temp_state), counter+1])
        total += counter

    return total

def part2():
    return

def read_file(filename):
    buttons = []
    states = []
    voltages = []
    with open(filename) as file:
        for line in file.readlines():
            data = line.strip().split(" ")
            states.append(data[0][1:-1])
            local_buttons = []
            for button_data in data[1:-1]:
                local_buttons.append([int(button) for button in button_data[1:-1].split(",")])
            buttons.append(local_buttons)
            voltages.append([int(voltage )for voltage in data[-1][1:-1].split(",")])
    return states, buttons, voltages

states, buttons, voltages = read_file("data.txt")
print(f"Part1 answer: {part1(states, buttons)}")
            
