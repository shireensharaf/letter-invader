import letter_invader

#create new letter position pair
def test_letter_insert_new_letter():
    assert letter_invader.create_letter({'a' : [20, 0]}, 'g', 45) == {'a' : [20, 0], 'g' : [45, 0]}

def test_letter_new_letter_repeat():
    assert letter_invader.create_letter({'a' : [20, 10]}, 'a', 45) == {'a' : [20, 10]}


#move letter

def test_letter_and_update_position():
    assert letter_invader.move_letter({'a' : [20, 0]}) == {'a' : [20, 1]}

def test_letter_and_update_position_multiple():
    assert letter_invader.move_letter({'a' : [20, 0], 'g': [45, 10]}) == {'a' : [20, 1], 'g' : [45, 11]}



#time delay

def test_delay_first_state():
    assert letter_invader.delay(2, 10, 'normal') == 1

def test_delay_reduce_delay():
    assert letter_invader.delay(10, 10,'normal') == .9

def test_delay_second_state():
    assert letter_invader.delay(23, 10, 'normal') == .8
    
def test_minimum_delay():
    assert letter_invader.delay(100, 10, 'normal') == .1


def test_delay_first_state_medium():
    assert letter_invader.delay(2, 10, 'medium') == .7

def test_delay_reduce_delay_medium():
    assert letter_invader.delay(10, 10,'medium') == .6

def test_delay_second_state_medium():
    assert letter_invader.delay(23, 10, 'medium') == .5
    
def test_minimum_delay_medium():
    assert letter_invader.delay(100, 10, 'medium') == .1

def test_delay_first_state_tough():
    assert letter_invader.delay(2, 10, 'hard') == .4

def test_delay_reduce_delay_tough():
    assert letter_invader.delay(10, 10,'hard') == .3

def test_delay_second_state_tough():
    assert letter_invader.delay(23, 10, 'hard') == .2
    
def test_minimum_delay_tough():
    assert letter_invader.delay(100, 10, 'hard') == .1

   
    
#process

def test_process_no_input():
    letter_and_position, score, life, game_over =  letter_invader.process('', {'a' : [20, 1], 'g' : [45, 0]}, 0, 5, 100)
    assert letter_and_position == {'a' : [20, 1], 'g' : [45, 0]}
    assert score == 0
    assert life == 5

def test_process_correct_input():
    letter_and_position, score, life, game_over = letter_invader.process('a', {'a' : [20, 1], 'g' : [45, 0]}, 0, 5, 100)
    assert letter_and_position == {'g' : [45, 0]}
    assert score ==  1
    assert life == 5

def test_process_reduce_life():
    letter_and_position, score, life, game_over = letter_invader.process('', {'a' : [20, 1], 'g' : [45, 100]}, 1, 5, 100)
    assert letter_and_position == {'a' : [20, 1]}
    assert score ==  1
    assert life == 4
    assert game_over == False
    
    
def test_process_gameover():
    letter_and_position, score, life, game_over = letter_invader.process('', {'a' : [20, 1], 'g' : [45, 100]}, 1, 1, 100)
    assert letter_and_position == {'a' : [20, 1]}
    assert score ==  1
    assert life == 0
    assert game_over == True

