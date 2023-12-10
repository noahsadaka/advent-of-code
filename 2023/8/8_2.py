file= open('input', 'r') 


def find_index(string, dictionary):
    index = dictionary[string]
    return index

data = file.readlines()

instructions = data[0].split('\n')[0]
instruction_counter = 0

step_count = 0

locations = []
lefts = []
rights = []

# Parse the info
for i in range(len(data)):
    if i > 1:
        line = data[i].split('\n')[0]
        location = line.split('=')[0]
        location = location.strip()
        locations.append(location)

        rightside = line.split('=')[1]
        rightside = rightside.strip(' ()')
        left = rightside.split(',')[0]
        right = rightside.split(',')[1]
        right = right.strip()

        lefts.append(left)
        rights.append(right)

# Convert locations to a dictionary
location_dict = {}
for i, v in enumerate(locations):
    location_dict[v] = i
current_indices = []

for location in locations:
    if location[2] == 'A':
        current_index = find_index(location, location_dict)
        current_indices.append(current_index)

flag = True

while flag:
    direction = instructions[instruction_counter]
    instruction_counter += 1
    if instruction_counter >= len(instructions):
        instruction_counter = 0
    if direction == 'R':
        next_string_list = rights
    elif direction == 'L':
        next_string_list = lefts
    checker = []
    for i, c in enumerate(current_indices):
        next_string = next_string_list[c]
        next_index = find_index(next_string, location_dict)
        current_indices[i] = next_index
        if next_string[2] == 'Z':
            checker.append(1)
    if len(checker) == len(current_indices):
        flag = False
    step_count += 1
print(step_count)

