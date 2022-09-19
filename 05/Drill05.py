import turtle

def turtle_move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_move_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(turtle_move_up, 'w')
turtle.onkey(turtle_move_right, 'd')
turtle.onkey(turtle_move_left, 'a')
turtle.onkey(turtle_move_down, 's')
turtle.onkey(restart, 'Escape')
turtle.listen()
