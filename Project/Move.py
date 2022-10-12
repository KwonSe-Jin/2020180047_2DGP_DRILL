from pico2d import*
import os
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2020180047_2DGP_DRILL\\Project\\resource')
import game_framework
import title_state
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)


class Move:
    def __init__(self):
        self.x = 100
        self.y = 80
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
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


x = 0
state = 0

pikachu = None
grass = None
running = None
# 초기화
def enter():
    global pikachu, grass, running
    pikachu = Move()
    grass = Grass()
    running = True
# 종료
def exit():
    global pikachu, grass
    del pikachu
    del grass
def update():
    pikachu.update(x)
def draw():
    clear_canvas()
    grass.draw()
    pikachu.draw(state)
    update_canvas()
    delay(0.08)





