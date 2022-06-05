import turtle
import random


def All_Game():
    me_up = ".\\images\\me_up.gif"
    me_down = ".\\images\\me_down.gif"
    me_lt = ".\\images\\me_lt.gif"
    me_rt = ".\\images\\me_rt.gif"
    ast_image = ".\\images\\asteroid.gif"

    # 우주선 스킨 적용
    rocket_skin = turtle.Screen()
    rocket_skin.addshape(me_up)
    rocket_skin.addshape(me_down)
    rocket_skin.addshape(me_lt)
    rocket_skin.addshape(me_rt)
    # 우주선2개 생성
    ship = [turtle.Turtle() for w in range(2)]
    for i in range(2):
        ship[i].speed(8)
        ship[i].shape(me_rt)
        ship[i].up()
    # 스코어보드 생성
    score_list = [0, 0]
    scoreboard = turtle.Turtle()
    scoreboard.hideturtle()
    scoreboard.up()
    scoreboard.goto(-200, 250)
    scoreboard.write(f"1p점수 : {score_list[1]}    |   2p점수 : {score_list[0]}")


    # 우주선 조작키
    def gostr():
        ship[0].shape(me_up)
        ship[0].setheading(90)
        ship[0].fd(8)


    def gobac():
        ship[0].shape(me_down)
        ship[0].setheading(270)
        ship[0].fd(8)


    def turnleft():
        ship[0].shape(me_lt)
        ship[0].setheading(180)
        ship[0].fd(8)


    def turnright():
        ship[0].shape(me_rt)
        ship[0].setheading(0)
        ship[0].fd(8)


    def gostr2():
        ship[1].shape(me_up)
        ship[1].setheading(90)
        ship[1].fd(8)


    def gobac2():
        ship[1].shape(me_down)
        ship[1].setheading(270)
        ship[1].fd(8)


    def turnleft2():
        ship[1].shape(me_lt)
        ship[1].setheading(180)
        ship[1].fd(8)


    def turnright2():
        ship[1].shape(me_rt)
        ship[1].setheading(0)
        ship[1].fd(8)


    # 게임 플레이스 지정
    def create_place():
        outline = turtle.Turtle()
        outline.up()
        outline.hideturtle()
        outline.goto(-230, 230)
        outline.down()
        outline.speed(5)
        for x in range(4):
            outline.fd(460)
            outline.rt(90)


    # 행성 움직임 커밋
    screen = turtle.Screen()


    def move_asteroid():
        global score_list
        screen.listen()
        while True:
            screen.onkeypress(gostr2, "w")
            screen.onkeypress(gobac2, "s")
            screen.onkeypress(turnleft2, "a")
            screen.onkeypress(turnright2, "d") # 위에까지 2p용 - 나누기
            screen.onkeypress(gostr, "Up")
            screen.onkeypress(gobac, "Down")
            screen.onkeypress(turnleft, "Left")
            screen.onkeypress(turnright, "Right")
            # 구역지정 (모든 객체들이 구간 밖으로 나가지 않도록)
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
            for b in range(10):
                ast_list[b].setheading(8 * random.randint(1, 45))
                ast_list[b].fd(4)
                for c in range(2):
                    if ship[c].distance(ast_list[b]) <= 20.00:
                        if not ast_list[b].isvisible():
                            break
                        ast_list[b].hideturtle()
                        score_list[c] += 1
                        scoreboard.clear()
                        scoreboard.write(f"1p점수 : {score_list[1]}    |   2p점수 : {score_list[0]}")
            if score_list[0] + score_list[1] == 10:
                scoreboard.write("레벨1")
                if score_list[0] > score_list[1]:
                    print("2p승")
                elif score_list[0] < score_list[1]:
                    print("1p승")
                else:
                    print("동점 level 2 시작")
                break


    # 행성 생성
    ast_sc = turtle.Screen()
    ast_sc.addshape(ast_image)
    ast_list = [turtle.Turtle() for x in range(10)]
    for i in range(10):
        ast_list[i].up()
        ast_list[i].shape(ast_image)
        ast_list[i].goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))

    turtle_list = list()
    turtle_list[0:] = ship
    turtle_list[2:] = ast_list

    # 행성 멋대로 움직이기 & 우주선 조작대로 움직이기
    create_place()
    move_asteroid()
