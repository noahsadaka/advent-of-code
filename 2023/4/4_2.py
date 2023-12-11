file= open('input', 'r') 

def check_win(index, winning_numbers, card_numbers):
    # Recursive function
    current_count = 0
    count = 1
    for wn in winning_numbers[index]:
        for cn in card_numbers[index]:
            if wn == cn:
                current_count += 1
                temp_count = check_win(index+current_count, winning_numbers, card_numbers)
                count += temp_count
    return count

data = file.readlines()
card_numbers = []

# parse and store
winning_numbers = []
card_numbers = []
for line in data:
    cur_line = line.split('\n')[0]
    numbers = cur_line.split(':')[1]
    winning_numb = numbers.split('|')[0]
    winning_numb = winning_numb.split()
    my_numb = numbers.split('|')[1]
    my_numb = my_numb.split()
    card_numbers.append(my_numb)
    winning_numbers.append(winning_numb)
summation = 0
for i in range(len(card_numbers)):
    print(i)
    temp = check_win(i, winning_numbers, card_numbers)
    summation += temp
print(summation)

