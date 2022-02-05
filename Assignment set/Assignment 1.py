
characters = []
discard = []


def find_common_characters(msg1, msg2):
    for pointer_one in msg1:
        for pointer_two in msg2:
            if pointer_one == pointer_two:
                if pointer_one == ' ':
                    discard.append(pointer_one)
                else:
                    characters.append(pointer_one)

    common_characters = set(characters)
    return common_characters


# Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
