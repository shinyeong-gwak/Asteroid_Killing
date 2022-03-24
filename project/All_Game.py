import turtle
import random
#이미지 출처
me_up="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_up.gif"
me_down="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_down.gif"
me_lt="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_lt.gif"
me_rt="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\me_rt.gif"
ast_image="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\asteroid.gif"
#우주선 스킨 적용
rocket_skin=turtle.Screen()
rocket_skin.addshape(me_up)
rocket_skin.addshape(me_down)
rocket_skin.addshape(me_lt)
rocket_skin.addshape(me_rt)
#우주선 생성
suri=turtle.Turtle()
suri.shape(me_rt)
suri.up()
#스코어보드 생성
score = 0
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.up()
scoreboard.goto(-200,230)
scoreboard.write(f"점수 : {score}")
#우주선 조작키
def gostr():
    suri.shape(me_up)
    suri.setheading(90)
    suri.fd(8)
def gobac():
    suri.shape(me_down)
    suri.setheading(270)
    suri.fd(8)
def turnleft():
    suri.shape(me_lt)
    suri.setheading(180)
    suri.fd(8)
def turnright():
    suri.shape(me_rt)
    suri.setheading(0)
    suri.fd(8)
#우주선 움직여라
# def Play_Game():
#     screen.onkeypress(gostr, "Up")
#     screen.onkeypress(gobac, "Down")
#     screen.onkeypress(turnleft, "Left")
#     screen.onkeypress(turnright, "Right")

#게임 플레이스 지정
def Create_Place():
    outline=turtle.Turtle()
    outline.up()
    outline.hideturtle()
    outline.goto(-200,200)
    outline.down()
    outline.speed(5)
    for i in range(4):
        outline.fd(400)
        outline.rt(90)
#행성 움직임
screen = suri.getscreen()
def Move_Asteroid():
    global score
    screen.listen()
    while True:
        screen.onkeypress(gostr, "Up")
        screen.onkeypress(gobac, "Down")
        screen.onkeypress(turnleft, "Left")
        screen.onkeypress(turnright, "Right")
        for i in range(10):
            ast_list[i].setheading(8*random.randint(1,45))
            ast_list[i].fd(4)
            if suri.distance(ast_list[i]) <= 20.00:
                ast_list[i].hideturtle()
                score += 1
                scoreboard.clear()
                scoreboard.write(f"점수 : {score}")

#행성 생성
ast_sc=turtle.getscreen()
ast_sc.addshape(ast_image)
ast_list = [turtle.Turtle() for x in range(10)]
for i in range(10):
    ast_list[i].up()
    ast_list[i].shape(ast_image)
    ast_list[i].goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))

#행성 멋대로 움직이기 & 우주선 조작대로 움직이기
Create_Place()
Move_Asteroid()
