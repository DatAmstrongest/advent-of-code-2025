def part1(boxes, distances, limit):
    counter = 0
    groups = []
    membership = {}
    
    print(f"Total boxes: {len(boxes)}")
    print(f"\nProcessing {limit} connections:\n")
    
    for distance in distances:
        if counter == limit:
            break
        
        i, j = distance[1], distance[2]
        
        print(f"Connection {counter + 1}: boxes {i} and {j} (distance: {distance[0]:.2f})")
        
        if i in membership and j in membership:
            # Both are in groups
            if membership[i] != membership[j]:
                # Merge different groups
                group_i = membership[i]
                group_j = membership[j]
                
                print(f"  Merging group {group_j} into group {group_i}")
                
                # Merge group_j into group_i
                for member in groups[group_j]:
                    membership[member] = group_i
                    groups[group_i].append(member)
                
                # Clear the old group
                groups[group_j] = []
            else:
                print(f"  Already in same group (group {membership[i]})")
            counter += 1
            
        elif i in membership:
            print(f"  Adding box {j} to group {membership[i]}")
            membership[j] = membership[i]
            groups[membership[i]].append(j)
            counter += 1
            
        elif j in membership:
            print(f"  Adding box {i} to group {membership[j]}")
            membership[i] = membership[j]
            groups[membership[j]].append(i)
            counter += 1
            
        else:
            print(f"  Creating new group {len(groups)}")
            membership[i] = len(groups)
            membership[j] = len(groups)
            groups.append([i, j])
            counter += 1
    
    print(f"\n--- After {limit} connections ---")
    
    # Get sizes of non-empty groups
    group_sizes = sorted([len(g) for g in groups if len(g) > 0], reverse=True)
    
    # Count nodes NOT in any group yet (isolated circuits)
    nodes_in_groups = sum(group_sizes)
    isolated_circuits = len(boxes) - nodes_in_groups
    total_circuits = len(group_sizes) + isolated_circuits
    
    print(f"Non-empty groups: {len(group_sizes)}")
    print(f"Group sizes: {group_sizes}")
    print(f"Nodes in groups: {nodes_in_groups}")
    print(f"Isolated circuits (single boxes): {isolated_circuits}")
    print(f"Total circuits: {total_circuits}")
    print(f"\nTop 3 largest circuit sizes: {group_sizes[:3]}")
    
    # Multiply three largest
    result = group_sizes[0] * group_sizes[1] * group_sizes[2]
    
    return result

def part2(boxes, distances):
    num_of_groups = len(boxes)
    groups = []
    membership = {}
    
    print(f"Total boxes: {len(boxes)}")
    
    for distance in distances:
        if num_of_groups == 1:
            break
        
        i, j = distance[1], distance[2]
        last_box1 = []
        last_box2 = []
        
        if i in membership and j in membership:
            # Both are in groups
            if membership[i] != membership[j]:
                last_box1 = boxes[i]
                last_box2 = boxes[j]
                # Merge different groups
                group_i = membership[i]
                group_j = membership[j]
                
                print(f"  Merging group {group_j} into group {group_i}")
                
                # Merge group_j into group_i
                for member in groups[group_j]:
                    membership[member] = group_i
                    groups[group_i].append(member)
                
                # Clear the old group
                groups[group_j] = []
                num_of_groups -= 1
            else:
                print(f"  Already in same group (group {membership[i]})")
            
        elif i in membership:
            last_box1 = boxes[i]
            last_box2 = boxes[j]
            print(f"  Adding box {j} to group {membership[i]}")
            membership[j] = membership[i]
            groups[membership[i]].append(j)
            num_of_groups -= 1
            
        elif j in membership:
            last_box1 = boxes[i]
            last_box2 = boxes[j]
            print(f"  Adding box {i} to group {membership[j]}")
            membership[i] = membership[j]
            groups[membership[j]].append(i)
            num_of_groups -= 1
            
        else:
            last_box1 = boxes[i]
            last_box2 = boxes[j]
            print(f"  Creating new group {len(groups)}")
            membership[i] = len(groups)
            membership[j] = len(groups)
            groups.append([i, j])
            num_of_groups -= 1
    print(last_box1, last_box2)
    return last_box1[0]*last_box2[0]


def read_file(filename):
    boxes = []
    with open(filename) as file:
        for line in file.readlines():
            boxes.append([int(num) for num in line.strip().split(",")])
    
    # Store all distances in flat list
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append([calculate_distance(boxes[i], boxes[j]), i, j])
    
    distances.sort(key=lambda x: x[0])
    
    return boxes, distances


def calculate_distance(box1, box2):
    distance = (box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2
    return distance


boxes, distances = read_file("data.txt")
print(f"Part1 answer: {part1(boxes, distances, 1000)}")
print(f"Part2 answer: {part2(boxes, distances)}")