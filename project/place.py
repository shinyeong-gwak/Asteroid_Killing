import turtle
import random
import time

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

def asteroid_create():
    ast_image="C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\asteroid.gif"
    ast_sc=turtle.getscreen()
    ast_sc.addshape(ast_image)
    ast_list = [turtle.Turtle() for x in range(10)]
    for i in range(10):
        ast_list[i].up()
        ast_list[i].shape(ast_image)
        ast_list[i].goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))

    while True:
        for i in range(10):
            ast_list[i].setheading(8*random.randint(1,45))
            ast_list[i].fd(4)


# for i in range(20):
#     globals()['ast_{}'.format(i)] = turtle.Turtle()
#     ast_.hideturtle()
#     ast.up()
#     ast.shape(ast_image)
#     ast.goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))
# random_asteroid = ast.stamp()
