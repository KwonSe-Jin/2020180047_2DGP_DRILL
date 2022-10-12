import pico2d
import play_state
import logo_state

# start_state = logo_state # 모듈을 변수 취급
pico2d.open_canvas()
states = [logo_state, play_state]
# game main loop code
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

# finalization code
pico2d.close_canvas()
