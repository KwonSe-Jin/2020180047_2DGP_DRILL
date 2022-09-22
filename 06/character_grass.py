from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,90)
    x = x + 2
    delay(0.001)
    
y=0
while (y < 800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(800, y)
    y = y + 2
    delay(0.001)

x = 800
while (x > 0):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 600)
    x = x - 2
    delay(0.001)

y=600
while (y > 90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(0, y)
    y = y - 2
    delay(0.001)







close_canvas()
