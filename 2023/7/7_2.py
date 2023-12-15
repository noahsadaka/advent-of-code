file= open('example', 'r') 

data = file.readlines()
def sort_function(card):
    if card == 'A':
        return 1
    elif card == 'K':
        return 2
    elif card == 'Q':
        return 3
    elif card == 'T':
        return 4
    elif card == '9':
        return 5
    elif card == '8':
        return 6
    elif card == '7':
        return 7
    elif card == '6':
        return 8
    elif card == '5':
        return 9
    elif card == '4':
        return 10
    elif card == '3':
        return 11
    elif card == '2':
        return 12
    elif card == '1':
        return 13
    elif card == 'J':
        return 14

def compare_two_cards(card1, card2):
    # return True if card 1 > card 2, False otherwise
    sorted_list = sorted([card1, card2], key=sort_function)
    if card1 == sorted_list[0]:
        return True
    else:
        return False

def sorter(cardlist):
    n = len(cardlist)
    for card_i, card_bid in enumerate(cardlist):
        card = card_bid.split()[0]
        for nextcard_i in range(n - card_i - 1):
            nextcard = cardlist[nextcard_i].split()[0]
            nextnextcard = cardlist[nextcard_i+1].split()[0]
            sort_flag = True
            cardval_i = 0
            while sort_flag:
                if nextcard[cardval_i] == nextnextcard[cardval_i]:
                    cardval_i += 1
                    if cardval_i == 5:
                        sort_flag = False
                else:
                    if not compare_two_cards(nextcard[cardval_i], nextnextcard[cardval_i]):
                        cardlist[nextcard_i], cardlist[nextcard_i+1] = cardlist[nextcard_i+1], cardlist[nextcard_i]
                        sort_flag = False
                    else:
                        sort_flag = False
    return cardlist

def scoring(rank, summation, cardbidlist):
    if len(cardbidlist)>=1:
        for card_bid in cardbidlist[::-1]:
            bid = int(card_bid.split()[1])
            summation += rank * bid
            rank += 1
    return rank, summation, cardbidlist

def handsorter(card_bid):
    card = card_bid.split()[0]
    card = sorted(card)
    if 'J' not in card:
        if card[0] == card[1] == card[2] == card[3] == card[4]:
            return '5'
        elif card[0] == card[1] == card[2] == card[3] or card[1] == card[2] == card[3] == card[4]:
            return '4'
        elif card[0] == card[1] == card[2]:
            if card[3] == card[4]:
                return 'fh'
            else:
                return 'th'
        elif card[2] == card[3] == card[4]:
            if card[0] == card[1]:
                return 'fh'
            else:
                return 'th'
        elif card[1] == card[2] == card[3]:
            if card[0] == card[4]:
                return 'fh'
            else:
                return 'th'
        elif card[0] != card[1] != card[2] != card[3] != card[4]:
            return 'hc'
        elif len(set(card)) == 4:
            return '1'
        else:
            return '2'
    else:
        # five of a kind
        if len(set(card)) == 2:
            return '5'
        # one pair
        elif len(set(card)) == 4:
            return '1'
        #  

# Data storage for each type of hand
fi_oak = [] # done
fo_oak = [] # done
fh = [] # done
th_oak = [] # done
two_p = [] # done
one_p = [] # done
high_c = [] # done

# Parse
for line in data:
    cur_line = line.split('\n')[0]
    card = sorted(cur_line.split()[0])
    # Five of a kind
    if len(set(card)) == 1 or (len(set(card)) == 2 and 'J' in card):
        fi_oak.append(cur_line)
    # four of a kind
    elif card[0] == card[1] == card[2] == card[3]:
        fo_oak.append(cur_line)
    elif card[1] == card[2] == card[3] == card[4]:
        fo_oak.append(cur_line)
    elif card[0] == card[1] == card[2]:
        if card[3] == card[4]:
            fh.append(cur_line)
        else:
            th_oak.append(cur_line)
    elif card[2] == card[3] == card[4]:
        if card[0] == card[1]:
            fh.append(cur_line)
        else:
            th_oak.append(cur_line)
    elif card[1] == card[2] == card[3]:
        if card[0] == card[4]:
            fh.append(cur_line)
        else:
            th_oak.append(cur_line)
    elif card[0] != card[1] != card[2] != card[3] != card[4]:
        high_c.append(cur_line)
    elif len(set(card)) == 4:
        one_p.append(cur_line)
    else:
        two_p.append(cur_line)

fi_oak = sorter(fi_oak)
fo_oak = sorter(fo_oak)
fh = sorter(fh)
th_oak = sorter(th_oak)
two_p = sorter(two_p)
one_p = sorter(one_p)
high_c = sorter(high_c)

# Scoring
summation = 0
rank = 1
rank, summation, _ = scoring(rank, summation, high_c)
rank, summation, _ = scoring(rank, summation, one_p)
rank, summation, _ = scoring(rank, summation, two_p)
rank, summation, _ = scoring(rank, summation, th_oak)
rank, summation, _ = scoring(rank, summation, fh)
rank, summation, _ = scoring(rank, summation, fo_oak)
rank, summation, _ = scoring(rank, summation, fi_oak)
print(summation)
