from pico2d import*
import os
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2020180047_2DGP_DRILL\\Project\\resource')
import game_framework
import title_state
class Grass:
    def __init__(self):
        self.image = load_image('background.png')
        self.net = load_image('net.png')
    def draw(self):
        self.image.draw(400, 300)
        self.net.draw(400, 150)


class Move:
    def __init__(self):
        self.x = 100
        self.y = 95
        self.frame = 0
        self.image = load_image('Pikachu.png')
        self.dirx = 0
        self.diry = 0
        self.m = 0.5
        self.v = 0.5
        self.jump = 0
        self.F = 0
        self.locate = 0
    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x += self.dirx * 5
        if self.jump == 1:
            if self.v > 0:
                self.F = (0.5 * self.m * (self.v * self.v))
            else:
                self.F = -(0.5 * self.m * (self.v * self.v))

            self.y -= self.F
            self.v -= 0.1
    def draw(self):
        if self.locate:
            self.image.clip_draw(self.frame*64, self.locate * 64, 64, 64, self.x, self.y, 100, 100)
        else:
            self.image.clip_draw(0, 320, 64, 64, self.x, self.y, 100, 100)

def handle_events():
    global running
    global dirx
    global diry
    global locate
    global F
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                pikachu.dirx += 1
                pikachu.locate = 5
            elif event.key == SDLK_a:
                pikachu.dirx -= 1
                pikachu.locate = 5
            elif event.key == SDLK_w:
                pikachu.jump = 1
                pikachu.locate = 4
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d or event.key == SDLK_a:
                pikachu.dirx = 0
                pikachu.locate = 0
            elif event.key == SDLK_w:
                pikachu.jump = 0

        if pikachu.x < 30:
            pikachu.dirx = 0
            if pikachu.locate == 4:
                pikachu.dirx += 1

        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

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
    pikachu.update()
def draw():
    clear_canvas()
    grass.draw()
    pikachu.draw()
    update_canvas()
    delay(0.03)





