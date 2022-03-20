import turtle
import time

sc=turtle.Screen()
me_up="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_up.gif"
me_down="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_down.gif"
me_lt="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_lt.gif"
me_rt="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_rt.gif"

sc.addshape(me_up)
sc.addshape(me_down)
sc.addshape(me_lt)
sc.addshape(me_rt)

suri=turtle.Turtle()
suri.shape(me_rt)
suri.up()

def create_me():
    def gostr():
        suri.shape(me_up)
        suri.setheading(90)
        suri.fd(2)
    def gobac():
        suri.shape(me_down)
        suri.setheading(270)
        suri.fd(2)
    def turnleft():
        suri.shape(me_lt)
        suri.setheading(180)
        suri.fd(2)
    def turnright():
        suri.shape(me_rt)
        suri.setheading(0)
        suri.fd(2)

    screen=suri.getscreen()
    screen.onkeypress(gostr,"Up")
    screen.onkeypress(gobac,"Down")
    screen.onkeypress(turnleft,"Left")
    screen.onkeypress(turnright,"Right")
    screen.listen()
