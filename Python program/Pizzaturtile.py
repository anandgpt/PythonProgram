import turtle
screen=turtle.Screen()
screen.bgcolor("blue")
screen.title("Drawing lines practise")
myturtle=turtle.Turtle()

myturtle.shape("turtle")
myturtle.pensize(5)
myturtle.forward(100)
for i in range(0,8):
    myturtle.forward(100)
    myturtle.backward(100)
    myturtle.left(45)
turtle.hideturtle()
turtle.done()
