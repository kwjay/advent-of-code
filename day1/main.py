with open("advent_day1.txt") as data_file:
    data = data_file.readlines()
result = 0
for text_line in data:
    first_digit = "none"
    for char in text_line.strip():
        if char.isdigit() and first_digit == "none":
            first_digit = char
            break
    second_digit = "none"
    for char in text_line[::-1]:
        if char.isdigit() and second_digit == "none":
            second_digit = char
            break
    number = first_digit + second_digit
    result += int(number)
print(result)
