from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0

frame = 0
for y in range(90, 550, 5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, frame * 100, 100, 100, 90, y) # clip : 시트를 짤라내서 그리겠다. 프레임 수에 맞춰서 짤라 냄
    update_canvas()
    frame = (frame + 1) % 4
    # x += 5
    delay(0.05)
    get_events()


close_canvas()

