file= open('input', 'r') 

data = file.readlines()
summation = 0
for line in data:
    cur_line = line.split('\n')[0]
    games_str = cur_line.split(':')[1]
    games = games_str.split(';')
    flag = True
    red_count = 0
    blue_count = 0
    green_count = 0
    for game in games:
        stuff = game.split()
        for i in range(len(stuff)):
            stuff[i] = stuff[i].strip(',')
        for step in range(int(len(stuff)/2)):
            if stuff[2*step+1] == 'blue':
                if int(stuff[2*step]) > blue_count:
                    blue_count = int(stuff[2*step])
            elif stuff[2*step+1] == 'red':
                if int(stuff[2*step]) > red_count:
                    red_count = int(stuff[2*step])
            elif stuff[2*step+1] == 'green':
                if int(stuff[2*step]) > green_count:
                    green_count = int(stuff[2*step])
    summation += green_count * red_count * blue_count
print(summation)

