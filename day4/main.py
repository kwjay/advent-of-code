
def split_numbers(data_to_format: str):
    list_of_numbers = data_to_format.split(" ")
    while "" in list_of_numbers:
        list_of_numbers.remove('')
    return list_of_numbers


with open("input.txt") as data_file:
    data = data_file.readlines()
first_part_result = 0
for card in data:
    card_result = 0
    card = card.strip().split(": ")[1]
    card_numbers = card.split(" | ")
    winning_numbers = split_numbers(card_numbers[0])
    drawn_numbers = split_numbers(card_numbers[1])
    won_numbers = []
    for drawn_number in drawn_numbers:
        if drawn_number in winning_numbers and drawn_number not in won_numbers:
            won_numbers.append(drawn_number)
            if card_result == 0:
                card_result = 1
            else:
                card_result *= 2

    first_part_result += card_result
print(first_part_result)
