import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

#constants

WINDOW_WIDTH = 60  # number of columns of window box
WINDOW_HEIGHT = 20 # number of rows of window box

# setup window
curses.initscr()
win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH) # rows, columns
curses.noecho()
win.border(0)
win.nodelay(False)

snake = [[4,10], [4,9], [4,8]] # snake body
food = (randint(1, WINDOW_HEIGHT - 2), randint(1, WINDOW_WIDTH - 2))
win.addch(food[0], food[1], 'X')

score = 0
SPC = 32
ESC = 27
key = curses.KEY_RIGHT

for pos in snake:
    win.addch(pos[0], pos[1], 'O')

while key != ESC:
    win.addstr(0, 4, 'Score ' + str(score) + ' ')
    snake_speed = 150 - (len(snake)) // 2
    if snake_speed < 75:
        snake_speed = 75
    win.timeout(snake_speed) # increase speed
    prev_key = key
    event = win.getch()
    # print(event)
    key = event if event != -1 else prev_key
    if key not in [SPC, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, ESC]:
        key = prev_key
    

curses.endwin()

