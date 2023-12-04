with open("input") as data_file:
    data = data_file.readlines()

sum = 0
for text_line in data:
    values_split = text_line.split(":")
    game_id = values_split[0]
    rolls = values_split[1].replace(" ", "").split(";")
    possible_roll = True
    highest_values = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for roll in rolls:
        for single_color_roll in roll.split(","):
            if "red" in single_color_roll:
                if highest_values["red"] < int(single_color_roll.replace("red", "")):
                    highest_values["red"] = int(single_color_roll.replace("red", ""))
            elif "green" in single_color_roll:
                if highest_values["green"] < int(single_color_roll.replace("green", "")):
                    highest_values["green"] = int(single_color_roll.replace("green", ""))
            elif "blue" in single_color_roll:
                if highest_values["blue"] < int(single_color_roll.replace("blue", "")):
                    highest_values["blue"] = int(single_color_roll.replace("blue", ""))
    roll_result = 1
    for key, value in highest_values.items():
        roll_result *= value
    sum += roll_result
print(sum)
