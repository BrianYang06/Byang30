
def get_last_comma(str):
    reversed_string = str[::-1]
    for index in range(len(reversed_string)):
        if reversed_string[index] == ",":
            return len(str) - index - 1
    return -1

info = open("occupations.csv")
lines = info.read().split("\n")

occupation_to_percentage = {}
for i in lines[1:-1]:
    last_comma = get_last_comma(i)
    occupation = i[:last_comma]
    percentage = i[last_comma + 1:]

    occupation_to_percentage[occupation] = float(percentage)

print(occupation_to_percentage)