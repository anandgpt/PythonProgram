import turtle
screen=turtle.Screen()
screen.bgcolor("blue")
screen.title("Drawing Pizza Practise")
myturtle=turtle.Turtle()
myturtle.pensize(5)

for i in range(0,8):
    myturtle.forward(100)
    myturtle.backward(100)
    myturtle.left(45)

myturtle.fillcolor("red")
myturtle.begin_fill()
myturtle.circle(100)
myturtle.end_fill()
myturtle.hideturtle()

    
