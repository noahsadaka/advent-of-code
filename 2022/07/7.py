from aoc_utils import *

data = import_data('input')

def get_total_sum(d):
    total_sum = 0
    if 'totalfiles' in d.keys():
        total_sum = d['totalfiles']
    for k,v in d.items():
        if isinstance(v, dict):
            t, _ = get_total_sum(v)
            total_sum += t
    if 'totalfiles' in d.keys():
        d['totalfiles']=total_sum
    return total_sum, d

def count_dirs(d):
    counter = 0
    for k,v in d.items():
        if k == 'totalfiles':
            if v <= 100000:
                counter+=v
        elif isinstance(v, dict):
            counter += count_dirs(v)
    return counter

def add_dir(d,dir_list):
    for key in dir_list[:-1]:
        d = d.setdefault(key, {})
    d[dir_list[-1]] = {'sumfiles':0, 'totalfiles':0}


def add_file_size(d, dir_list, value):
    for key in dir_list[:-1]:
        d = d.setdefault(key, {})
    d[dir_list[-1]]['sumfiles'] += value
    d[dir_list[-1]]['totalfiles'] += value

def delete_smallest(d, min_size, current_value):
    for k,v in d.items():
        if k=='totalfiles':
            if v < current_value and v > min_size:
                current_value = v
        elif isinstance(v, dict):
            current_value = delete_smallest(v, min_size, current_value)
    return current_value



def parse_tree(data=data):
    tree = dict([('/', {'sumfiles':0, 'totalfiles':0})])
    line_ind = 1
    folder_depth = ['/']
    lsflag = False
    while line_ind < len(data):
        line = data[line_ind]
        splitted = line.split()
        if splitted[0] == '$':
            if splitted[1] == 'cd':
                lsflag = False
                if splitted[2] == '..':
                    folder_depth = folder_depth[0:-1]
                else:
                    folder_depth.append(splitted[2])
                    add_dir(tree, folder_depth)
            elif splitted[1] == 'ls':
                lsflag = True
        if lsflag and splitted[0] != 'dir' and splitted[0] != '$':
            filesize=int(splitted[0])
            add_file_size(tree, folder_depth, filesize)
        line_ind +=1
    return tree

tree = parse_tree()
_,tree = get_total_sum(tree)
print(f'part 1 answer: {count_dirs(tree)}')

min_delete = 30000000-(70000000-tree['/']['totalfiles'])
print(f'part 2 answer: {delete_smallest(tree, min_delete, 1e20)}')


