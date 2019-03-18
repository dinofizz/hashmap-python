from random import randint


def get_random_string():
    length = randint(1, 10)
    chars = []
    for i in range(length):
       chars.append(chr(randint(97,122)))
    return "".join(chars)


dictionary = {}

for i in range(100):

    while True:
        key = get_random_string()
        value = get_random_string()

        if key not in dictionary:
            dictionary[key] = value
            break
        else:
            key = get_random_string()

with open("test_data.csv", "w+") as file:
    for item in dictionary:
        line = f"{item},{dictionary[item]}\n"
        file.write(line)
