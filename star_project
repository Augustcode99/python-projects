import turtle
kaus = turtle.Turtle()
kaus.getscreen().bgcolor("black")
kaus.color("yellow", "yellow")
kaus.speed(50)

def star(turtle, size):
    turtle.begin_fill()
    for i in range(5):
        turtle.left(216)
        turtle.forward(size*2)
        for i in range(5):
            turtle.forward(size)
            turtle.left(216)
            for ii in range(5):
                kaus.forward(size/3)
                kaus.left(216)
    turtle.end_fill()

star(kaus, 120)

turtle.done()