import numpy as np

file= open('input', 'r') 

data = file.readlines()
letters='abcdefghijklmnopqrstuvwxyz'
summation = 0
for line in data:
    cur_line=line.split('\n')[0]
    cur_line = cur_line.strip(letters)
    num1 = cur_line[0]
    num2 = cur_line[-1]
    summation += int(num1 + num2)

print(summation)

