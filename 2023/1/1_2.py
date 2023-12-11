import numpy as np

file= open('input', 'r') 

def get_first_number(line):
    letters='abcdefghijklmnopqrstuvwxyz'
    numbers = ['one','two','three','four','five','six','seven','eight','nine']

    len_line = len(line)
    flag = True
    i = 0
    while i < len_line:
        try: 
            int(line[i])
            return line[i]
        except:
            for n_i, number in enumerate(numbers):
                len_numb = len(number)
                if line[i:i+len_numb] == number:
                    return str(n_i+1)
            i+=1

def get_second_number(line):
    letters='abcdefghijklmnopqrstuvwxyz'
    numbers = ['one','two','three','four','five','six','seven','eight','nine']

    len_line = len(line)
    flag = True
    i = len_line-1
    while i >= 0:
        try: 
            int(line[i])
            return line[i]
        except:
            for n_i, number in enumerate(numbers):
                len_numb = len(number)-1
                if line[i-len_numb:i+1] == number:
                    return str(n_i+1)
            i-=1


data = file.readlines()
summation = 0
for line in data:
    cur_line=line.split('\n')[0]
    num1 = get_first_number(cur_line)
    num2 = get_second_number(cur_line)
    value = num1 + num2
    summation += int(value)

print(summation)

