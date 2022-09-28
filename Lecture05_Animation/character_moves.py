from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


for x in range(0, 800, 2):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
   # x = x + 2
    update_canvas()
    delay(0.01)
    get_events() # 현재 프로세스가 다른 프로세스에게 os에게 실행권을 넘겨 줌

close_canvas()

