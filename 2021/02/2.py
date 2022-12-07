from aoc_utils import *

data = import_data('input')

def mult_positions(data=data):
    h=0
    d=0
    for line in data:
        splitted = line.split()
        if splitted[0] == 'forward':
            h+=int(splitted[1])
        elif splitted[0] == 'down':
            d += int(splitted[1])
        elif splitted[0] == 'up':
            d -= int(splitted[1])
    return d*h

def aims(data=data):
    h=0
    d=0
    aim=0
    for line in data:
        splitted = line.split()
        if splitted[0] == 'forward':
            h+=int(splitted[1])
            d+=aim*int(splitted[1])
        elif splitted[0] == 'down':
            aim += int(splitted[1])
        elif splitted[0] == 'up':
            aim -= int(splitted[1])
    return d*h

print(mult_positions())
print(aims())



