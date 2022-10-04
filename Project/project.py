from pico2d import *
import os
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2020180047_2DGP_DRILL\\Project\\resource')
grass_WIDTH, grass_HEIGHT = 800, 600
x = grass_WIDTH // 2
y = grass_WIDTH // 2

frame = 0
dirX = 0
dirY = 0
state = 3
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
                state = 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
                state = 0
            elif event.key == SDLK_UP:
                dirY += 1
                if state == 2:
                    state = 0
                if state == 3:
                    state = 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
                if state == 2:
                    state = 0
                if state == 3:
                    state = 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                state = 3
            elif event.key == SDLK_LEFT:
                dirX += 1
                state = 2
            elif event.key == SDLK_UP:
                dirY -= 1
                if state == 0:
                    state = 2
                if state == 1:
                    state = 3
            elif event.key == SDLK_DOWN:
                dirY += 1
                if state == 0:
                    state = 2
                if state == 1:
                    state = 3

open_canvas(grass_WIDTH, grass_HEIGHT)
TUK_GROUND = load_image('grass.png')
character = load_image('pika_0_0.png')
character1 = load_image('pika_0_1.png')
character2 = load_image('pika_0_2.png')
character3 = load_image('pika_0_3.png')
character4 = load_image('pika_0_4.png')

running = True

a = 0
while running:
    if a == 0:
        clear_canvas_now()
        TUK_GROUND.draw_now(grass_WIDTH // 2, grass_HEIGHT)
        character.draw_now(x, y , 100, 100)
        update_canvas()
        handle_events()
        a = 1
        # delay(0.01)
    elif a == 1:
        clear_canvas_now()
        TUK_GROUND.draw_now(grass_WIDTH // 2, grass_HEIGHT)
        character1.draw_now(x, y, 100, 100)
        update_canvas()
        handle_events()
        a = 2
        # delay(0.01)
    elif a == 2:
        clear_canvas_now()
        TUK_GROUND.draw_now(grass_WIDTH // 2, grass_HEIGHT)
        character2.draw_now(x, y, 100, 100)
        update_canvas()
        handle_events()
        a = 3
        # delay(0.01)
    elif a == 3:
        clear_canvas_now()
        TUK_GROUND.draw_now(grass_WIDTH // 2, grass_HEIGHT)
        character3.draw_now(x, y, 100, 100)
        update_canvas()
        handle_events()
        a = 4

    elif a == 4:
        clear_canvas_now()
        TUK_GROUND.draw_now(grass_WIDTH // 2, grass_HEIGHT)
        character4.draw_now(x, y, 100, 100)
        update_canvas()
        handle_events()
        a = 0
    # update_canvas()
    x += dirX * 10
    y += dirY * 10
    delay(0.05)
close_canvas()
