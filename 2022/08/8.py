from aoc_utils import *
import numpy as np

data = import_data('input')

def parse_input(data=data):
    out = np.zeros(len(data[0]))
    for ind, line in enumerate(data):
        temp = np.zeros(len(line))
        for treeind, tree in enumerate(line):
            temp[treeind] = int(tree)
        out = np.vstack([out, temp])
    out = out[1:]
    return out

def count_large_trees(tree_array):
    tree_counter = 0
    tree_counter += len(tree_array[0,:])*2 # top and bottom edges
    tree_counter += len(tree_array[:,0])*2 - 4 #L and R edges, minus corners
    for i, row in enumerate(tree_array[1:-1, 1:-1]):
        for j, col in enumerate(row):
            th = tree_array[i+1, j+1]
            if th > max(tree_array[:i+1, j+1]) or th > max(tree_array[i+2:, j+1]) or th > max(tree_array[i+1, :j+1]) or th > max(tree_array[i+1, j+2:]):
                tree_counter+=1
    return tree_counter

def scenic_score_iterator(tree_value, tree_list):
    if len(tree_list) == 0:
        sc = 0
    else:
        sc=1
        for i,v in enumerate(tree_list):
            if v < tree_value:
                sc+=1
                if i == len(tree_list)-1:
                    sc-=1
            else:
                return sc
    return sc

def scenic_score_counter(tree_array, row_ind, col_ind):
    th = tree_array[row_ind, col_ind]
    sc = 1
    sc*= scenic_score_iterator(th, np.flip(tree_array[row_ind, :col_ind]))
    sc*= scenic_score_iterator(th, tree_array[row_ind, col_ind+1:])
    sc*= scenic_score_iterator(th, np.flip(tree_array[:row_ind, col_ind]))
    sc*= scenic_score_iterator(th, tree_array[row_ind+1:, col_ind])
    return sc

def scenic_score(tree_array):
    sc = 0
    for rowind, row in enumerate(tree_array):
        for colind, col in enumerate(row):
            sc_temp = scenic_score_counter(tree_array, rowind, colind)
            if sc_temp > sc:
                sc = sc_temp
    return sc

matrix = parse_input()
p1 = count_large_trees(matrix)
p2 = scenic_score(matrix)
print(f'part 1 answer is {p1}')
print(f'part 2 answer is {p2}')






