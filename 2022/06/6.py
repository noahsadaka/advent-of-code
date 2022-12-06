def get_message(data, num):
    num_char=num
    for line in data:
        line = line.strip('\n')
        while num_char < len(line):
            substring = line[num_char-num:num_char]
            flag = False
            for i in substring:
                if len(substring.replace(i,''))<num-1:
                    flag = True
            if flag == False:
                break
            else:
                num_char +=1
    return num_char

file= open('input.in', 'r') 
data = file.readlines()

p1 = get_message(data, 4)
p2 = get_message(data, 14)

print(p1)
print(p2)



