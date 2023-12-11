
def precision_mapping(formatting: str, seed_number: int):
    formatted_number = -1
    for ranges in almanac[formatting]:
        destination_range_start = int(ranges[0])
        source_range_start = int(ranges[1])
        range_length = int(ranges[2])
        source_range_end = source_range_start + range_length
        destination_range_end = destination_range_start + range_length
        if source_range_start <= seed_number < source_range_end:
            formatted_number = destination_range_end - (source_range_end - 1 - seed_number) - 1
            break
        else:
            formatted_number = seed_number
    return formatted_number


def range_remapping(formatting: str, search_ranges):
    returning_ranges = []
    lowest_range = -1
    for search_range in search_ranges:
        for ranges in almanac[formatting]:
            x = int(ranges[0])
            y = int(ranges[1])
            z = int(ranges[2])
            format_range = [y, y + z]
            if x <= search_range[0] or x >= search_range[0] and x + z >= search_range[1]:
                returning_ranges.append(format_range)
            if format_range[0] < lowest_range or lowest_range == -1:
                lowest_range = format_range[0]
    if not returning_ranges:
        returning_ranges.append([0, lowest_range])
    return returning_ranges


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


result = -1
found_location = False
location = 0
# for seeds in almanac["seeds"]:
#     for seed in range(int(seeds[0]), int(seeds[0]) + int(seeds[1])):
#
#         # soil = mapping("seed-to-soil", int(seed))
#         # fertilizer = mapping("soil-to-fertilizer", soil)
#         # water = mapping("fertilizer-to-water", fertilizer)
#         # light = mapping("water-to-light", water)
#         # temperature = mapping("light-to-temperature", light)
#         # humidity = mapping("temperature-to-humidity", temperature)
#         # location = mapping("humidity-to-location", humidity)
#         if result > location or result == -1:
#             result = location
location_ranges = []
for xyz in almanac["humidity-to-location"]:
    location_ranges.append([int(xyz[0]), int(xyz[0]) + int(xyz[2])])
location_ranges.sort()
location_ranges.append([0, location_ranges[0][0]])
location_ranges.sort()
for location_range in location_ranges:
    humidity_ranges = range_remapping("humidity-to-location", [location_range])
    temperature_ranges = range_remapping("temperature-to-humidity", humidity_ranges)
    print(f"{humidity_ranges} : {temperature_ranges}")
print(location_ranges)

