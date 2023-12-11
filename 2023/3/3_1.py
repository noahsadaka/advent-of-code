file= open('input', 'r') 


def check_if_part(all_lines, line_index, digit_indices):
    len_lines = len(all_lines)
    current_line = all_lines[line_index]
    len_c = len(current_line)
    if line_index != 0 and line_index != len_lines-1:
        previous_line = all_lines[line_index-1]
        next_line = all_lines[line_index+1]
        diagonal_left = digit_indices[0]-1
        if diagonal_left < 0:
            diagonal_left = 0
        diagonal_right = digit_indices[-1]+1
        if diagonal_right >= len_c:
            diagonal_right = len_c - 1
        if digit_indices[0]-1 >= 0 and current_line[digit_indices[0]-1] != '.':
            return True
        elif digit_indices[-1]+1 < len_c and current_line[digit_indices[-1]+1] != '.':
            return True
        else:
            up_slice = previous_line[diagonal_left : diagonal_right+1]
            down_slice = next_line[diagonal_left : diagonal_right+1]
            for l in up_slice:
                if l != '.':
                    return True
            for l in down_slice:
                if l != '.':
                    return True
    elif line_index != 0:
        previous_line = all_lines[line_index-1]
        diagonal_left = digit_indices[0]-1
        if diagonal_left < 0:
            diagonal_left = 0
        diagonal_right = digit_indices[-1]+1
        if diagonal_right >= len(current_line):
            diagonal_right = len(current_line) - 1
        if digit_indices[0]-1 >= 0 and current_line[digit_indices[0]-1] != '.':
            return True
        elif digit_indices[-1]+1 < len_c and current_line[digit_indices[-1]+1] != '.':
            return True
        else:
            up_slice = previous_line[diagonal_left : diagonal_right+1]
            for l in up_slice:
                if l != '.':
                    return True
    else:
        next_line = all_lines[line_index+1]
        diagonal_left = digit_indices[0]-1
        if diagonal_left < 0:
            diagonal_left = 0
        diagonal_right = digit_indices[-1]+1
        if diagonal_right >= len(current_line):
            diagonal_right = len(current_line) - 1
        if digit_indices[0]-1 >= 0 and current_line[digit_indices[0]-1] != '.':
            return True
        elif digit_indices[-1]+1 < len_c and current_line[digit_indices[-1]+1] != '.':
            return True
        else:
            down_slice = next_line[diagonal_left : diagonal_right+1]
            for l in down_slice:
                if l != '.':
                    return True
    return False

# Open data, parse, and generate list of lines
data = file.readlines()
lines = []
for line in data:
    cur_line = line.split('\n')[0]
    lines.append(cur_line)

# iterate through lines to find parts
line_ind = 0
summation = 0
while line_ind < len(lines):
    digit_ind = 0
    current_line = lines[line_ind]
    while digit_ind < len(current_line):
        current_number_indices = []
        # Get a block of indices corresponding to a number
        if current_line[digit_ind].isdigit():
            current_number_indices.append(digit_ind)
            flag = True
            while flag:
                if digit_ind < len(current_line)-1:
                    digit_ind += 1
                    if current_line[digit_ind].isdigit():
                        current_number_indices.append(digit_ind)
                    else:
                        flag = False
                else:
                    digit_ind += 1
                    flag = False
        else:
            digit_ind += 1
        if len(current_number_indices)>0 and check_if_part(lines, line_ind, current_number_indices):
            summation += int(current_line[current_number_indices[0]:current_number_indices[-1]+1])
    line_ind +=1
        #print(current_number_indices)
        #input()

print(summation)


