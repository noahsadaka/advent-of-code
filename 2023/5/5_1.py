from copy import deepcopy
file= open('input', 'r') 
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

def thing1_to_thing2(thing1_IDs, mapping):
    thing2_IDs = deepcopy(thing1_IDs)
    for mapp in mapping:
        dest_start = mapp[0]
        dest_end = mapp[0] + mapp[2] - 1

        source_start = mapp[1]
        source_end =  mapp[1] + mapp[2] - 1
        for i, thing in enumerate(thing1_IDs):
            if thing >= source_start and thing <= source_end:
                incrementer = thing - source_start
                thing2_IDs[i] = dest_start + incrementer
                
    return thing2_IDs

# Parsing
seeds_str = data[0].split('\n')[0].split(':')[1].split()
seeds = []
for seed in seeds_str:
    seeds.append(int(seed))
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

