def formatting_data(data):
    global races
    for row in data:
        row_numbers = []
        for number in row.split(":")[1].strip().split(" "):
            if number:
                row_numbers.append(int(number))
        races[row.split(":")[0]] = row_numbers


def get_data():
    with open("input.txt") as data_file:
        return data_file.readlines()


races = {}
formatting_data(get_data())
print(races)

