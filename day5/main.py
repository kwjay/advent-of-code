
def mapping(formatting: str, seed_number: int):
    format_number = -1
    for ranges in almanac[formatting]:
        destination_range_start = int(ranges[0])
        source_range_start = int(ranges[1])
        range_length = int(ranges[2])
        source_range_end = source_range_start + range_length
        destination_range_end = destination_range_start + range_length
        if source_range_start <= seed_number < source_range_end:
            format_number = destination_range_end - (source_range_end - 1 - seed_number) - 1
            break
        else:
            format_number = seed_number
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
result = -1
found_location = False
for seeds in almanac["seeds"]:
    for seed in range(int(seeds[0]), int(seeds[0]) + int(seeds[1])):
        print(seed)
        soil = mapping("seed-to-soil", int(seed))
        fertilizer = mapping("soil-to-fertilizer", soil)
        water = mapping("fertilizer-to-water", fertilizer)
        light = mapping("water-to-light", water)
        temperature = mapping("light-to-temperature", light)
        humidity = mapping("temperature-to-humidity", temperature)
        location = mapping("humidity-to-location", humidity)
        if result > location or result == -1:
            result = location
print(result)

