file= open('input', 'r') 


def gear_analysis(all_lines, gear_line_ind, gear_digit_ind):
    numbers = []
    current_line = all_lines[gear_line_ind]
    if gear_line_ind > 0:
        previous_line = all_lines[gear_line_ind-1]
    else:
        previous_line = False
    if gear_line_ind < len(all_lines) - 1:
        next_line = all_lines[gear_line_ind + 1]
    else:
        next_line = False

    # check to the left
    if gear_digit_ind > 0:
        if current_line[gear_digit_ind - 1].isdigit():
            num = build_number(current_line, gear_digit_ind - 1)
            numbers.append(num)
    # check to the right
    if gear_digit_ind < len(current_line) - 1:
        if current_line[gear_digit_ind + 1].isdigit():
            num = build_number(current_line, gear_digit_ind + 1)
            numbers.append(num)
    # Check above
    if previous_line is not False:
        # check directly above, if no num, check to left and right
        if previous_line[gear_digit_ind].isdigit():
            num = build_number(previous_line, gear_digit_ind)
            numbers.append(num)
        else:
            if gear_digit_ind > 0 and previous_line[gear_digit_ind - 1].isdigit():
                num = build_number(previous_line, gear_digit_ind-1)
                numbers.append(num)
            if gear_digit_ind < len(current_line) - 1 and previous_line[gear_digit_ind + 1].isdigit():
                num = build_number(previous_line, gear_digit_ind+1)
                numbers.append(num)
    # Check below
    if next_line is not False:
        # check directly above, if no num, check to left and right
        if next_line[gear_digit_ind].isdigit():
            num = build_number(next_line, gear_digit_ind)
            numbers.append(num)
        else:
            if gear_digit_ind > 0 and next_line[gear_digit_ind - 1].isdigit():
                num = build_number(next_line, gear_digit_ind-1)
                numbers.append(num)
            if gear_digit_ind < len(current_line) - 1 and next_line[gear_digit_ind + 1].isdigit():
                num = build_number(next_line, gear_digit_ind+1)
                numbers.append(num)
    if len(numbers) > 1:
        if len(numbers) > 2:
            print('oops')
        else:
            return numbers[0] * numbers[1]
    else: 
        return 0


def build_number(line, digit_ind):
    number = ''
    # Start moving towards the right
    if line[digit_ind].isdigit():
        number += line[digit_ind]
        flag = True
        temp_ind = digit_ind + 1
        while flag and temp_ind < len(line):
            if line[temp_ind].isdigit():
                number += line[temp_ind]
            else:
                flag = False
            temp_ind += 1
        temp_ind = digit_ind - 1
        flag = True
        while flag and temp_ind >= 0:
            if line[temp_ind].isdigit():
                number = line[temp_ind] + number
            else:
                flag = False
            temp_ind -= 1
        return int(number)
    else:
        print('something is very wrong')



# Open data, parse, and generate list of lines
data = file.readlines()
lines = []
for line in data:
    cur_line = line.split('\n')[0]
    lines.append(cur_line)

# iterate through lines to find parts
line_indices = []
digit_indices = []
for line_ind, line in enumerate(lines):
    for digit_ind, digit in enumerate(line):
        if digit == '*':
            line_indices.append(line_ind)
            digit_indices.append(digit_ind)

summation = 0
for i in range(len(line_indices)):
    value = gear_analysis(lines, line_indices[i], digit_indices[i])
    summation += value
print(summation)





