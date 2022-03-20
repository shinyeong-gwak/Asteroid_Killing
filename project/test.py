#행성을 하나만 만드는 경우
import turtle
import random
import time

sc=turtle.getscreen()
asteroid_image= "C:\\Users\\Gwak\\Desktop\\classes\\python\\asteroid\\images\\asteroid.gif"
sc.addshape(asteroid_image)

ast1=turtle.Turtle()
ast1.shape(asteroid_image)
ast1.up()
#ast1.hideturtle()
ast1.goto(random.randrange(-200,200),random.randrange(-200,200))
time.sleep(1)

while True:
    ast1.setheading(90*random.randint(1,4))
    ast1.speed(1)
    ast1.fd(10)

