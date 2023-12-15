from copy import deepcopy
file= open('example', 'r') 
data = file.readlines()

def retrieve_mappings(lines, start_index):
    flag = True
    out = []
    ind = start_index + 1
    while flag and ind < len(lines):
        line = lines[ind].split('\n')[0]
        if line != '':
            line_str = line.split()
            line_int = []
            for l in line_str:
                line_int.append(int(l))
            out.append(line_int)
            ind += 1
        else:
            flag = False
    return out

def thing1_to_thing2(thing1, mapping):
    thing2 = []
    for mapp in mapping:
        dest_start = mapp[0]
        dest_end = mapp[0] + mapp[2] - 1

        source_start = mapp[1]
        source_end =  mapp[1] + mapp[2] - 1
        flag = True
        ind = 0
        while flag:
            thing_start = thing1[2*ind]
            thing_end = thing1[2*ind] + thing1[2*ind + 1] - 1
            # 3 cases where we need to consider this: 1) thing1 fully contained
            # by source range. 2) thing1 end sticks out 3) thing1 start sticks out
            if thing_start >= source_start and thing_start <= source_end or (thing_end <= source_end and thing_end >= source_start):
                # Easy case: fully contained
                if thing_start >= source_start and thing_end <= source_end:
                    incrementer = thing_start - source_start
                    thing2.append([dest_start + incrementer, thing1[2*ind+1]])
                # end sticks out
                elif thing_start >= source_start and thing_end > source_end:
                    incrementer = thing_start - source_start
                    delta = (thing_end - source_end)
                    num_keep = thing1[2*ind+1]] - delta
                    thing2.append([dest_start + incrementer, num_keep])
                    thing2.append([source_start + delta, delta])
                # start sticks out
                else:
                    delta = source_start - thing_start
                    #.....

            else:
                ind += 1

            if 2*ind > len(thing1):
                flag = False
                
    return thing2

# Parsing
seeds_str = data[0].split('\n')[0].split(':')[1].split()
seeds = []
for i in range(int(len(seeds_str)/2)):
    startval = int(seeds_str[2*i])
    rangeval = int(seeds_str[2*i+1])
    seeds.append([startval, rangeval])
for ind, line in enumerate(data):
    cur_line = line.split('\n')[0]
    if cur_line == 'seed-to-soil map:':
        seed_soil_id = ind
    elif cur_line == 'soil-to-fertilizer map:':
        soil_fert_id = ind
    elif cur_line == 'fertilizer-to-water map:':
        fert_water_id = ind
    elif cur_line == 'water-to-light map:':
        water_light_id = ind
    elif cur_line == 'light-to-temperature map:':
        light_temp_id = ind
    elif cur_line == 'temperature-to-humidity map:':
        temp_humid_id = ind
    elif cur_line == 'humidity-to-location map:':
        humid_loc_id = ind
seed_soil_mapping = retrieve_mappings(data, seed_soil_id)
soil_fert_mapping = retrieve_mappings(data, soil_fert_id)
fert_water_mapping = retrieve_mappings(data, fert_water_id)
water_light_mapping = retrieve_mappings(data, water_light_id)
light_temp_mapping = retrieve_mappings(data, light_temp_id)
temp_humid_mapping = retrieve_mappings(data, temp_humid_id)
humid_loc_mapping = retrieve_mappings(data, humid_loc_id)

# Mapping conversions
soil = thing1_to_thing2(deepcopy(seeds), seed_soil_mapping)
fert = thing1_to_thing2(deepcopy(soil), soil_fert_mapping)
water = thing1_to_thing2(deepcopy(fert), fert_water_mapping)
light = thing1_to_thing2(deepcopy(water), water_light_mapping)
temp = thing1_to_thing2(deepcopy(light), light_temp_mapping)
humid = thing1_to_thing2(deepcopy(temp), temp_humid_mapping)
loc = thing1_to_thing2(deepcopy(humid), humid_loc_mapping)
print(min(loc))

