file= open('input', 'r') 

data = file.readlines()
summation = 0
red = 12
green = 13
blue = 14
lines = []
for line in data:
    cur_line = line.split('\n')[0]
    lines.append(cur_line)

for line_ind, line_val in enumerate(lines):
    # get the indices of all the blocks of numbers

print(summation)


