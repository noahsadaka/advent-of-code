from aoc_utils import *

def count_increases(data):
    count = 0
    ind = 1
    while ind < len(data):
        if int(data[ind-1]) < int(data[ind]):
            count +=1
        ind+=1
    return count

def count_increases_window(data):
    count = 0
    ind = 0
    data_num = []
    for line in data:
        data_num.append(float(line))
    while ind < len(data)-3:
        if sum(data_num[ind:ind+3])<sum(data_num[ind+1:ind+4]):
            count +=1
        ind+=1
    return count

data = import_data('input')

print(count_increases(data))
print(count_increases_window(data))
