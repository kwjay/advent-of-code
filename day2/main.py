with open("input") as data_file:
    data = data_file.readlines()
    possible_games = 0

for text_line in data:
    values_split = text_line.split(":")
    game_id = values_split[0]
    rolls = values_split[1].replace(" ", "").split(";")
    possible_roll = True
    for roll in rolls:
        for single_color_roll in roll.split(","):
            if "red" in single_color_roll and int(single_color_roll.replace("red", "")) > 12:
                possible_roll = False
            elif "green" in single_color_roll and int(single_color_roll.replace("green", "")) > 13:
                possible_roll = False
            elif "blue" in single_color_roll and int(single_color_roll.replace("blue", "")) > 14:
                possible_roll = False
    if possible_roll:
        possible_games += int(game_id.replace("Game ", " "))
print(possible_games)
