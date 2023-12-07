

def search_adjacent(t_index, c_index):
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

    for row in range(starting_row, ending_row + 1):
        for column in range(starting_column, ending_column + 1):
            if not data[row][column].isdigit() and data[row][column] != ".":
                return True
    return False


with open("input.txt") as data_file:
    data = data_file.readlines()
result = 0
number = ""
near_symbol = False
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
                    result += int(number)
                near_symbol = False
                number = ""
print(result)
