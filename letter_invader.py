max_ht = 100

def letter_position(letter_position, new_letter, max_ht):
    for letter, position in letter_position.items():
        position[1] -= 1
        letter_position[letter] = position
    if(new_letter):
        letter_position[new_letter[0]] = [new_letter[1], max_ht]
    return letter_position
