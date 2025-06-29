import turtle as tl
t=tl.Turtle()
t.speed(0)
col=["red","lime","cyan","magenta","blue","yellow","white"]
t.shape("turtle")
# wn=t.screen()
screen = tl.Screen()

# Change the background color to black
screen.bgcolor("black")
t.hideturtle()

for i in range(360):
    for c in col:
        t.color(c)
        t.fd(150)
        for i in range(100):
            t.fd(3)
            t.rt(5)

        for i in range(90):
            t.rt(9)
            t.bk(3)
            t.rt(3)
        t.fd(100)
for i in range(360):
    for c in col:
        t.color(c)
        t.fd(150)
        for i in range(100):
            t.fd(3)
            t.rt(5)

        for i in range(90):
            t.rt(9)
            t.bk(3)
            t.rt(3)
        t.fd(100)



t.done()
