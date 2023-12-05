

def check_for_digit(positions, line:str):
    for position in positions:
        if position != 0 and position != len(line):
            if line[position].isdigit():
                return line[position]



with open("input.txt") as data_file:
    data = data_file.readlines()
for line_index in range(0, len(data)):
    text_line = data[line_index]
    for char_index in range(0, len(text_line)):
        if not text_line[char_index].isdigit() and text_line[char_index] != ".":
            places_to_check = [char_index-1, char_index, char_index+1]

