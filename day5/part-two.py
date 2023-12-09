def sort_ranges(e):
    return e[0]


def remapping(formatting: str, value):
    format_number = [0, 0]
    for ranges in almanac[formatting]:
        destination_range_start = int(ranges[0])
        source_range_start = int(ranges[1])
        range_length = int(ranges[2])
        source_range_end = source_range_start + range_length
        destination_range_end = destination_range_start + range_length
        min_range = []
        format_number = 0
    print("HALOOO")
    return format_number


with open("input.txt") as data_file:
    almanac = {}
    for text_line in data_file.read().split("\n\n"):
        key = text_line.split(":")[0].replace(" map", "")
        temp_values = text_line.split(":")[1].strip().split("\n")
        values = []
        test = []
        if key != "seeds":
            for value_index in range(0, len(temp_values)):
                values.append(temp_values[value_index].split(" "))
        else:
            seed_numbers = temp_values[0].split(" ")
            seed_range = []
            for seed_index in range(0, len(seed_numbers)):
                seed_range.append(seed_numbers[seed_index])
                if seed_index % 2 != 0:
                    values.append(seed_range)
                    seed_range = []
        almanac[key] = values
all_locations_ranges = []
location_found = False
for ranges in almanac["humidity-to-location"]:
    temp_ranges = []
    for i in range(0, 3):
        if i != 1:
            temp_ranges.append(int(ranges[i]))
    all_locations_ranges.append(temp_ranges)
all_locations_ranges.sort(key=sort_ranges)
print(all_locations_ranges)

# while not location_found:
#     location += 1
#     humidity = remapping("humidity-to-location", location)
#     temperature = remapping("temperature-to-humidity", humidity)
#     light = remapping("light-to-temperature", temperature)
#     water = remapping("water-to-light", light)
#     fertilizer = remapping("fertilizer-to-water", water)
#     soil = remapping("soil-to-fertilizer", fertilizer)
#     seed = remapping("seed-to-soil", soil)
#     for seeds in almanac["seeds"]:
#         if int(seeds[0]) <= seed < int(seeds[0]) + int(seeds[1]):
#             location_found = True
#             break
#
# print(location)
#
