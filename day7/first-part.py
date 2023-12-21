def get_data():
    with open("input.txt") as data_file:
        return data_file.readlines()


def formatting_data(data_to_format):
    formatted_data = {}
    for row in data_to_format:
        first_value = row.strip().split(" ")[0]
        second_value = int(row.strip().split(" ")[1])
        formatted_data[first_value] = second_value
    return formatted_data


def set_type():
    card_typing = {"five of a kind": [], "four of a kind": [], "full house": [], "three of a kind": [], "two pair": [],
                   "one pair": [], "high card": []}
    for hand in camel_cards:
        for card in hand:
            card_count = hand.count(card)
            if card_count == 5:
                card_typing["five of a kind"].append(hand)
                break
            elif card_count == 4:
                card_typing["four of a kind"].append(hand)
                break
            elif card_count == 3:
                hand_copy = hand
                for yy in range(0, card_count):
                    hand_copy = hand_copy.replace(card, "")
                if hand_copy.count(hand_copy[0]) == 2:
                    card_typing["full house"].append(hand)
                else:
                    card_typing["three of a kind"].append(hand)
                break
            elif card_count == 2:
                hand_copy = hand
                for yy in range(0, card_count):
                    hand_copy = hand_copy.replace(card, "")
                if hand_copy.count(hand_copy[0]) == 2 or hand_copy.count(hand_copy[1]) == 2:
                    card_typing["two pair"].append(hand)
                else:
                    card_typing["one pair"].append(hand)
                break
            elif hand.index(card) == len(hand) - 1:
                card_typing["high card"].append(hand)
                break
    return card_typing


def merge_sort(array):
    array_length = len(array)
    if array_length > 1:
        middle = array_length // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            for card_index in range(0, len(left[i])):
                if type_of_cards.index(left[i][card_index]) < type_of_cards.index(right[j][card_index]):
                    array[k] = left[i]
                    i += 1
                    break
                elif type_of_cards.index(left[i][card_index]) > type_of_cards.index(right[j][card_index]):
                    array[k] = right[j]
                    j += 1
                    break
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


type_of_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
first_part_result = 0

data = get_data()
camel_cards = formatting_data(data)
grouped_cards = set_type()
ranking = []
for hand_type in grouped_cards.values():
    merge_sort(hand_type)
    print(hand_type)
    for x in hand_type:
        ranking.append(x)
ranking = ranking[::-1]
print(ranking)
for rank in range(0, len(ranking)):
    temp = camel_cards[ranking[rank]] * (rank + 1)
    first_part_result += temp

print(first_part_result)