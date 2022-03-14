import turtle
import random
import time

def create_place():
    outline=turtle.Turtle()
    outline.up()
    outline.goto(-200,200)
    outline.down()
    outline.speed(5)
    for i in range(4):
        outline.fd(400)
        outline.rt(90)

ast_image="C:\\Users\\Gwak\\Desktop\\수업\\파이썬\\asteroid.gif"
ast_sc=turtle.getscreen()
ast_sc.addshape(ast_image)
while True:
    ast_list = [turtle.Turtle() for x in range(20)]
    for i in range(5):
        ast_list[i].up()
        ast_list[i].shape(ast_image)
        ast_list[i].goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))


# for i in range(20):
#     globals()['ast_{}'.format(i)] = turtle.Turtle()
#     ast_.hideturtle()
#     ast.up()
#     ast.shape(ast_image)
#     ast.goto(2 * random.randrange(-100, 100), 2 * random.randrange(-100, 100))
# random_asteroid = ast.stamp()
time.sleep(5)

