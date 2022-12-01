import numpy as np
calorie_list = []

file= open('input.in', 'r') 

data = file.readlines()
calorie_list = []
calorie_counter=0
for line in data:
    cur_line=line.split('\n')[0]
    if len(cur_line) != 0:
        calorie_counter += int(cur_line)
    else:
        calorie_list.append(calorie_counter)
        calorie_counter = 0
print(np.argmax(calorie_list)+1)
print(max(calorie_list))


sum_top_3=0

for i in range(3):
    sum_top_3 += max(calorie_list)
    max_ind = np.argmax(calorie_list)
    calorie_list[max_ind]=0
print(sum_top_3)

