# Rope Bridge
from load_data import get_data
import numpy as np

def rope(data):
    instructions = data.split('\n')[:-1]
    t_locations = [[0,0]]
    h_location = [0,0]
    for line in instructions:
        for move in range(int(line.split()[-1])):
            # move Head around
            if line[0] == 'R':
                h_location[0] += 1
            if line[0] == 'L':
                h_location[0] -= 1
            if line[0] == 'U':
                h_location[1] += 1
            if line[0] == 'D':
                h_location[1] -= 1
            # update position of Tail depending on Head
            distance = np.array(h_location) - np.array(t_locations[-1])
            # move right
            new_t_location = t_locations[-1].copy()
            if list(distance) == [2, 0]:
                new_t_location[0] += 1
                t_locations.append(new_t_location)
            # move left
            if list(distance) == [-2, 0]:
                new_t_location[0] -= 1
                t_locations.append(new_t_location)
            # move up
            if list(distance) == [0, 2]:
                new_t_location[1] += 1
                t_locations.append(new_t_location)
            # move down
            if list(distance) == [0, -2]:
                new_t_location[1] -= 1
                t_locations.append(new_t_location)
            # move up-right
            if list(distance) in [[1, 2], [2,1]] :
                new_t_location[0] += 1
                new_t_location[1] += 1
                t_locations.append(new_t_location)
            # move up-left
            if list(distance) in [[-1, 2], [-2,1]] :
                new_t_location[0] -= 1
                new_t_location[1] += 1
                t_locations.append(new_t_location)
            # move down-right
            if list(distance) in [[1, -2], [2,-1]] :
                new_t_location[0] += 1
                new_t_location[1] -= 1
                t_locations.append(new_t_location)
            # move down-left
            if list(distance) in [[-1, -2], [-2,-1]] :
                new_t_location[0] -= 1
                new_t_location[1] -= 1
                t_locations.append(new_t_location)
    t_locations_tups = [tuple(x) for x in t_locations]
    return len(set(t_locations_tups))

def rope_2(data):
    instructions = data.split('\n')[:-1]
    t_locations = [[0,0]]
    h_location = [0,0]
    for line in instructions:
        print(line)
        for move in range(int(line.split()[-1])):
            # move Head around
            if line[0] == 'R':
                h_location[0] += 1
            if line[0] == 'L':
                h_location[0] -= 1
            if line[0] == 'U':
                h_location[1] += 1
            if line[0] == 'D':
                h_location[1] -= 1
            print(f'h:{h_location}')
            # update position of Tail depending on Head
            distance = np.array(h_location) - np.array(t_locations[-1])
            # move right
            new_t_location = t_locations[-1].copy()
            if list(distance) == [2, 0]:
                new_t_location[0] += 1
                t_locations.append(new_t_location)
            # move left
            if list(distance) == [-2, 0]:
                new_t_location[0] -= 1
                t_locations.append(new_t_location)
            # move up
            if list(distance) == [0, 2]:
                new_t_location[1] += 1
                t_locations.append(new_t_location)
            # move down
            if list(distance) == [0, -2]:
                new_t_location[1] -= 1
                t_locations.append(new_t_location)
            # move up-right
            if list(distance) in [[1, 2], [2,1]] :
                new_t_location[0] += 1
                new_t_location[1] += 1
                t_locations.append(new_t_location)
            # move up-left
            if list(distance) in [[-1, 2], [-2,1]] :
                new_t_location[0] -= 1
                new_t_location[1] += 1
                t_locations.append(new_t_location)
            # move down-right
            if list(distance) in [[1, -2], [2,-1]] :
                new_t_location[0] += 1
                new_t_location[1] -= 1
                t_locations.append(new_t_location)
            # move down-left
            if list(distance) in [[-1, -2], [-2,-1]] :
                new_t_location[0] -= 1
                new_t_location[1] -= 1
                t_locations.append(new_t_location)
            print(f't: {new_t_location}')
    t_locations_tups = [tuple(x) for x in t_locations]
    return len(set(t_locations_tups))

with open("test_data/test09.txt") as file:
     test_data = file.read()
     print(rope(test_data))

# raw_data = get_data(9)

# print(f'part 1 solution = {rope(raw_data)}')

# with open("test_data/test09.txt") as file:
#     test_data = file.read()
#     print(rope_2(test_data))

# print(f'part 2 solution = {rope_2(raw_data)}')
