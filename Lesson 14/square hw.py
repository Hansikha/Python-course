import turtle
turtle.Screen().bgcolor("hot pink")
turtle.Screen().setup(400,400)
polygon = turtle.Turtle()

sides = 4
length = int (input("enter the length of the side of your polygon " ))
square = sides * length

for i in range (4):
    polygon.forward(length)
    polygon.right(90)

turtle.done()


