

def search_adjacent(t_index, c_index):

    return True



with open("input.txt") as data_file:
    data = data_file.readlines()
result = 0
number = ""
for text_index in range(0, len(data)):
    text = data[text_index].strip()
    for character_index in range(0, len(text)):
        character = text[character_index]
        if character.isdigit():
            search_adjacent(text_index, character_index)
            number += character
        else:
            if number != "":
                if search_adjacent(text_index, character_index):
                    result += int(number)
            number = ""

