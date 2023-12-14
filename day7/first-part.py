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
    card_typing = {"five": [], "four": [], "full": [], "three": [], "two": [], "one": [], "high": []}
    for hand in camel_cards:
        for card in hand:
            hand_count = hand.count(card)
            if hand_count == 5:
                card_typing["five"].append(hand)
                break
            elif hand_count == 4:
                card_typing["four"].append(hand)
                break
            elif hand_count == 3 or hand_count == 2:
                hand_copy = hand
                for _ in range(0, hand_count):
                    hand_copy = hand_copy.replace(card, "")
                if hand_copy.count(hand_copy[0]) == 3 or hand_copy.count(hand_copy[0]) == 2:
                    card_typing["full"].append(hand)
                elif hand_count == 3:
                    card_typing["three"].append(hand)
                elif (hand_copy.count(hand_copy[0]) == 2 or hand_copy.count(hand_copy[1]) == 2
                      or hand_copy.count(hand_copy[2]) == 2):
                    card_typing["two"].append(hand)
                else:
                    card_typing["one"].append(hand)
                break
            elif hand.index(card) == len(hand) - 1:
                card_typing["high"].append(hand)
    return card_typing


def resolve_same_values(first_hand, second_hand):
    for i in first_hand:
        if type_of_cards.index(first_hand[i]) < type_of_cards.index(second_hand[i]):
            return



def calc_ranking(grouped_types):
    global first_part_result
    ranking = []
    for hand_type, hands in grouped_types.items():
        in_type_ranking = []
        for hand_index in range(0, len(hands)):
            if not in_type_ranking:
                in_type_ranking.append(hands[hand_index])
            else:
                for ranking_index in range(0, len(in_type_ranking)):
                    if type_of_cards.index(hands[hand_index][0]) < type_of_cards.index(in_type_ranking[ranking_index][0]):
                        in_type_ranking.insert(ranking_index, hands[hand_index])
                        break
                    elif type_of_cards.index(hands[hand_index][0]) == type_of_cards.index(in_type_ranking[ranking_index][0]):
                        resolve_same_values()




type_of_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
first_part_result = 0

data = get_data()
camel_cards = formatting_data(data)
grouped_cards = set_type()
calc_ranking(grouped_cards)
