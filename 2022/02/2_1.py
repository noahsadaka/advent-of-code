file= open('input.in', 'r') 
data = file.readlines()

points = 0

for line in data:
    split_line = line.split()
    move_1=split_line[0]
    move_2=split_line[1]
    if move_2 == 'X':
        points +=1
        if move_1 == 'A':
            points += 3
        elif move_1 == 'B':
            points += 0
        else:
            points += 6
    elif move_2 == 'Y':
        points +=2
        if move_1 == 'B':
            points += 3
        elif move_1 == 'C':
            points += 0
        else:
            points += 6
    elif move_2 == 'Z':
        points +=3
        if move_1 == 'C':
            points += 3
        elif move_1 == 'A':
            points += 0
        else:
            points += 6

print(points)







