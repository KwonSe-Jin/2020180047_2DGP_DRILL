from pico2d import *
import random
import game_framework
import game_world

#Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:


    def __init__(self):
        Bird.image = load_image('bird_animation.png')
        self.x = random.randint(25, 1550)
        self.y = random.randint(400, 500)
        self.dir = 1
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x <= 25:
            self.dir = 1
        elif self.x >= 1550 - 25:
            self.dir -= 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 184, 168, 184, 168, 0, 'h', self.x, self.y, 100, 100)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 184, 168, 184, 168, 3.141592 / 16, ' ', self.x, self.y, 100, 100)
