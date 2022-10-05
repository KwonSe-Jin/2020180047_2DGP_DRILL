from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas(TUK_WIDTH, TUK_HEIGHT)

arrow = load_image('hand_arrow.png')
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = sx, sy
ax, ay= x, y
frame = 0
hide_cursor()


def reset_world():
    global ax, ay
    global t
    global sx, sy
    ax, ay = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    t = 0
    sx, sy = x, y

def update_world():
    global x, y
    global t
    global state
    t += 0.005
    x = (1 - t) * sx + t * ax
    y = (1 - t) * sy + t * ay
    if t >= 1.0:
        reset_world()
    if sx <= ax:
        state = 1
    if sx > ax:
        state = 0


reset_world()
while running:
    update_world()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(ax, ay)
    character.clip_draw(frame * 100, 100 * state, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




