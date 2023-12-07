

def search_adjacent(t_index, c_index):
    global gears
    global symbol_positions
    starting_row = t_index - 1
    ending_row = t_index + 1
    starting_column = c_index - 1
    ending_column = c_index + 1
    if t_index == 0:
        starting_row = t_index
    elif t_index == len(data) - 1:
        ending_row = t_index - 1
    if c_index == 0:
        starting_column = c_index
    elif c_index == len(text) - 1:
        ending_column = c_index

    found_any_symbol = False
    for row in range(starting_row, ending_row + 1):
        for column in range(starting_column, ending_column + 1):
            if not data[row][column].isdigit() and data[row][column] != ".":
                symbol_positions.append([row, column])
                if data[row][column] == "*":
                    if row not in gears:
                        gears[row] = {}
                    if column not in gears[row]:
                        gears[row] = {column: [1, 1]}
                    else:
                        gears[row][column][0] += 1
                found_any_symbol = True
    return found_any_symbol


with open("input.txt") as data_file:
    data = data_file.readlines()
first_part_result = 0
second_part_result = 0
gears = {}
number = ""
near_symbol = False
symbol_positions = []
for text_index in range(0, len(data)):
    text = data[text_index].strip()
    for character_index in range(0, len(text)):
        character = text[character_index]
        if character.isdigit():
            if not near_symbol:
                near_symbol = search_adjacent(text_index, character_index)
            number += character
            if character_index == len(text) - 1 or not text[character_index + 1].isdigit():
                if near_symbol:
                    first_part_result += int(number)
                    for symbol_position in symbol_positions:
                        if data[symbol_position[0]][symbol_position[1]] == "*":
                            print(symbol_position)
                            # gears[symbol_position[0]][symbol_position[1]][1] *= int(number)
                near_symbol = False
                number = ""
    symbol_position = []
for gear_x, gear_y in gears.items():
    for gear_values in gear_y.values():
        if gear_values[0] == 2:
            second_part_result += gear_values[1]
print(first_part_result)
print(second_part_result)
