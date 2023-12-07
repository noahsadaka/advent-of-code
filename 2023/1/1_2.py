import numpy as np

file= open('input', 'r') 

data = file.readlines()
letters='abcdefghijklmnopqrstuvwxyz'
numbers = ['one','two','three','four','five','six','seven','eight','nine']
summation = 0
for line in data:
    cur_line=line.split('\n')[0]
    num1 = 0
    num2 = 0
    for i in range(len(line)):
        try int(letter[i]):
            num1 = int(letter[i])
        except:
            for number in numbers:


print(summation)

