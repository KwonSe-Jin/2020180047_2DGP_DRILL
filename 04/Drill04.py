import turtle

turtle.reset()

cnt = 0
while (cnt <= 5): #세로
    turtle.penup()
    turtle.goto(0, 300-(cnt*100))
    turtle.pendown()
    turtle.forward(500)
    cnt+=1

cnt = 0
# turtle.reset()
turtle.left(90)

while(cnt <= 5): #가로
    turtle.penup()
    turtle.goto(500-(cnt* 100), -200)
    turtle.pendown()
    turtle.forward(500)
    cnt+=1