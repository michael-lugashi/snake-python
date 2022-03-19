import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

#constants

WINDOW_WIDTH = 60  # number of columns of window box
WINDOW_HEIGHT = 20 # number of rows of window box

# setup window
curses.initscr()
win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH) # rows, columns
win.keypad(True)
curses.noecho()
win.border(0)

snake = [(4,10), (4,9), (4,8)] # snake body
food = (12, 40) # food coordinates
win.addch(food[0], food[1], 'X')

score = 0
SPC = 32
ESC = 27
key = curses.KEY_RIGHT

for pos in snake:
    win.addch(pos[0], pos[1], 'O')

while key != ESC:
    win.addstr(0, 4, 'Score ' + str(score) + ' ')

    # snake speed
    snake_speed = 150 - (len(snake)) // 2
    if snake_speed < 75:
        snake_speed = 75
    win.timeout(snake_speed)

    # get user input
    event = win.getch()
    prev_key = key
    key = event if event != -1 else prev_key
    if key not in [SPC, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, ESC]:
        key = prev_key

    # pause
    if key == SPC:
        continue

    # move snake
    snake_head = snake[0]
    snake_tail = snake[-1] 

    if key == KEY_LEFT and prev_key != KEY_RIGHT:
        snake.insert(0, (snake_head[0], snake_head[1] - 1))
    elif key == KEY_LEFT:
        snake.insert(0, (snake_head[0], snake_head[1] + 1))
        key = prev_key
    elif key == KEY_RIGHT and prev_key != KEY_LEFT:
        snake.insert(0, (snake_head[0], snake_head[1] + 1))
    elif key == KEY_RIGHT:
        snake.insert(0, (snake_head[0], snake_head[1] - 1))
        key = prev_key
    elif key == KEY_UP and prev_key != KEY_DOWN:
        snake.insert(0, (snake_head[0] - 1, snake_head[1]))
    elif key == KEY_UP:
        snake.insert(0, (snake_head[0] + 1, snake_head[1]))
        key = prev_key
    elif key == KEY_DOWN and prev_key != KEY_UP:
        snake.insert(0, (snake_head[0] + 1, snake_head[1]))
    elif key == KEY_DOWN:
        snake.insert(0, (snake_head[0] - 1, snake_head[1]))
        key = prev_key

    snake_head = snake[0]

    # check if snake hit itself
    if snake_head in snake[1:]:
        break

    # check if snake hit wall

    if snake_head[0] == 0 or snake_head[0] == WINDOW_HEIGHT - 1:
        break
    if snake_head[1] == 0 or snake_head[1] == WINDOW_WIDTH - 1:
        break

    # check if snake ate food
    if snake_head == food:
        win.addch(food[0], food[1], ' ')
        while(food in snake):
            food = (randint(1, WINDOW_HEIGHT - 2), randint(1, WINDOW_WIDTH - 2))
        win.addch(food[0], food[1], 'X')
        score += 1
    else:
        win.addch(snake_tail[0], snake_tail[1], ' ')
        snake.pop()
    
    win.addch(snake_head[0], snake_head[1], 'O')
    

curses.endwin()
print('Game Over! Score: ' + str(score))
