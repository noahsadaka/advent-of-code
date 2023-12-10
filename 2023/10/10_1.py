from copy import deepcopy
import numpy as np
import math
file = open('input.txt', 'r')
data = file.readlines()


def get_next_coord(current_coord, last_coord, character):
    option_1 = deepcopy(current_coord)
    option_2 = deepcopy(current_coord)
    if character == '|':
        option_1[0] += 1
        option_2[0] -= 1
    elif character == '-':
        option_1[1] += 1
        option_2[1] -= 1
    elif character == 'L':
        option_1[1] += 1
        option_2[0] -= 1
    elif character == 'J':
        option_1[1] -= 1
        option_2[0] -= 1
    elif character == '7':
        option_1[0] += 1
        option_2[1] -= 1
    elif character == 'F':
       option_1[1] += 1
       option_2[0] += 1
    elif character == 'S':
        return False
    else:
        print('something went wrong')
        print(current_coord)
        return False
    if last_coord == option_1:
        return option_2
    else:
        return option_1

full_map = []

# Parse the info
for line in data:
    full_map.append(line.split('\n')[0])

# Find the starting point
for i_l, line in enumerate(full_map):
    for ic, character in enumerate(line):
        if character == 'S':
            coords_S = [i_l, ic]

last_coord = deepcopy(coords_S)
current_coord = deepcopy(coords_S)
step = 0
current_coord[0] -= 1
checker = True
coordlist = [current_coord]
while checker:
    step += 1
    pipeline = full_map[current_coord[0]]
    pipechar = pipeline[current_coord[1]]
    current_coord_temp = get_next_coord(current_coord, last_coord, pipechar)
    if not current_coord_temp:
        checker = False
    last_coord = current_coord
    current_coord = current_coord_temp
    coordlist.append(current_coord)
print(step/2)
