import turtle
import random
from multiprocessing import Process
import time

#우주선 스킨 생성
sc=turtle.Screen()
me_up="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_up.gif"
me_down="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_down.gif"
me_lt="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_lt.gif"
me_rt="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_rt.gif"
#우주선 스킨 적용
sc.addshape(me_up)
sc.addshape(me_down)
sc.addshape(me_lt)
sc.addshape(me_rt)
#우주선 생성
suri=turtle.Turtle()
suri.shape(me_rt)
suri.up()

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

def Play_Game():
    screen = suri.getscreen()
    screen.onkeypress(gostr, "Up")
    screen.onkeypress(gobac, "Down")
    screen.onkeypress(turnleft, "Left")
    screen.onkeypress(turnright, "Right")

#게임 플레이스 지정
def create_place():
    outline=turtle.Turtle()
    outline.up()
    outline.goto(-200,200)
    outline.down()
    outline.speed(5)
    for i in range(4):
        outline.fd(400)
        outline.rt(90)
#행성 움직임
def Move_Asteroid():
    ast_list[i].setheading(8*random.randint(1,45))
    ast_list[i].fd(4)

#행성 생성
ast_image="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\asteroid.gif"
ast_sc=turtle.getscreen()
ast_sc.addshape(ast_image)
ast_list = [turtle.Turtle() for x in range(10)]
for i in range(10):
    ast_list[i].up()
    ast_list[i].shape(ast_image)
    ast_list[i].goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))

if __name__ == '__main__':
    Asteroid_Moving=Process(target=Move_Asteroid())
    Player_Moving=Process(target=Play_Game())
    while True:
        Asteroid_Moving.start()
        Player_Moving.start()
        time.sleep(0.1)
    Asteroid_Moving.join()
    Player_Moving.join()
