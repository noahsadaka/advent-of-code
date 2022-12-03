def calc_priority(letter):
    if letter == '-':
        value = 0
    elif letter.isupper():
        value = ord(letter)-64+26
    else:
        value = ord(letter)-96
    print(f'{letter}-{value}')
    return value


file= open('input.in', 'r') 
data = file.readlines()

p = 0
ind = 3
while ind-1 < len(data):
    lines = data[ind-3:ind]
    threelines = []
    for line in lines:
        line = line.split('\n')[0]
        threelines.append(line)
    matches = []
    for i in threelines[0]:
        for j in threelines[1]:
            if i == j:
                matches.append(i)
    for i in matches:
        if i in threelines[2]:
            p+= calc_priority(i)
            break
    ind +=3
print(p)
                
