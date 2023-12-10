file= open('input', 'r') 

data = file.readlines()
hands = []
bids = []

for line in data:
    cur_line = line.split('\n')[0]
    hand = cur_line.split()[0]
    hands.append(hand)
    bid = cur_line.split()[1]
    bids.append(int(bid))

print(hands)
print(bids)
