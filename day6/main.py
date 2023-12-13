def formatting_data(data):
    global races
    for row in data:
        row_numbers = []
        for number in row.split(":")[1].strip().split(" "):
            if number:
                row_numbers.append(int(number))
        races[row.split(":")[0]] = row_numbers


def get_data():
    with open("input.txt") as data_file:
        return data_file.readlines()


def race_strategy(time, distance):
    ways_to_win = 0
    for hold_time in range(0, time):
        distance_travelled = (time - hold_time) * hold_time
        if distance_travelled > distance:
            ways_to_win += 1
    return ways_to_win


races = {}
formatting_data(get_data())
first_part_result = 1
for race in range(0, len(races["Time"])):
    first_part_result *= race_strategy(races["Time"][race], races["Distance"][race])
print(first_part_result)

