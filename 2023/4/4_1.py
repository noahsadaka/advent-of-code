file= open('input', 'r') 

data = file.readlines()
summation = 0
for line in data:
    cur_line = line.split('\n')[0]
    numbers = cur_line.split(':')[1]
    winning_numb = numbers.split('|')[0]
    winning_numb = winning_numb.split()
    my_numb = numbers.split('|')[1]
    my_numb = my_numb.split()
    points=0
    for wn in winning_numb:
        for mn in my_numb:
            if int(wn) == int(mn):
                if points==0:
                    points=1
                else:
                    points *= 2
    summation += points
print(summation)

