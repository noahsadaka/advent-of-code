def import_data(filename):
    file = open(filename,'r')
    data = file.readlines()
    data_2 = []
    for line in data:
        data_2.append(line.strip('\n'))
    return data_2

