import letter_invader

def test_letter_and_position_initial():
    assert letter_invader.letter_position({}, ['a', 20], 100) == {'a' : [20, 100]}

def test_letter_and_update_position_no_new():
    assert letter_invader.letter_position({'a' : [20, 100]}, [], 100) == {'a' : [20, 99]}

def test_letter_and_update_position_insert_new_letter():
    assert letter_invader.letter_position({'a' : [20, 100]}, ['g', 45], 100) == {'a' : [20, 99], 'g' : [45, 100]}


#process

def test_process_no_input():
    assert letter_invader.process('', {'a' : [20, 99], 'g' : [45, 100]}, 0, 5) == [{'a' : [20, 99], 'g' : [45, 100]}, 0, 5]
