file= open('input.in', 'r') 
data = file.readlines()

points = 0
#a=rock=1
#b=paper=2
#c=scissors=3
for line in data:
    split_line = line.split()
    move_1=split_line[0]
    move_2=split_line[1]
    if move_2 == 'X':
        if move_1 == 'A':
            points += 3
        elif move_1 == 'B':
            points += 1
        else:
            points += 2
    elif move_2 == 'Y':
        points +=3
        if move_1 == 'B':
            points += 2
        elif move_1 == 'C':
            points += 3
        else:
            points += 1
    elif move_2 == 'Z':
        points +=6
        if move_1 == 'C':
            points += 1
        elif move_1 == 'A':
            points += 2
        else:
            points += 3

print(points)







