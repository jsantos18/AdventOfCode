import re

def parse(line):
    amounts = re.match(r'([0-9]+)-([0-9]+)\s([a-z]+):\s([a-z]+)', line)
    return amounts.groups()
    

def search(least, most, character, string):
    char_amount = 0
    for i in string:
        if character == i:
            char_amount += 1
    if int(least) <= char_amount <= int(most):
        return 1
    return 0


def positions(pos1, pos2, character, string):
    first_pos = string[int(pos1) - 1] == character
    second_pos = string[int(pos2) - 1] == character
    if first_pos ^ second_pos:
        return 1
    return 0


if __name__ == "__main__":
    with open("input.txt") as passwords:
        valid_passwords_1 = 0
        valid_passwords_2 = 0
        for line in passwords:
            least, most, character, string = parse(line)
            valid_passwords_1 += search(least, most, character, string)
            valid_passwords_2 += positions(least, most, character, string)
        print("Valid Passwords 1: ", valid_passwords_1)
        print("Valid Passwords 2: ", valid_passwords_2)

