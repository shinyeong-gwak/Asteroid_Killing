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
#우주선1 생성
suri1=turtle.Turtle()
turtle.speed(8)
suri1.shape(me_rt)
suri1.up()
#우주선2 생성
suri2=turtle.Turtle()
suri2.shape(me_rt)
suri2.up()
#스코어보드 생성
score = 0
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.up()
scoreboard.goto(-200,250)
scoreboard.write(f"점수 : {score}")
#우주선 조작키
def gostr():
    suri1.shape(me_up)
    suri1.setheading(90)
    suri1.fd(8)
def gobac():
    suri1.shape(me_down)
    suri1.setheading(270)
    suri1.fd(8)
def turnleft():
    suri1.shape(me_lt)
    suri1.setheading(180)
    suri1.fd(8)
def turnright():
    suri1.shape(me_rt)
    suri1.setheading(0)
    suri1.fd(8)
def gostr2():
    suri2.shape(me_up)
    suri2.setheading(90)
    suri2.fd(8)
def gobac2():
    suri2.shape(me_down)
    suri2.setheading(270)
    suri2.fd(8)
def turnleft2():
    suri2.shape(me_lt)
    suri2.setheading(180)
    suri2.fd(8)
def turnright2():
    suri2.shape(me_rt)
    suri2.setheading(0)
    suri2.fd(8)
#게임 플레이스 지정
def Create_Place():
    outline=turtle.Turtle()
    outline.up()
    outline.hideturtle()
    outline.goto(-230,230)
    outline.down()
    outline.speed(5)
    for i in range(4):
        outline.fd(460)
        outline.rt(90)
#행성 움직임
screen = turtle.getscreen()
def Move_Asteroid():
    global score
    screen.listen()
    while True:
        screen.onkeypress(gostr2, "w")
        screen.onkeypress(gobac2, "s")
        screen.onkeypress(turnleft2, "a")
        screen.onkeypress(turnright2, "d")
        screen.onkeypress(gostr, "Up")
        screen.onkeypress(gobac, "Down")
        screen.onkeypress(turnleft, "Left")
        screen.onkeypress(turnright, "Right")
        #구역지정
        for a in range(len(turtle_list)):
            if turtle_list[a].ycor() > 200 or turtle_list[a].ycor() < -200:
                turtle_list[a].hideturtle()
                turtle_list[a].speed(10)
                turtle_list[a].sety(-(turtle_list[a].ycor()))
                turtle_list[a].showturtle()
                turtle_list[a].speed(1)
            elif turtle_list[a].xcor() > 200 or turtle_list[a].xcor() < -200:
                turtle_list[a].hideturtle()
                turtle_list[a].speed(10)
                turtle_list[a].setx(-(turtle_list[a].xcor()))
                turtle_list[a].showturtle()
                turtle_list[a].speed(1)
        for i in range(10):
            ast_list[i].setheading(8*random.randint(1,45))
            ast_list[i].fd(4)
            if suri1.distance(ast_list[i]) <= 20.00:
                if ast_list[i].isvisible() == False :
                    break
                ast_list[i].hideturtle()
                score += 1
                scoreboard.clear()
                scoreboard.write(f"점수 : {score}")
        if score == 10:
            suri1.write("레벨1\n클리어")
            break

#행성 생성
ast_sc=turtle.getscreen()
ast_sc.addshape(ast_image)
ast_list = [turtle.Turtle() for x in range(10)]
for i in range(10):
    ast_list[i].up()
    ast_list[i].shape(ast_image)
    ast_list[i].goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))

turtle_list=list()
turtle_list.append(suri1)
turtle_list.append(suri2)
turtle_list[2:]=ast_list

#행성 멋대로 움직이기 & 우주선 조작대로 움직이기
Create_Place()
Move_Asteroid()
turtle.mainloop()
