max_ht = 100

def letter_position(letter_position, new_letter, max_ht):
    "letter and its position for viewport and update existing position"
    for letter, position in letter_position.items():
        position[1] -= 1
        letter_position[letter] = position
    if(new_letter):
        letter_position[new_letter[0]] = [new_letter[1], max_ht]
    return letter_position


def process(user_input, letter_position, score, life):
    "Update score & remaining life"
    if(user_input in letter_position.keys()):
        del letter_position[user_input]
        score += 1
    return [letter_position, score, life]
