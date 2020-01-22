import string
import random
import time
import curses

def create_letter(letter_position, new_letter, new_position):
    "create new letter with its position in viewport and add to existing letters"
    if new_letter not in letter_position.keys():
        letter_position[new_letter] = [new_position, 0]
    return letter_position

def move_letter(letter_position):
    "move letter from existing position"
    for letter, position in letter_position.items():
        position[1] += 1
        letter_position[letter] = position
    return letter_position

def process(user_input, letter_position, score, life, max_ht):
    "Update score & remaining life"
    del_letter = []
    if user_input in letter_position.keys():
        del letter_position[user_input]
        score += 1
        
    for letter, position in letter_position.items():
        if position[1] == max_ht:
            del_letter.append(letter)
            life -= 1
            
    if del_letter:
        for i in del_letter:
            del letter_position[i]
    if life==0:
        return (letter_position, score, life, True)
    return (letter_position, score, life, False)


def delay(score, m):
    "Reduce time delay with increase in score"
    time_delay = 1
    if score >= m:
        time_delay = 1 - int(score/m) * .1
        if time_delay < .1:
            return .1
    return time_delay

def main(window):
    letters_and_positions = {}
    score = 0
    life = 5
    gameover = False
    height, width = window.getmaxyx()[0]-1, window.getmaxyx()[1]-1
    curses.curs_set(0)
    window.nodelay(True)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    while not gameover:
        letters_and_positions = create_letter(letters_and_positions, random.choice(string.ascii_lowercase), random.choice(range(0,width)))
        letters_and_positions = move_letter(letters_and_positions)
        try:
            user_input = window.getkey()
        except:
            user_input = ''
        letter_position, score, life, gameover = process(user_input, letters_and_positions, score, life,height)
        for letter, position in letter_position.items():
            window.addstr(position[1], position[0], letter, curses.A_BOLD)
        window.addstr(0, 0,'Score : {}'.format(score), curses.color_pair(1) | curses.A_BOLD )
        window.addstr(0, width - 10,'Life : {}'.format(life), curses.color_pair(1) | curses.A_BOLD )
        window.refresh()
        time.sleep(delay(score, 10))
        window.clear()
    window.addstr(int(height/2), int((width/2)-4), 'Game Over')
    window.addstr(int(height/2)+2, int((width/2)-6), 'Your Score: {}'.format(score))
    window.refresh()
    time.sleep(3)

if __name__ == '__main__':
    curses.wrapper(main)
