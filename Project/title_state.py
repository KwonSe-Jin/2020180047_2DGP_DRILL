import game_framework
from pico2d import *
import Move
import os
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2020180047_2DGP_DRILL\\Project\\resource')
image = None

def enter():
    global image
    image = load_image('Title.png')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(Move)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
