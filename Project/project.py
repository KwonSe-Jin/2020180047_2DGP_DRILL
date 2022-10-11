from pico2d import *
import os
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2020180047_2DGP_DRILL\\Project\\resource')

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 900
x = TUK_WIDTH // 2
y = TUK_WIDTH // 2
R_x = TUK_WIDTH // 2
R_y = TUK_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0
state = 0
dir_state = 0

def handle_events():
    global running
    global dirX
    global dirY
    global state
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
                state = 5
            elif event.key == SDLK_LEFT:
                dirX -= 1
                state = 5
            elif event.key == SDLK_UP:
                dirY += 1
                state = 4
            elif event.key == SDLK_DOWN:
                dirY -= 1
                state = 3
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            dirX = 0
            dirY = 0
            state = 0


open_canvas(TUK_WIDTH, TUK_HEIGHT)
# TUK_GROUND = load_image('TUK_GROUND.png')
character = load_image('Pikachu.png')
character2 = load_image('Pikachu_R.png')
running = True
player = True
playerR = True
while running:
    clear_canvas()
    if player == True:

        # TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if state:
            character.clip_draw(frame * 64, state * 64, 64, 64, x, y, 100, 100)
        else:
            character.clip_draw(0, 320, 64, 64, x, y, 100, 100)
        handle_events()
        frame = (frame + 1) % 5
        x += dirX * 5
        y += dirY * 5
        delay(0.05)
        if (x > TUK_WIDTH or y > TUK_HEIGHT or x < 0 or y < 0):
             break
    if playerR == True:

        # TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if state:
            character2.clip_draw(frame * 64, state * 64, 64, 64, R_x, R_y, 100, 100)
        else:
            character2.clip_draw(0, 320, 64, 64, R_x, R_y, 100, 100)
        handle_events()
        frame = (frame + 1) % 5
        R_x += dirX * 5
        R_y += dirY * 5
        delay(0.05)
        if (R_x > TUK_WIDTH or R_y > TUK_HEIGHT or R_x < 0 or R_y < 0):
            break
    update_canvas()


close_canvas()
