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
    while num1 == 0:
        numbercount = 0
        for numb in numbers:
            numbercount += 1
            len_numb = len(numb)
            if cur_line[0:len_numb] == numb:
                num1 = numbercount
            elif numb == numbers[-1]:
                cur_line = cur_line[1:]
    print(cur_line)
    while num2 == 0:
        numbercount = 0
        for numb in numbers:
            numbercount += 1
            len_numb = len(numb)
            len_cur_line = len(cur_line)
            if cur_line[len_cur_line-len_numb:] == numb:
                num1 = numbercount
            elif numb == numbers[-1]:
                cur_line = cur_line[0:-2]
                print(cur_line)
    print(num1)
    print(num2)
    input()



print(summation)

