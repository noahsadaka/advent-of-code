from aoc_utils import *

data = import_data('input')

def get_additions(data=data):
    additions = []
    for line in data:
        split = line.split()
        if split[0] == 'noop':
            additions.append(0)
        else:
            additions.append(0)
            additions.append(int(split[1]))
    return additions

def noop_noop(data=data):
    X=1
    summation=0
    counter=1
    additions = get_additions(data)
    for i in additions:
        X+=i
        counter +=1 
        if counter in [20,60,100,140,180,220]:
            summation += counter*X
        i+=1
    return summation

def draw(data=data):
    row = ''
    X=1
    summation=0
    counter=0
    additions = get_additions(data)
    for i in additions:
        if X in range(counter-1, counter+2):
            row += '██'
        else:
            row += '  '
        X+=i
        counter +=1 
        if counter == 40:
            counter -=40
            print(row)
            row = ''
        i+=1
    return summation

print(f'part 1 answer is {noop_noop()}')
draw()



