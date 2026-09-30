import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")

t = turtle.Turtle()
t.color("yellow", "orange")
t.width(10)

t.begin_fill()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

screen.mainloop()