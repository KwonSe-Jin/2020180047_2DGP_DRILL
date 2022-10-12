from pico2d import*
import os
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2020180047_2DGP_DRILL\\Project\\resource')


class Move:
    def __init__(self):
        self.x = 100
        self.y = 90
        self.frame = 0
        self.image = load_image('Pikachu.png')
    def update(self, x):
        self.frame = (self.frame + 1) % 5
        self.x += x * 5
    def draw(self, state):
        self.state = state
        if state:
            self.image.clip_draw(self.frame*64, self.state * 64, 64, 64, self.x, self.y)
        else:
            self.image.clip_draw(0, 320, 64, 64, self.x, self.y)

def handle_events():
    global running
    global x
    global state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                x += 1
                state = 5
            elif event.key == SDLK_a:
                x -= 1
                state = 5
        elif event.type == SDL_KEYUP:
                x = 0
                state = 0

open_canvas()
pikachu = Move()
running = True
x = 0
state = 0

while running:
    handle_events()
    pikachu.update(x)
    clear_canvas()
    # grass.draw()
    pikachu.draw(state)
    update_canvas()
    delay(0.05)

# finalization code
close_canvas()




