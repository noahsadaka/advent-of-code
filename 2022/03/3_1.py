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

for line in data:
    line = line.split('\n')[0]
    print(line)
    length = int(len(line)/2)
    c_1 = line[0:length]
    c_2 = line[length:]
    letter_list = []
    for i in c_1:
        for j in c_2:
            if i == j:
                if i not in letter_list:
                    letter = i
                    p += calc_priority(letter)
                    letter_list.append(letter)
print(p)
                
