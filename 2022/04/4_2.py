def get_vector(pair):
    splitted_pair = pair.split('-')
    return list(range(int(splitted_pair[0]), int(splitted_pair[1])+1))

file= open('input.in', 'r') 
data = file.readlines()

contained_pairs = 0

for line in data:
    line = line.split('\n')[0]
    pair = line.split(',')
    elf_1 = get_vector(pair[0])
    elf_2 = get_vector(pair[1])
    
    flag1 = False
    flag2 = False
    for i in elf_1:
        if i in elf_2:
            flag1 = True
    for i in elf_2:
        if i in elf_1:
            flag2 = True
    if flag1 or flag2:
        contained_pairs +=1
print(contained_pairs)
                
