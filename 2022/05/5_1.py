file= open('input.in', 'r') 
data = file.readlines()
data_2 = []
ind = 0
bin_line = 0
for line in data:
    if line == '\n':
        bin_line = ind
    ind+=1
    splitted_line = line.split('\n')[0]
    data_2.append(splitted_line)
data = data_2
stack_num = int(data[bin_line-1].strip().split(' ')[-1])
bins = dict()
for i in data[bin_line-1].split():
    bins[i]=[]
for line in data[:bin_line-1]:
    for i in data[bin_line-1].split():
        letter = line[4*(int(i)-1):4*int(i)].strip('[] ')
        if letter != '':
            bins[i].append(letter)
for instruction in data[bin_line+1:]:
    split_inst = instruction.split()
    num_move = int(split_inst[1])
    from_bin = split_inst[3]
    to_bin = split_inst[-1]

    for i in range(num_move):
        moved_crate = bins[from_bin][0]
        bins[from_bin] = bins[from_bin][1:]
        to_bin_list = bins[to_bin]
        to_bin_list.insert(0, moved_crate)
        bins[to_bin] = to_bin_list
out_string=''
for i in data[bin_line-1].split():
    out_string += bins[i][0]
print(out_string)

