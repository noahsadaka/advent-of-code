from copy import deepcopy
import math
file = open('input', 'r')
data = file.readlines()
character_line = data[0].split('\n')[0]
characters = character_line.split(',')
print(characters)

summation = 0

for item in characters:
    current_sum = 0
    for ch in item:
        ascii_val = ord(ch)
        current_sum += ascii_val
        current_sum *= 17
        current_sum = current_sum % 256
    summation += current_sum
print(summation)

