from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
      #  self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
       # self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 0, 0))


