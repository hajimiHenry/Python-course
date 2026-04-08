import turtle as t

t.showturtle()
t.setup(800, 400)
t.forward(50)
t.goto(100, 60)
t.penup()
t.pensize(width=5)
t.pencolor("red")
t.goto(600, 456)
for i in range(4):
    t.circle(50, 33)
    t.circle(-50, 33)
t.done
