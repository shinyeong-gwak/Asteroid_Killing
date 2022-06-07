import turtle

class Button():
    message = 0
    def __init__(self,width=3,height=12,xco=0,yco=0,mes="버튼"):
        self.but=turtle.Turtle(shape="square")
        self.but.color("white")
        self.but.up()
        self.but.setpos(xco,yco)
        self.but.shapesize(width,height)
        self.message = mes

    def write(self):
        self.but.pencolor("black")
        self.but.write(self.message)

    # def __del__(self):
    #     self.but.clear()
    #     self.but.hideturtle()

    def func(self,fun):
        self.but.onclick(fun)
        return self.but


