import letter_invader

def test_letter_and_position():
    assert letter_invader.letter_position({}, 100) == {'a' : [20, 100]}
