import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,400)
polygon = turtle.Turtle()

sides = int (input("enter the amount of sides you want " ))
length = int (input("enter the length of the side of your polygon " ))
angle = 360 / sides

for i in range (sides):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()