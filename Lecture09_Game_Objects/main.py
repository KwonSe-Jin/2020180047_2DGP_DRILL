from boy_grass_object import *

# game main loop code
while running:
    handle_events()

    # game logic
    for boy in team:
        boy.update()

    # game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    update_canvas()
    delay(0.05)

# finalization code
close_canvas()