file= open('input', 'r') 

def game_determiner(time, distance):
    counter = 0
    for speed in range(1, time):
        move_time = time - speed
        distance_travelled = move_time * speed
        if distance_travelled > distance:
            counter +=1
    return counter

data = file.readlines()
line1 = data[0]
line2 = data[1]

times = line1.split('\n')[0]
times = times.split(':')[1]
times = times.split()
time  = ''
for t in times:
    time = time + t
time = int(time)

distances = line2.split('\n')[0]
distances = distances.split(':')[1]
distances = distances.split()
dist = ''
for d in distances:
    dist = dist + d
distances = int(dist)

output = game_determiner(time, distances)
print(output)


