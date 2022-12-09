from aoc_utils import *
import numpy as np

data = import_data('example')

def move(data=data):
    tailcoordlist = [[0,0]]
    headcoordlist = [[0,0]]
    counter = 1

    for line in data:
        line = line.split()
        direction = line[0]
        steps = int(line[1])
        for step in range(steps):
            if direction == 'R':
                cur_head_coord = headcoordlist[-1].copy()
                cur_head_coord[1]+=1
                headcoordlist.append(cur_head_coord)
            elif direction == 'L':
                cur_head_coord = headcoordlist[-1].copy()
                cur_head_coord[1]-=1
                headcoordlist.append(cur_head_coord)
            elif direction == 'U':
                cur_head_coord = headcoordlist[-1].copy()
                cur_head_coord[0]+=1
                headcoordlist.append(cur_head_coord)
            elif direction == 'D':
                cur_head_coord = headcoordlist[-1].copy()
                cur_head_coord[0]-=1
                headcoordlist.append(cur_head_coord)
            new_tailcoord = move_tail(headcoordlist[-1].copy(), tailcoordlist[-1].copy())
            if new_tailcoord not in tailcoordlist:
                counter+=1
            tailcoordlist.append(new_tailcoord)
    return counter

def move_tail(headcoord, tailcoord):
    headcoord = np.array(headcoord)
    tailcoord = np.array(tailcoord)
    if (headcoord[0]==tailcoord[0] or headcoord[1]==tailcoord[1]) and (abs(headcoord[0]-tailcoord[0])>1 or abs(headcoord[1]-tailcoord[1])>1): # if same row or column
        if headcoord[0]>tailcoord[0]: # same col
            tailcoord[0]+=1
        elif headcoord[0] < tailcoord[0]:
            tailcoord[0]-=1
        elif headcoord[1]>tailcoord[1]: # same row
            tailcoord[1]+=1
        elif headcoord[1] < tailcoord[1]:
            tailcoord[1]-=1
    elif (abs(headcoord[0]-tailcoord[0]) + abs(headcoord[1]-tailcoord[1]))>2: # diagonally by >1 
        if headcoord[0]>tailcoord[0] and headcoord[1]>tailcoord[1]:
            tailcoord[0]+=1
            tailcoord[1]+=1
        elif headcoord[0]>tailcoord[0] and headcoord[1]<tailcoord[1]:
            tailcoord[0]+=1
            tailcoord[1]-=1
        elif headcoord[0]<tailcoord[0] and headcoord[1]>tailcoord[1]:
            tailcoord[0]-=1
            tailcoord[1]+=1
        elif headcoord[0]<tailcoord[0] and headcoord[1]<tailcoord[1]:
            tailcoord[0]-=1
            tailcoord[1]-=1
    return tailcoord.tolist()

print(move())
