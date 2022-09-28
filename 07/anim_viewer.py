from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('sample.png')





frame = 0

for y in range(90, 450, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 97, 0, 97, 72, 40, 550 - y)  # clip : 시트를 짤라내서 그리겠다. 프레임 수에 맞춰서 짤라 냄
        update_canvas()
        frame = (frame + 1) % 4
        # frame2 = (frame2 + 1) % 6
        delay(0.005)
        get_events()


frame = 0
for x in range(80, 300, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw((frame * 97) + 291, 216, 97, 72, x, 90)  # clip : 시트를 짤라내서 그리겠다. 프레임 수에 맞춰서 짤라 냄
        update_canvas()
        frame = (frame + 1) % 3
        delay(0.05)
        get_events()

frame = 0
for x in range(300, 600, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw((frame * 97) + 97, 360, 97, 72, x, 90)  # clip : 시트를 짤라내서 그리겠다. 프레임 수에 맞춰서 짤라 냄
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.05)
        get_events()

frame = 0
for x in range(600, 750, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw((frame * 97) + 97, 144, 97, 72, x, 90)  # clip : 시트를 짤라내서 그리겠다. 프레임 수에 맞춰서 짤라 냄
        update_canvas()
        frame = (frame + 1) % 3
        delay(0.05)
        get_events()




