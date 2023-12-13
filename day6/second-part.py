def formatting_data(data):
    global races
    for row in data:
        races[row.split(":")[0]] = int(row.split(":")[1].strip().replace(" ", ""))


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
second_part_result = race_strategy(races["Time"], races["Distance"])
print(second_part_result)

