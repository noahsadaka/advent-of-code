file= open('input', 'r') 

data = file.readlines()
summation = 0
red = 12
green = 13
blue = 14
for line in data:
    cur_line = line.split('\n')[0]
    game_id = cur_line.split(':')[0]
    game_id = int(game_id.strip('Game'))
    games_str = cur_line.split(':')[1]
    games = games_str.split(';')
    flag = True
    for game in games:
        stuff = game.split()
        for i in range(len(stuff)):
            stuff[i] = stuff[i].strip(',')
        for step in range(int(len(stuff)/2)):
            if stuff[2*step+1] == 'blue':
                if int(stuff[2*step]) > blue:
                    flag = False
            elif stuff[2*step+1] == 'red':
                if int(stuff[2*step]) > red:
                    flag = False
            elif stuff[2*step+1] == 'green':
                if int(stuff[2*step]) > green:
                    flag = False
    if flag:
        summation += game_id
print(summation)

