from aoc_utils import *
from math import floor

data = import_data('input')

def get_starting_lists(data=data):
    starting_list = []
    for i, line in enumerate(data):
        if line!='' and line.split()[0] == 'Monkey':
            monkey_list= []
            values = data[i+1].split(':')[1].split(',')
            for value in values:
                monkey_list.append(int(value))
            starting_list.append(monkey_list)
    return starting_list

def update_value(value, operation):
    value = int(value)
    operation = operation.split()
    if operation[0] =='old' and operation[2] == 'old':
        if operation[1] == '*':
            value = value*value
    elif operation[1] == '*':
        value *= int(operation[2])
    elif operation[1] == '+':
        value += int(operation[2])
    else:
        print('something is wrong')
        print(operation)
    value = floor(value/3)
    return value

def simulate_rounds(data=data, n=20):
    item_list = get_starting_lists(data)
    num_inspects = [0]*len(item_list)

    for roundnum in range(n):
        for i, line in enumerate(data):
            if line!='' and line.split()[0] == 'Monkey':
                monkey_ind = int(line.split()[1].strip(':'))
                operation = data[i+2].split('=')[-1]
                for item_ind, item in enumerate(item_list[monkey_ind]):
                    num_inspects[monkey_ind]+=1
                    item_list[monkey_ind][item_ind] = update_value(item_list[monkey_ind][item_ind], operation)
                    test = int(data[i+3].split()[-1])
                    if item_list[monkey_ind][item_ind]%test==0:
                        item_list[int(data[i+4].split()[-1])].append(item_list[monkey_ind][item_ind])
                    else:
                        item_list[int(data[i+5].split()[-1])].append(item_list[monkey_ind][item_ind])
                item_list[monkey_ind] = []
    return num_inspects 

def part1_calc(num_inspects):
    value = max(num_inspects)
    num_inspects.remove(value)
    value *= max(num_inspects)
    return value


final_list = simulate_rounds()
print(part1_calc(final_list))



