NUMBERS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("advent_day1.txt") as data_file:
    data = data_file.readlines()

result = 0
for text_line in data:
    first_digit = ""
    second_digit = ""
    temp_text = ""
    for char in text_line:
        temp_text += char
        for number_key, number_value in NUMBERS.items():
            if number_key in temp_text or number_value in temp_text:
                first_digit = number_value
                break
        if first_digit != "":
            break
    temp_text = ""
    for char in text_line[::-1]:
        temp_text = char + temp_text
        for number_key, number_value in NUMBERS.items():
            if number_key in temp_text or number_value in temp_text:
                second_digit = number_value
                break
        if second_digit != "":
            break
    result += int(first_digit + second_digit)
print(result)
